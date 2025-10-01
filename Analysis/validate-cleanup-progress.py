#!/usr/bin/env python3
"""
Validate Cleanup Progress
Track the codebase reduction progress and verify data-driven system is complete.
"""

import sys
from pathlib import Path

def validate_cleanup():
    """Validate the codebase cleanup progress"""

    main_js_path = Path(__file__).parent.parent / "Web-App" / "main.js"

    with open(main_js_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)

    print("=" * 60)
    print("STTI ASSESSMENT CODEBASE CLEANUP PROGRESS")
    print("=" * 60)
    print()

    # Historical progress
    original_lines = 2153
    priority_1_lines = 1034  # After dead code removal (52% reduction)
    priority_2_lines = 1020  # After consolidating duplicates
    priority_3_lines = 979   # After removing fallbacks
    archetype_desc_lines = 961  # After archetype description cleanup
    current_lines = line_count

    print("HISTORICAL PROGRESS:")
    print(f"  Original codebase:              {original_lines:4d} lines")
    print(f"  After Priority 1 (dead code):   {priority_1_lines:4d} lines (-{original_lines - priority_1_lines:3d}, {(1 - priority_1_lines/original_lines)*100:.1f}% reduction)")
    print(f"  After Priority 2 (duplicates):  {priority_2_lines:4d} lines (-{priority_1_lines - priority_2_lines:3d})")
    print(f"  After Priority 3 (fallbacks):   {priority_3_lines:4d} lines (-{priority_2_lines - priority_3_lines:3d})")
    print(f"  After archetype descriptions:   {archetype_desc_lines:4d} lines (-{priority_3_lines - archetype_desc_lines:3d})")
    print(f"  Current (orientation cleanup):  {current_lines:4d} lines (-{archetype_desc_lines - current_lines:3d})")
    print()

    # Total reduction
    total_reduction = original_lines - current_lines
    percent_reduction = (1 - current_lines / original_lines) * 100

    print("TOTAL REDUCTION:")
    print(f"  Lines removed:     {total_reduction:4d} lines")
    print(f"  Percent reduction: {percent_reduction:.1f}%")
    print(f"  Current size:      {current_lines:4d} lines ({(current_lines/original_lines)*100:.1f}% of original)")
    print()

    # Data-driven system checks
    print("DATA-DRIVEN SYSTEM CHECKS:")

    checks = []

    # Check for hardcoded archetype descriptions
    hardcoded_patterns = [
        ('philosophical approach', 'Archetype description pattern'),
        ("maker's approach", 'Archetype description pattern'),
        ("builder's approach", 'Archetype description pattern'),
    ]

    content = ''.join(lines)

    for pattern, description in hardcoded_patterns:
        if pattern in content:
            checks.append(f"  ❌ Found hardcoded {description}: '{pattern}'")
        else:
            checks.append(f"  ✅ No hardcoded {description}")

    # Check for ProfileRenderer usage
    if 'setArchetypeDescription(profile.code)' in content:
        checks.append("  ✅ Using setArchetypeDescription() in showResults()")
    else:
        checks.append("  ❌ Missing setArchetypeDescription() call in showResults()")

    if 'setOrientation(profile.code)' in content:
        checks.append("  ✅ Using setOrientation() in showResults()")
    else:
        checks.append("  ❌ Missing setOrientation() call in showResults()")

    if 'setProfileSubtitle(profile.code)' in content:
        checks.append("  ✅ Using setProfileSubtitle() in showResults()")
    else:
        checks.append("  ❌ Missing setProfileSubtitle() call in showResults()")

    for check in checks:
        print(check)

    print()

    # Summary
    errors = [c for c in checks if '❌' in c]
    if errors:
        print(f"❌ {len(errors)} issue(s) found")
        return False
    else:
        print("✅ All data-driven system checks passed!")
        return True

def main():
    success = validate_cleanup()
    sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
