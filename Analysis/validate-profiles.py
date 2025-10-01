#!/usr/bin/env python3
"""
Profile Validation Script
Validates profiles.json structure and completeness
"""

import json
import sys
from pathlib import Path

# Expected profile codes (all 24)
EXPECTED_PROFILES = [
    'IS-Architect', 'IS-Gardener',
    'IP-Architect', 'IP-Gardener',
    'CP-Architect', 'CP-Gardener',
    'CS-Architect', 'CS-Gardener',
    'PS-Architect', 'PS-Gardener',
    'CI-Architect', 'CI-Gardener',
    'IC-Architect', 'IC-Gardener',
    'PC-Architect', 'PC-Gardener',
    'SC-Architect', 'SC-Gardener',
    'SP-Architect', 'SP-Gardener',
    'SI-Architect', 'SI-Gardener',
    'PI-Architect', 'PI-Gardener'
]

# Required sections with their structure
REQUIRED_SECTIONS = {
    'archetypeDescription': ['content'],
    'orientationDescription': ['content'],
    'tendencyDescription': ['content'],
    'overwhelmed': ['title', 'content'],
    'stuckUnstuck': ['title', 'content'],
    'prompts': ['title', 'content']
}

# Optional sections
OPTIONAL_SECTIONS = {
    'archetypesSynergy': ['title', 'content']
}

class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass

def validate_profiles(json_path):
    """
    Validate profiles.json structure and content

    Args:
        json_path: Path to profiles.json file

    Returns:
        dict: Validation results with success status and messages
    """
    results = {
        'success': True,
        'errors': [],
        'warnings': [],
        'info': []
    }

    # Check file exists
    if not json_path.exists():
        results['success'] = False
        results['errors'].append(f"File not found: {json_path}")
        return results

    # Parse JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            profiles = json.load(f)
    except json.JSONDecodeError as e:
        results['success'] = False
        results['errors'].append(f"Invalid JSON: {e}")
        return results
    except Exception as e:
        results['success'] = False
        results['errors'].append(f"Error reading file: {e}")
        return results

    results['info'].append(f"✓ JSON parsed successfully")
    results['info'].append(f"✓ Found {len(profiles)} profiles")

    # Check profile count
    if len(profiles) != len(EXPECTED_PROFILES):
        results['warnings'].append(
            f"Expected {len(EXPECTED_PROFILES)} profiles, found {len(profiles)}"
        )

    # Check for missing profiles
    missing_profiles = set(EXPECTED_PROFILES) - set(profiles.keys())
    if missing_profiles:
        results['warnings'].append(
            f"Missing profiles: {', '.join(sorted(missing_profiles))}"
        )

    # Check for unexpected profiles
    unexpected_profiles = set(profiles.keys()) - set(EXPECTED_PROFILES)
    if unexpected_profiles:
        results['warnings'].append(
            f"Unexpected profiles: {', '.join(sorted(unexpected_profiles))}"
        )

    # Validate each profile
    for profile_code, profile_data in profiles.items():
        profile_errors = validate_profile(profile_code, profile_data)
        if profile_errors:
            results['success'] = False
            results['errors'].extend(profile_errors)

    # Summary
    if results['success']:
        results['info'].append(f"✅ All validation checks passed!")

    return results

def validate_profile(profile_code, profile_data):
    """
    Validate a single profile's structure and content

    Args:
        profile_code: Profile identifier (e.g., 'IS-Architect')
        profile_data: Profile data dictionary

    Returns:
        list: List of error messages (empty if valid)
    """
    errors = []

    if not isinstance(profile_data, dict):
        errors.append(f"{profile_code}: Profile data must be a dictionary")
        return errors

    # Check for required sections
    all_sections = {**REQUIRED_SECTIONS, **OPTIONAL_SECTIONS}
    for section_name, required_fields in all_sections.items():
        is_required = section_name in REQUIRED_SECTIONS

        if section_name not in profile_data:
            if is_required:
                errors.append(f"{profile_code}: Missing required section '{section_name}'")
            continue

        section_data = profile_data[section_name]

        if not isinstance(section_data, dict):
            errors.append(
                f"{profile_code}.{section_name}: Section data must be a dictionary"
            )
            continue

        # Check required fields
        for field in required_fields:
            if field not in section_data:
                errors.append(
                    f"{profile_code}.{section_name}: Missing field '{field}'"
                )
                continue

            # Check field is not empty
            value = section_data[field]
            if not isinstance(value, str):
                errors.append(
                    f"{profile_code}.{section_name}.{field}: Must be a string"
                )
            elif not value.strip():
                errors.append(
                    f"{profile_code}.{section_name}.{field}: Cannot be empty"
                )

    return errors

def print_results(results):
    """Pretty print validation results"""
    print("\n" + "="*60)
    print("PROFILE VALIDATION RESULTS")
    print("="*60 + "\n")

    # Info messages
    if results['info']:
        for msg in results['info']:
            print(f"ℹ️  {msg}")
        print()

    # Warnings
    if results['warnings']:
        print("⚠️  WARNINGS:")
        for msg in results['warnings']:
            print(f"   {msg}")
        print()

    # Errors
    if results['errors']:
        print("❌ ERRORS:")
        for msg in results['errors']:
            print(f"   {msg}")
        print()

    # Final status
    print("="*60)
    if results['success']:
        print("✅ VALIDATION PASSED")
    else:
        print("❌ VALIDATION FAILED")
    print("="*60 + "\n")

    return 0 if results['success'] else 1

def main():
    """Main entry point"""
    # Determine profiles.json path
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    json_path = project_root / 'Web-App' / 'profiles.json'

    # Allow custom path as argument
    if len(sys.argv) > 1:
        json_path = Path(sys.argv[1])

    print(f"Validating: {json_path}")

    # Run validation
    results = validate_profiles(json_path)

    # Print results and exit
    exit_code = print_results(results)
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
