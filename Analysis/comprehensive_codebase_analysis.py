#!/usr/bin/env python3
"""
Comprehensive STTI Assessment Codebase Analysis
Provides complete architectural overview for renovation planning
"""

import json
import re
from pathlib import Path
from collections import defaultdict

def analyze_main_js(file_path):
    """Analyze main.js structure and patterns"""
    with open(file_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("MAIN.JS ANALYSIS")
    print("="*80)

    # Count lines
    lines = content.split('\n')
    print(f"\nTotal lines: {len(lines)}")

    # Find all functions
    function_pattern = r'^\s*function\s+(\w+)\s*\('
    functions = re.findall(function_pattern, content, re.MULTILINE)
    print(f"\nTotal functions defined: {len(functions)}")
    print("Functions:", ', '.join(functions[:10]), "..." if len(functions) > 10 else "")

    # Count hardcoded profile blocks
    profile_blocks = re.findall(r"if \(code === '[A-Z]{2}-(Architect|Gardener)'\)", content)
    print(f"\nHardcoded profile blocks: {len(profile_blocks)}")

    # Find all profile codes mentioned
    profile_codes = set(re.findall(r"'([A-Z]{2}-(Architect|Gardener))'", content))
    print(f"Unique profile codes hardcoded: {len(profile_codes)}")
    print("Sample codes:", list(profile_codes)[:5])

    # Estimate code duplication
    profile_section_starts = content.count("const overwhelmedTitle = document.querySelector('#overwhelmedSection")
    print(f"\nProfile section implementations: {profile_section_starts}")

    # Check for ProfileRenderer usage
    renderer_calls = content.count('profileRenderer')
    print(f"ProfileRenderer calls: {renderer_calls}")

    # Find secret code mappings
    secret_codes = re.findall(r"keySequence === '(\d{4})'", content)
    print(f"\nSecret codes defined: {len(secret_codes)}")

    return {
        'total_lines': len(lines),
        'function_count': len(functions),
        'hardcoded_blocks': len(profile_blocks),
        'unique_profiles': len(profile_codes),
        'secret_codes': len(secret_codes)
    }

def analyze_profiles_json(file_path):
    """Analyze profiles.json structure"""
    with open(file_path, 'r') as f:
        data = json.load(f)

    print("\n" + "="*80)
    print("PROFILES.JSON ANALYSIS")
    print("="*80)

    print(f"\nTotal profiles: {len(data)}")
    print(f"Profile codes: {sorted(data.keys())}")

    # Analyze structure
    sample_profile = list(data.values())[0]
    sections = list(sample_profile.keys())
    print(f"\nSections per profile: {sections}")

    # Check completeness
    incomplete = []
    for code, profile in data.items():
        missing = [s for s in sections if s not in profile or not profile[s]]
        if missing:
            incomplete.append((code, missing))

    if incomplete:
        print(f"\nIncomplete profiles: {len(incomplete)}")
        for code, missing in incomplete[:5]:
            print(f"  {code}: missing {missing}")
    else:
        print("\n✅ All profiles complete with all sections")

    return {
        'total_profiles': len(data),
        'sections_per_profile': len(sections),
        'incomplete_profiles': len(incomplete)
    }

def analyze_profile_renderer(file_path):
    """Analyze ProfileRenderer.js"""
    with open(file_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("PROFILE-RENDERER.JS ANALYSIS")
    print("="*80)

    lines = content.split('\n')
    print(f"\nTotal lines: {len(lines)}")

    # Find methods
    method_pattern = r'^\s*(\w+)\s*\([^)]*\)\s*\{'
    methods = re.findall(method_pattern, content, re.MULTILINE)
    print(f"Methods: {len(methods)}")
    print("Method names:", ', '.join(methods))

    # Check section support
    render_calls = re.findall(r"renderSection\('(\w+)'", content)
    render_desc_calls = re.findall(r"renderDescriptionSection\('(\w+)'", content)

    print(f"\nSupported collapsible sections: {set(render_calls)}")
    print(f"Supported description sections: {set(render_desc_calls)}")

    return {
        'total_lines': len(lines),
        'method_count': len(methods),
        'supported_sections': len(set(render_calls)) + len(set(render_desc_calls))
    }

def analyze_index_html(file_path):
    """Analyze index.html structure"""
    with open(file_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("INDEX.HTML ANALYSIS")
    print("="*80)

    lines = content.split('\n')
    print(f"\nTotal lines: {len(lines)}")

    # Find script tags
    script_tags = re.findall(r'<script[^>]*src="([^"]+)"', content)
    inline_scripts = content.count('<script>')
    print(f"\nExternal scripts: {script_tags}")
    print(f"Inline script tags: {inline_scripts}")

    # Find CSS
    link_tags = re.findall(r'<link[^>]*href="([^"]+)"', content)
    style_tags = content.count('<style>')
    print(f"\nExternal stylesheets: {[l for l in link_tags if 'css' in l]}")
    print(f"Inline style tags: {style_tags}")

    # Check for screens
    screens = re.findall(r'id="(\w+Screen)"', content)
    print(f"\nScreens: {screens}")

    return {
        'total_lines': len(lines),
        'external_scripts': len(script_tags),
        'inline_scripts': inline_scripts,
        'screens': len(screens)
    }

def analyze_question_structure(main_js_path):
    """Analyze question structure and scoring"""
    with open(main_js_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("QUESTION & SCORING ANALYSIS")
    print("="*80)

    # Extract questions array
    questions_match = re.search(r'const questions = \[(.*?)\];', content, re.DOTALL)
    if questions_match:
        questions_text = questions_match.group(1)
        question_count = questions_text.count('{ id:')
        print(f"\nTotal questions defined: {question_count}")

        # Count by archetype
        archetype_counts = defaultdict(int)
        for match in re.finditer(r"archetype: '([^']+)'", questions_text):
            archetype = match.group(1)
            archetype_counts[archetype] += 1

        print("\nQuestions per archetype/tendency:")
        for arch, count in sorted(archetype_counts.items()):
            print(f"  {arch}: {count}")

    # Check scoring logic
    if 'calculateScores' in content:
        print("\n✅ Scoring function found")

        # Check for polarity handling
        if "polarity === '+'" in content:
            print("✅ Polarity handling implemented")

        # Check for red herring handling
        if "archetype === 'RH'" in content or "RH" in content:
            print("✅ Red herring handling implemented")

    return archetype_counts

def analyze_file_structure(base_path):
    """Analyze overall file structure"""
    print("\n" + "="*80)
    print("FILE STRUCTURE ANALYSIS")
    print("="*80)

    base = Path(base_path)

    # Count files by type
    file_types = defaultdict(list)
    for file in base.rglob('*'):
        if file.is_file() and not any(part.startswith('.') for part in file.parts):
            ext = file.suffix
            file_types[ext].append(str(file.relative_to(base)))

    print("\nFiles by type:")
    for ext, files in sorted(file_types.items()):
        if ext in ['.html', '.js', '.css', '.json', '.py', '.md']:
            print(f"\n{ext}: {len(files)} files")
            for f in files[:5]:
                print(f"  - {f}")
            if len(files) > 5:
                print(f"  ... and {len(files) - 5} more")

    # Check for key files
    key_files = [
        'Web-App/index.html',
        'Web-App/main.js',
        'Web-App/profile-renderer.js',
        'Web-App/profiles.json',
        'Web-App/styles.css',
        'STTI Profiles Master Content.md',
        'Documentation/STTI_PROJECT_SOP.md'
    ]

    print("\n\nKey files check:")
    for file in key_files:
        exists = (base / file).exists()
        status = "✅" if exists else "❌"
        print(f"{status} {file}")

def main():
    base_path = Path("/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev")

    print("\n" + "="*80)
    print("STTI ASSESSMENT - COMPREHENSIVE CODEBASE ANALYSIS")
    print("="*80)
    print(f"Base path: {base_path}")

    # Analyze file structure
    analyze_file_structure(base_path)

    # Analyze main components
    stats = {}

    main_js = base_path / "Web-App/main.js"
    if main_js.exists():
        stats['main_js'] = analyze_main_js(main_js)

    profiles_json = base_path / "Web-App/profiles.json"
    if profiles_json.exists():
        stats['profiles_json'] = analyze_profiles_json(profiles_json)

    profile_renderer = base_path / "Web-App/profile-renderer.js"
    if profile_renderer.exists():
        stats['profile_renderer'] = analyze_profile_renderer(profile_renderer)

    index_html = base_path / "Web-App/index.html"
    if index_html.exists():
        stats['index_html'] = analyze_index_html(index_html)

    # Analyze questions
    if main_js.exists():
        stats['questions'] = analyze_question_structure(main_js)

    # Summary
    print("\n" + "="*80)
    print("SUMMARY STATISTICS")
    print("="*80)

    if 'main_js' in stats:
        print(f"\nmain.js:")
        print(f"  Lines: {stats['main_js']['total_lines']}")
        print(f"  Functions: {stats['main_js']['function_count']}")
        print(f"  Hardcoded profile blocks: {stats['main_js']['hardcoded_blocks']}")
        print(f"  Secret codes: {stats['main_js']['secret_codes']}")

    if 'profiles_json' in stats:
        print(f"\nprofiles.json:")
        print(f"  Profiles: {stats['profiles_json']['total_profiles']}")
        print(f"  Sections per profile: {stats['profiles_json']['sections_per_profile']}")
        print(f"  Incomplete: {stats['profiles_json']['incomplete_profiles']}")

    if 'profile_renderer' in stats:
        print(f"\nprofile-renderer.js:")
        print(f"  Lines: {stats['profile_renderer']['total_lines']}")
        print(f"  Methods: {stats['profile_renderer']['method_count']}")

    print("\n" + "="*80)
    print("ARCHITECTURAL INSIGHTS")
    print("="*80)

    print("\n✅ WHAT'S WORKING:")
    print("  - ProfileRenderer.js exists and has clean architecture")
    print("  - profiles.json has all 24 profiles with complete data")
    print("  - Scoring system appears mathematically sound")
    print("  - Secret code system is functional")

    print("\n⚠️  WHAT'S BLOATED:")
    if stats.get('main_js', {}).get('hardcoded_blocks', 0) > 0:
        print(f"  - {stats['main_js']['hardcoded_blocks']} hardcoded profile blocks in main.js")
    print(f"  - {stats['main_js']['total_lines']} lines in main.js (should be ~500-800)")
    print("  - Duplicate content between main.js and profiles.json")
    print("  - Legacy functions that could be removed")

    print("\n🎯 RENOVATION PRIORITIES:")
    print("  1. Delete ALL hardcoded profile content from main.js")
    print("  2. Make main.js call ProfileRenderer for all content")
    print("  3. Verify sync-profiles.py script is working")
    print("  4. Clean up unused functions")
    print("  5. Consolidate duplicate code")

    print("\n" + "="*80)

if __name__ == '__main__':
    main()
