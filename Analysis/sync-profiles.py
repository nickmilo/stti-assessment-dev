#!/usr/bin/env python3
"""
Sync Profiles Script
Parses STTI Profiles Master Content.md and generates profiles.json
"""

import json
import re
import sys
import subprocess
from pathlib import Path

# Section headers to look for
SECTION_HEADERS = [
    'Archetype Description',
    'Orientation Description',
    'Tendency Description',
    'Overwhelmed',
    'Stuck/Unstuck',
    'Prompts',
    'Archetype Synergy'
]

# Map section headers to JSON keys
SECTION_MAP = {
    'Archetype Description': 'archetypeDescription',
    'Orientation Description': 'orientationDescription',
    'Tendency Description': 'tendencyDescription',
    'Overwhelmed': 'overwhelmed',
    'Stuck/Unstuck': 'stuckUnstuck',
    'Prompts': 'prompts',
    'Archetype Synergy': 'archetypesSynergy'
}

# Description sections (only have content, no title)
DESCRIPTION_SECTIONS = {
    'archetypeDescription',
    'orientationDescription',
    'tendencyDescription'
}

class ParserError(Exception):
    """Custom exception for parsing errors"""
    pass

def parse_master_content(md_path):
    """
    Parse STTI Profiles Master Content.md into structured data

    Args:
        md_path: Path to the Markdown file

    Returns:
        dict: Parsed profiles data
    """
    if not md_path.exists():
        raise ParserError(f"File not found: {md_path}")

    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into profile sections
    # Pattern: ## PROFILE-CODE (description)
    profile_pattern = r'^## ([A-Z]{2}-(Architect|Gardener))'
    profile_matches = list(re.finditer(profile_pattern, content, re.MULTILINE))

    if not profile_matches:
        raise ParserError("No profile sections found in Master Content")

    print(f"Found {len(profile_matches)} profile sections")

    profiles = {}

    for i, match in enumerate(profile_matches):
        profile_code = match.group(1)
        start_pos = match.start()

        # Determine end position (start of next profile or end of file)
        if i + 1 < len(profile_matches):
            end_pos = profile_matches[i + 1].start()
        else:
            end_pos = len(content)

        profile_text = content[start_pos:end_pos]

        try:
            profile_data = parse_profile_section(profile_code, profile_text)
            profiles[profile_code] = profile_data
            print(f"  ✓ Parsed {profile_code}")
        except Exception as e:
            raise ParserError(f"Error parsing {profile_code}: {e}")

    return profiles

def parse_profile_section(profile_code, text):
    """
    Parse a single profile section into structured data

    Args:
        profile_code: Profile identifier (e.g., 'IS-Architect')
        text: Markdown text for this profile

    Returns:
        dict: Profile data with all sections
    """
    profile_data = {}

    # Find all section headers
    section_pattern = r'^### (.+?)$'
    section_matches = list(re.finditer(section_pattern, text, re.MULTILINE))

    for i, match in enumerate(section_matches):
        section_title = match.group(1).strip()

        # Skip if not a recognized section
        if section_title not in SECTION_HEADERS:
            continue

        # Extract content between this header and next header (or end)
        start_pos = match.end()
        if i + 1 < len(section_matches):
            end_pos = section_matches[i + 1].start()
        else:
            # Look for profile separator (---) or end of text
            separator = text.find('\n---\n', start_pos)
            end_pos = separator if separator != -1 else len(text)

        section_content = text[start_pos:end_pos].strip()

        # Parse section based on type
        json_key = SECTION_MAP[section_title]

        if json_key in DESCRIPTION_SECTIONS:
            # Description sections: only content
            profile_data[json_key] = {
                'content': clean_content(section_content)
            }
        else:
            # Collapsible sections: extract title and content
            title, content = parse_titled_section(section_content)
            profile_data[json_key] = {
                'title': title,
                'content': content
            }

    # Validate required sections
    required = ['archetypeDescription', 'orientationDescription', 'tendencyDescription',
                'overwhelmed', 'stuckUnstuck', 'prompts']
    missing = [s for s in required if s not in profile_data]
    if missing:
        raise ParserError(f"Missing required sections: {', '.join(missing)}")

    return profile_data

