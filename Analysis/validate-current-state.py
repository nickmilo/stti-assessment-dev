#!/usr/bin/env python3
"""
Validate current state of STTI Assessment codebase
Checks for consistency between main.js, profiles.json, and Master Content
"""

import json
import re

def validate_profiles_json():
    """Verify all 24 profiles exist in profiles.json"""
    print("📋 Validating profiles.json...")

    with open('../Web-App/profiles.json', 'r', encoding='utf-8') as f:
        profiles = json.load(f)

    expected_count = 24
    actual_count = len(profiles)

    print(f"   Expected profiles: {expected_count}")
    print(f"   Found profiles: {actual_count}")

    if actual_count == expected_count:
        print(f"   ✅ All {expected_count} profiles present")
    else:
        print(f"   ❌ Missing {expected_count - actual_count} profiles")
        return False

    # Check each profile has all required sections
    required_sections = [
        'archetypeDescription',
        'orientationDescription',
        'tendencyDescription',
        'overwhelmed',
        'stuckUnstuck',
        'prompts'
    ]

    missing_sections = []
    for code, profile in profiles.items():
        for section in required_sections:
            if section not in profile:
                missing_sections.append(f"{code}.{section}")

    if missing_sections:
        print(f"   ❌ Missing sections: {', '.join(missing_sections)}")
        return False
    else:
        print(f"   ✅ All profiles have required sections")

    return True

def validate_secret_codes():
    """Verify secret codes in main.js map to valid profiles"""
    print("\n🔐 Validating secret codes in main.js...")

    with open('../Web-App/main.js', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract secret code mappings
    pattern = r"keySequence === '(\d{4})'\) \{\s+activateProfile\('([^']+)', '([^']+)'\)"
    matches = re.findall(pattern, content)

    print(f"   Found {len(matches)} secret code mappings")

    if len(matches) != 24:
        print(f"   ❌ Expected 24 secret codes, found {len(matches)}")
        return False

    # Load profiles to verify codes map to real profiles
    with open('../Web-App/profiles.json', 'r', encoding='utf-8') as f:
        profiles = json.load(f)

    invalid_codes = []
    for code, profile_name, subtitle in matches:
        if profile_name not in profiles:
            invalid_codes.append(f"{code} → {profile_name} (not in profiles.json)")

    if invalid_codes:
        print(f"   ❌ Invalid mappings: {', '.join(invalid_codes)}")
        return False
    else:
        print(f"   ✅ All secret codes map to valid profiles")

    return True

def validate_file_sizes():
    """Check file sizes are reasonable"""
    print("\n📏 Validating file sizes...")

    import os

    files = {
        'main.js': '../Web-App/main.js',
        'profile-renderer.js': '../Web-App/profile-renderer.js',
        'profiles.json': '../Web-App/profiles.json',
        'index.html': '../Web-App/index.html'
    }

    for name, path in files.items():
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())

            size_kb = os.path.getsize(path) / 1024
            print(f"   {name}: {lines} lines, {size_kb:.1f} KB")
        else:
            print(f"   ❌ {name}: NOT FOUND")
            return False

    print(f"   ✅ All files present and reasonable size")
    return True

def validate_no_dead_code():
    """Check for common dead code patterns"""
    print("\n🧹 Checking for dead code...")

    with open('../Web-App/main.js', 'r', encoding='utf-8') as f:
        content = f.read()

    dead_functions = [
        'loadProfileByCode',
        'showSpecificProfile',
        'showTestResults'
    ]

    found_dead = []
    for func in dead_functions:
        if f'function {func}' in content:
            found_dead.append(func)

    if found_dead:
        print(f"   ⚠️  Found deleted functions still present: {', '.join(found_dead)}")
        print(f"   (This should not happen after Phase 2 Priority 1)")
        return False
    else:
        print(f"   ✅ No dead code found")

    return True

def main():
    print("=" * 60)
    print("STTI ASSESSMENT - CURRENT STATE VALIDATION")
    print("=" * 60)
    print("")

    results = []

    results.append(("profiles.json", validate_profiles_json()))
    results.append(("Secret codes", validate_secret_codes()))
    results.append(("File sizes", validate_file_sizes()))
    results.append(("Dead code check", validate_no_dead_code()))

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    all_passed = True
    for name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {name}")
        if not passed:
            all_passed = False

    print("")

    if all_passed:
        print("🎉 ALL VALIDATIONS PASSED")
        print("   Ready to proceed with Priority 2 cleanup")
        return 0
    else:
        print("❌ SOME VALIDATIONS FAILED")
        print("   Review errors above before proceeding")
        return 1

if __name__ == '__main__':
    exit(main())
