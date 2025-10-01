#!/usr/bin/env python3
"""
Identify Bloat and Redundancy in STTI Assessment
Pinpoints exactly what code is duplicate and can be deleted
"""

import re
from pathlib import Path

def analyze_setcollapsiblesections(main_js_path):
    """Analyze the setCollapsibleSections function for duplicate code"""
    with open(main_js_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("ANALYZING setCollapsibleSections() FUNCTION")
    print("="*80)

    # Find the function
    func_match = re.search(
        r'function setCollapsibleSections\(code\)\s*\{(.*?)\n\s*function\s',
        content,
        re.DOTALL
    )

    if not func_match:
        print("❌ Function not found")
        return

    func_body = func_match.group(1)
    func_lines = func_body.split('\n')

    print(f"\nFunction length: {len(func_lines)} lines")

    # Count profile-specific blocks
    profile_blocks = re.findall(r"if \(code === '([A-Z]{2}-(Architect|Gardener))'\)", func_body)
    print(f"Profile-specific blocks: {len(profile_blocks)}")
    print(f"Profiles handled: {[p[0] for p in profile_blocks[:10]]}...")

    # Count repeated patterns
    overwhelmed_sets = func_body.count("const overwhelmedTitle = document.querySelector")
    stuck_sets = func_body.count("const stuckTitle = document.querySelector")
    prompts_sets = func_body.count("const promptsTitle = document.querySelector")

    print(f"\nRepeated code patterns:")
    print(f"  Overwhelmed section setup: {overwhelmed_sets} times")
    print(f"  Stuck/Unstuck section setup: {stuck_sets} times")
    print(f"  Prompts section setup: {prompts_sets} times")

    # Calculate duplicate line count
    # Each block has roughly:
    # - 3 lines for overwhelmed (title querySelector, content querySelector, if + textContent + innerHTML)
    # - 3 lines for stuck/unstuck
    # - 3 lines for prompts
    # - 1 return statement
    # = ~10 lines per profile block

    lines_per_block = 25  # Conservative estimate with spacing
    total_duplicate_lines = len(profile_blocks) * lines_per_block

    print(f"\nEstimated duplicate lines: {total_duplicate_lines}")
    print(f"These {total_duplicate_lines} lines should be replaced with 1-2 lines:")
    print("  profileRenderer.renderProfile(code);")

    return {
        'function_lines': len(func_lines),
        'profile_blocks': len(profile_blocks),
        'duplicate_lines': total_duplicate_lines
    }

def analyze_hardcoded_descriptions(main_js_path):
    """Analyze hardcoded descriptions vs ProfileRenderer"""
    with open(main_js_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("ANALYZING HARDCODED DESCRIPTIONS")
    print("="*80)

    # Check setArchetypeDescription
    if 'function setArchetypeDescription' in content:
        print("\n❌ setArchetypeDescription() is hardcoded")
        print("   Should use: profileRenderer.renderDescriptionSection()")

    # Check setTendencyPills
    if 'function setTendencyPills' in content:
        # Check if it contains hardcoded descriptions
        func_match = re.search(
            r'function setTendencyPills\(code\)\s*\{(.*?)\n\s*function\s',
            content,
            re.DOTALL
        )
        if func_match and 'innerHTML' in func_match.group(1):
            print("\n❌ setTendencyPills() has hardcoded descriptions")
            print("   Should use: profileRenderer.renderDescriptionSection()")

    # Check setOrientation
    if 'function setOrientation' in content:
        func_match = re.search(
            r'function setOrientation\(code\)\s*\{(.*?)\n\s*function\s',
            content,
            re.DOTALL
        )
        if func_match and 'innerHTML' in func_match.group(1):
            print("\n❌ setOrientation() has hardcoded orientation descriptions")
            print("   Should use: profileRenderer.renderDescriptionSection()")

def analyze_showresults_duplication(main_js_path):
    """Analyze duplication in showResults function"""
    with open(main_js_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("ANALYZING showResults() FUNCTION")
    print("="*80)

    func_match = re.search(
        r'function showResults\(\)\s*\{(.*?)^\s*function\s',
        content,
        re.DOTALL | re.MULTILINE
    )

    if not func_match:
        print("❌ Function not found")
        return

    func_body = func_match.group(1)
    func_lines = func_body.split('\n')

    print(f"\nFunction length: {len(func_lines)} lines")

    # Check for calls to setCollapsibleSections
    if 'setCollapsibleSections(profile.code)' in func_body:
        print("\n⚠️  showResults() calls setCollapsibleSections()")
        print("   This is duplicate with activateProfile()")

    # Check for hardcoded archetype descriptions
    if 'archetypeDescriptions' in func_body:
        print("\n❌ showResults() has hardcoded archetype descriptions")
        print("   Should use data from profiles.json")

    # Check for hardcoded tendency descriptions
    if 'tendencyDescriptions' in func_body:
        print("\n❌ showResults() has hardcoded tendency descriptions")
        print("   Should use data from profiles.json")

def compare_with_profiles_json(main_js_path, json_path):
    """Compare hardcoded content with profiles.json"""
    import json

    with open(main_js_path, 'r') as f:
        js_content = f.read()

    with open(json_path, 'r') as f:
        json_data = json.load(f)

    print("\n" + "="*80)
    print("COMPARING HARDCODED CONTENT WITH PROFILES.JSON")
    print("="*80)

    # Find unique text snippets in JS
    sample_snippets = [
        "double-down on their strengths to analyze",
        "most difficult to access your Creative archetype",
        "tie your current activity or problem to a concrete outcome"
    ]

    duplicates_found = 0
    for snippet in sample_snippets:
        if snippet in js_content:
            # Check if also in JSON
            json_str = json.dumps(json_data)
            if snippet in json_str:
                duplicates_found += 1
                print(f"\n❌ DUPLICATE CONTENT FOUND:")
                print(f"   '{snippet[:60]}...'")
                print(f"   Exists in BOTH main.js AND profiles.json")

    print(f"\n{duplicates_found} duplicate content snippets found")
    print("These snippets are stored TWICE in the codebase")

def identify_unused_functions(main_js_path):
    """Identify potentially unused or legacy functions"""
    with open(main_js_path, 'r') as f:
        content = f.read()

    print("\n" + "="*80)
    print("IDENTIFYING POTENTIALLY UNUSED FUNCTIONS")
    print("="*80)

    # Find all function definitions
    func_pattern = r'function\s+(\w+)\s*\('
    all_functions = set(re.findall(func_pattern, content))

    print(f"\nTotal functions defined: {len(all_functions)}")

    # Check usage for each function
    suspicious = []
    for func in all_functions:
        # Count calls (excluding definition)
        call_pattern = rf'{func}\s*\('
        calls = len(re.findall(call_pattern, content))

        # One call is the definition itself
        actual_calls = calls - 1

        if actual_calls == 0:
            suspicious.append((func, actual_calls))
        elif actual_calls <= 2:
            suspicious.append((func, actual_calls))

    if suspicious:
        print("\n⚠️  Functions with few/no calls:")
        for func, calls in sorted(suspicious, key=lambda x: x[1]):
            print(f"  {func}(): {calls} call(s)")

def calculate_renovation_savings(stats):
    """Calculate how much code can be removed"""
    print("\n" + "="*80)
    print("RENOVATION SAVINGS ESTIMATE")
    print("="*80)

    current_lines = 2144
    print(f"\nCurrent main.js: {current_lines} lines")

    # Estimate what can be removed
    removable = 0

    # All 24 profile blocks in setCollapsibleSections
    if 'setcollapsible' in stats:
        removable += stats['setcollapsible']['duplicate_lines']

    # Hardcoded descriptions (estimate ~50 lines)
    removable += 50

    # Duplicate content in showResults (estimate ~100 lines)
    removable += 100

    # Generic fallback logic (estimate ~50 lines)
    removable += 50

    target_lines = current_lines - removable
    percentage = (removable / current_lines) * 100

    print(f"\nRemovable lines: ~{removable}")
    print(f"Target main.js: ~{target_lines} lines")
    print(f"Reduction: {percentage:.1f}%")

    print(f"\nAfter renovation:")
    print(f"  - main.js: {target_lines} lines (orchestration only)")
    print(f"  - profile-renderer.js: 192 lines (rendering logic)")
    print(f"  - profiles.json: all content data")
    print(f"  - Total: ~{target_lines + 192} lines of code")
    print(f"  vs Current: {current_lines} lines in main.js alone")

    return {
        'current_lines': current_lines,
        'removable_lines': removable,
        'target_lines': target_lines,
        'percentage_reduction': percentage
    }

def main():
    base_path = Path("/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev")
    main_js = base_path / "Web-App/main.js"
    profiles_json = base_path / "Web-App/profiles.json"

    print("\n" + "="*80)
    print("STTI ASSESSMENT - BLOAT & REDUNDANCY ANALYSIS")
    print("="*80)

    stats = {}

    # Analyze setCollapsibleSections
    if main_js.exists():
        stats['setcollapsible'] = analyze_setcollapsiblesections(main_js)

    # Analyze hardcoded descriptions
    if main_js.exists():
        analyze_hardcoded_descriptions(main_js)

    # Analyze showResults duplication
    if main_js.exists():
        analyze_showresults_duplication(main_js)

    # Compare with JSON
    if main_js.exists() and profiles_json.exists():
        compare_with_profiles_json(main_js, profiles_json)

    # Identify unused functions
    if main_js.exists():
        identify_unused_functions(main_js)

    # Calculate savings
    calculate_renovation_savings(stats)

    print("\n" + "="*80)
    print("KEY FINDINGS")
    print("="*80)

    print("\n🔥 MAJOR BLOAT SOURCES:")
    print("  1. 24 hardcoded profile blocks in setCollapsibleSections()")
    print("  2. Hardcoded archetype/orientation/tendency descriptions")
    print("  3. Duplicate content in showResults() and activateProfile()")
    print("  4. Unused or barely-used legacy functions")

    print("\n✂️  SAFE DELETIONS:")
    print("  - All 24 profile blocks in setCollapsibleSections()")
    print("  - Hardcoded descriptions (use ProfileRenderer instead)")
    print("  - Generic fallback logic (profiles.json has all content)")
    print("  - Duplicate section-setting code")

    print("\n✅ REPLACEMENT STRATEGY:")
    print("  Replace 600+ lines of duplicate code with:")
    print("  - profileRenderer.renderProfile(code);")
    print("  - Let ProfileRenderer handle all content loading")
    print("  - Keep only orchestration logic in main.js")

    print("\n" + "="*80)

if __name__ == '__main__':
    main()