def parse_titled_section(text):
    """
    Parse a section with both title and content

    Args:
        text: Section text starting after ### header

    Returns:
        tuple: (title, content)
    """
    # Look for **Title:** or plain text on first line
    title_pattern = r'^\*\*Title:\*\*\s*(.+?)$'
    match = re.search(title_pattern, text, re.MULTILINE)

    if match:
        title = match.group(1).strip()
        # Content is everything after the title line
        content_start = match.end()
        content = text[content_start:].strip()

        # Remove **Content:** prefix if present
        content = re.sub(r'^\*\*Content:\*\*\s*', '', content, flags=re.MULTILINE)
    else:
        # No explicit title marker - use first paragraph as fallback
        # This shouldn't happen in well-formatted content
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        if paragraphs:
            title = paragraphs[0]
            content = '\n\n'.join(paragraphs[1:]) if len(paragraphs) > 1 else ''
        else:
            title = ''
            content = text

    return clean_content(title), clean_content(content)

def clean_content(text):
    """
    Clean and normalize content text

    Args:
        text: Raw content text

    Returns:
        str: Cleaned content
    """
    # Strip leading/trailing whitespace
    text = text.strip()

    # Normalize line endings
    text = text.replace('\r\n', '\n')

    # Remove excessive blank lines (max 2 consecutive newlines)
    text = re.sub(r'\n{3,}', '\n\n', text)

    return text

def generate_profiles_json(profiles, output_path, dry_run=False):
    """
    Generate profiles.json from parsed data

    Args:
        profiles: Parsed profiles dictionary
        output_path: Path to output JSON file
        dry_run: If True, don't write file, just validate

    Returns:
        bool: True if successful
    """
    # Convert to JSON
    try:
        json_str = json.dumps(profiles, indent=2, ensure_ascii=False)
    except Exception as e:
        raise ParserError(f"Error encoding JSON: {e}")

    if dry_run:
        print("\n" + "="*60)
        print("DRY RUN - Would write to:", output_path)
        print("="*60)
        print(f"File size: {len(json_str):,} bytes")
        print(f"Profiles: {len(profiles)}")
        return True

    # Write to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(json_str)
        print(f"\n✅ Written to: {output_path}")
        print(f"   File size: {len(json_str):,} bytes")
        print(f"   Profiles: {len(profiles)}")
        return True
    except Exception as e:
        raise ParserError(f"Error writing file: {e}")

def main():
    """Main entry point"""
    # Determine paths
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    master_content_path = project_root / 'STTI Profiles Master Content.md'
    output_path = project_root / 'Web-App' / 'profiles.json'

    # Check for dry-run flag
    dry_run = '--dry-run' in sys.argv

    print("="*60)
    print("STTI PROFILE SYNC")
    print("="*60)
    print(f"Source: {master_content_path.name}")
    print(f"Target: {output_path}")
    if dry_run:
        print("Mode: DRY RUN (no files will be modified)")
    print()

    try:
        # Parse master content
        print("Parsing Master Content...")
        profiles = parse_master_content(master_content_path)
        print(f"✅ Parsed {len(profiles)} profiles successfully\n")

        # Generate JSON
        print("Generating profiles.json...")
        generate_profiles_json(profiles, output_path, dry_run=dry_run)

        if not dry_run:
            # Validate generated file by running validation script
            print("\nValidating generated file...")
            validate_script = script_dir / 'validate-profiles.py'
            result = subprocess.run(
                ['python3', str(validate_script), str(output_path)],
                capture_output=False
            )

            if result.returncode == 0:
                print("\n🎉 Sync completed successfully!")
                print("Next steps:")
                print("  1. Test locally (open index.html)")
                print("  2. Test secret codes (0001-0024)")
                print("  3. Commit changes")
            else:
                print("\n⚠️  Sync completed but validation failed")
                print("Please fix errors before committing")

            sys.exit(result.returncode)
        else:
            print("\n✅ Dry run completed - no files modified")
            sys.exit(0)

    except ParserError as e:
        print(f"\n❌ Parser Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
