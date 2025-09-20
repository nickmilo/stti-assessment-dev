#!/usr/bin/env python3
"""
Analyze the difference between secret code path vs assessment completion path
Following SOP Tenet #2: Use Python to understand structure completely
"""

def analyze_code_paths():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING TWO CODE PATHS FOR COLLAPSIBLE SECTIONS ===")
    print("SECRET CODES WORK ✅ | ACTUAL ASSESSMENT FAILS ❌\n")
    
    lines = content.split('\n')
    
    # 1. Find secret code activation path
    print("🔍 1. SECRET CODE PATH ANALYSIS:")
    
    secret_code_lines = []
    for i, line in enumerate(lines, 1):
        if 'activateProfile(' in line and not line.strip().startswith('//'):
            secret_code_lines.append((i, line.strip()))
    
    print(f"Found {len(secret_code_lines)} secret code activations:")
    for line_num, line in secret_code_lines[:5]:  # Show first 5
        print(f"  Line {line_num}: {line}")
    
    # Find the activateProfile function
    activate_profile_start = None
    for i, line in enumerate(lines, 1):
        if 'function activateProfile(' in line:
            activate_profile_start = i
            break
    
    if activate_profile_start:
        print(f"\nactivateProfile function starts at line {activate_profile_start}")
        
        # Look for setCollapsibleSections calls within activateProfile
        activate_calls_setcollapsible = False
        for i in range(activate_profile_start, min(activate_profile_start + 200, len(lines))):
            if 'setCollapsibleSections(' in lines[i]:
                activate_calls_setcollapsible = True
                print(f"  ✅ activateProfile calls setCollapsibleSections at line {i + 1}")
                print(f"     {lines[i].strip()}")
                break
        
        if not activate_calls_setcollapsible:
            print("  ❌ activateProfile does NOT call setCollapsibleSections")
    
    # 2. Find assessment completion path
    print(f"\n🔍 2. ASSESSMENT COMPLETION PATH ANALYSIS:")
    
    # Look for showResults function (likely called on 53rd question)
    show_results_start = None
    for i, line in enumerate(lines, 1):
        if 'function showResults(' in line:
            show_results_start = i
            break
    
    if show_results_start:
        print(f"showResults function starts at line {show_results_start}")
        
        # Look for setCollapsibleSections calls within showResults
        show_results_calls_setcollapsible = False
        setcollapsible_calls_in_showresults = []
        
        for i in range(show_results_start, min(show_results_start + 1000, len(lines))):
            if 'setCollapsibleSections(' in lines[i] and not lines[i].strip().startswith('//'):
                show_results_calls_setcollapsible = True
                setcollapsible_calls_in_showresults.append((i + 1, lines[i].strip()))
        
        if setcollapsible_calls_in_showresults:
            print(f"  ✅ showResults calls setCollapsibleSections:")
            for line_num, call in setcollapsible_calls_in_showresults:
                print(f"     Line {line_num}: {call}")
        else:
            print("  ❌ showResults does NOT call setCollapsibleSections")
    
    # 3. Look for other places that might set collapsible content
    print(f"\n🔍 3. OTHER COLLAPSIBLE CONTENT SETTERS:")
    
    # Look for direct manipulation of collapsible sections
    collapsible_setters = []
    collapsible_keywords = ['overwhelmedTitle', 'overwhelmedContent', 'stuckTitle', 'stuckContent', 'promptsTitle', 'promptsContent']
    
    for i, line in enumerate(lines, 1):
        for keyword in collapsible_keywords:
            if f'{keyword}.textContent' in line or f'{keyword}.innerHTML' in line:
                # Skip if it's inside setCollapsibleSections function
                if not (1673 <= i <= 2337):  # setCollapsibleSections function boundaries
                    collapsible_setters.append((i, keyword, line.strip()))
    
    if collapsible_setters:
        print(f"Found {len(collapsible_setters)} direct collapsible content setters OUTSIDE setCollapsibleSections:")
        
        # Group by approximate location
        current_function = "Unknown"
        for line_num, keyword, line in collapsible_setters:
            # Try to identify which function this is in
            if line_num > show_results_start if show_results_start else 0:
                current_function = "showResults"
            elif line_num > activate_profile_start if activate_profile_start else 0:
                current_function = "activateProfile"
            
            print(f"  Line {line_num} ({current_function}): {line[:80]}...")
    else:
        print("  ✅ No direct collapsible content setters found outside setCollapsibleSections")
    
    # 4. Check if showResults has hardcoded IS-Architect content
    print(f"\n🔍 4. CHECKING FOR HARDCODED IS-ARCHITECT CONTENT IN SHOWRESULTS:")
    
    if show_results_start:
        # Look for IS-Architect specific text in showResults
        is_architect_patterns = [
            "When Westerners feel overwhelmed",
            "Getting stuck and unstuck as an IS-Architect", 
            "Prompts to go from West to East as an IS-Architect"
        ]
        
        hardcoded_is_architect = []
        for i in range(show_results_start, min(show_results_start + 1000, len(lines))):
            for pattern in is_architect_patterns:
                if pattern in lines[i]:
                    hardcoded_is_architect.append((i + 1, pattern, lines[i].strip()))
        
        if hardcoded_is_architect:
            print(f"  ❌ FOUND HARDCODED IS-ARCHITECT CONTENT IN SHOWRESULTS:")
            for line_num, pattern, line in hardcoded_is_architect:
                print(f"     Line {line_num}: {line[:80]}...")
        else:
            print("  ✅ No hardcoded IS-Architect content found in showResults")
    
    # 5. Summary and hypothesis
    print(f"\n🎯 ANALYSIS SUMMARY:")
    print("SECRET CODE PATH (✅ works):")
    print("  keypress -> activateProfile() -> setCollapsibleSections() -> correct content")
    
    print("\nASSESSMENT COMPLETION PATH (❌ fails):")
    if show_results_start:
        print("  question 53 -> showResults() -> ??? -> IS-Architect content")
    else:
        print("  question 53 -> ??? -> IS-Architect content")
    
    print(f"\n💡 HYPOTHESIS:")
    print("The assessment completion path either:")
    print("1. Doesn't call setCollapsibleSections() at all")
    print("2. Calls setCollapsibleSections() but then overwrites it with hardcoded content")
    print("3. Has a different function that sets collapsible content with IS-Architect defaults")
    print("4. The HTML defaults to IS-Architect and showResults() doesn't update collapsible sections")

if __name__ == "__main__":
    analyze_code_paths()