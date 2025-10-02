#!/usr/bin/env python3
"""
Validate Archetype Descriptions
Verifies that all 24 profiles have unique, properly formatted archetype descriptions.
"""

import json
import sys
from pathlib import Path

def validate_archetype_descriptions():
    """Validate archetype descriptions in profiles.json"""

    # Load profiles.json
    profiles_path = Path(__file__).parent.parent / "Web-App" / "profiles.json"

    with open(profiles_path, 'r', encoding='utf-8') as f:
        profiles = json.load(f)

    print("=" * 60)
    print("ARCHETYPE DESCRIPTION VALIDATION")
    print("=" * 60)
    print()

    # Expected patterns for each orientation
    expected_patterns = {
        'IS': 'philosophical approach',
        'SI': 'philosophical approach',
        'IP': "converter's approach",
        'PI': "converter's approach",
        'IC': "explorer's approach",
        'CI': "explorer's approach",
        'PS': "builder's approach",
        'SP': "builder's approach",
        'PC': "maker's approach",
        'CP': "maker's approach",
        'CS': "translator's approach",
        'SC': "translator's approach",
    }

    errors = []
    successes = []

    for profile_code, profile_data in profiles.items():
        # Extract orientation from profile code (first 2 characters before hyphen)
        orientation = profile_code.split('-')[0]

        # Get archetype description
        if 'archetypeDescription' not in profile_data:
            errors.append(f"❌ {profile_code}: Missing archetypeDescription")
            continue

        description = profile_data['archetypeDescription']['content']

        # Check for expected pattern
        expected_pattern = expected_patterns.get(orientation)
        if expected_pattern and expected_pattern.lower() not in description.lower():
            errors.append(f"❌ {profile_code}: Missing expected pattern '{expected_pattern}'")
            continue

        # Check for (dominant) and (secondary) labels
        if '(dominant)' not in description:
            errors.append(f"❌ {profile_code}: Missing '(dominant)' label")
            continue

        if '(secondary)' not in description:
            errors.append(f"❌ {profile_code}: Missing '(secondary)' label")
            continue

        # Check for HTML formatting
        if '<strong>' not in description:
            errors.append(f"❌ {profile_code}: Missing <strong> tags for archetype names")
            continue

        successes.append(f"✅ {profile_code}: Valid archetype description")

    # Print results
    if successes:
        print("SUCCESSFUL VALIDATIONS:")
        for success in successes:
            print(f"  {success}")
        print()

    if errors:
        print("ERRORS FOUND:")
        for error in errors:
            print(f"  {error}")
        print()
        print(f"❌ {len(errors)} error(s) found")
        return False
    else:
        print(f"✅ All {len(profiles)} profiles have valid archetype descriptions!")
        return True

def main():
    success = validate_archetype_descriptions()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
