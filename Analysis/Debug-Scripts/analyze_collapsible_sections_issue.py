#!/usr/bin/env python3
"""
Analyze why collapsible sections appear in secret codes but not actual results
Following SOP Tenet #2: Use Python script to understand structure completely
Following SOP Tenet #1: Understand before making ANY changes
"""

def analyze_collapsible_sections():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING COLLAPSIBLE SECTIONS ISSUE ===")
    print("Working version 0.9.9 - SECRET CODES show sections, ACTUAL RESULTS don't\n")
    
    lines = content.split('\n')
    
    # 1. Find all functions that might handle results display
    print("🔍 RESULTS DISPLAY FUNCTIONS:")
    
    result_functions = []
    for i, line in enumerate(lines, 1):
        if 'function ' in line and any(keyword in line.lower() for keyword in ['result', 'profile', 'test']):
            func_name = line.strip().split('function ')[1].split('(')[0]
            result_functions.append((i, func_name))
            print(f"  Line {i}: {func_name}()")
    
    # 2. Find which functions call setCollapsibleSections
    print(f"\n🔍 SETCOLLAPSIBLESECTIONS CALLS:")
    
    setcollapsible_calls = []
    for i, line in enumerate(lines, 1):
        if 'setCollapsibleSections(' in line and 'function' not in line:
            setcollapsible_calls.append((i, line.strip()))
            print(f"  Line {i}: {line.strip()}")
    
    print(f"\nFound {len(setcollapsible_calls)} calls to setCollapsibleSections")
    
    # 3. Analyze showResults vs showTestResults vs showSpecificProfile
    key_functions = ['showResults', 'showTestResults', 'showSpecificProfile']
    
    for func_name in key_functions:
        print(f"\n🔍 ANALYZING {func_name.upper()} FUNCTION:")
        
        # Find function start
        func_start = None
        func_end = None
        
        for i, line in enumerate(lines, 1):
            if f'function {func_name}(' in line:
                func_start = i
                break
        
        if func_start:
            # Find function end
            brace_count = 0
            for i in range(func_start - 1, len(lines)):
                line = lines[i]
                brace_count += line.count('{') - line.count('}')
                if brace_count == 0 and i > func_start - 1:
                    func_end = i + 1
                    break
            
            print(f"  Function: lines {func_start} to {func_end}")
            
            # Check if it calls setCollapsibleSections
            calls_setcollapsible = False
            calls_activateprofile = False
            
            for i in range(func_start - 1, func_end):
                line = lines[i]
                if 'setCollapsibleSections(' in line:
                    calls_setcollapsible = True
                    print(f"    ✅ Calls setCollapsibleSections at line {i + 1}")
                if 'activateProfile(' in line:
                    calls_activateprofile = True
                    print(f"    ✅ Calls activateProfile at line {i + 1}")
            
            if not calls_setcollapsible and not calls_activateprofile:
                print(f"    ❌ Does NOT call setCollapsibleSections or activateProfile")
                print(f"    ⚠️  This might be why collapsible sections are missing!")
        else:
            print(f"  Function not found")
    
    # 4. Check activateProfile function
    print(f"\n🔍 ANALYZING ACTIVATEPROFILE FUNCTION:")
    
    activate_start = None
    for i, line in enumerate(lines, 1):
        if 'function activateProfile(' in line:
            activate_start = i
            break
    
    if activate_start:
        print(f"  activateProfile starts at line {activate_start}")
        
        # Check what activateProfile calls
        brace_count = 0
        for i in range(activate_start - 1, min(activate_start + 50, len(lines))):
            line = lines[i]
            brace_count += line.count('{') - line.count('}')
            
            if 'setCollapsibleSections(' in line:
                print(f"    ✅ activateProfile calls setCollapsibleSections at line {i + 1}")
            
            if brace_count == 0 and i > activate_start - 1:
                break
    
    # 5. Check what secret codes do differently
    print(f"\n🔍 SECRET CODE FLOW ANALYSIS:")
    
    # Find showTestResults function
    test_results_start = None
    for i, line in enumerate(lines, 1):
        if 'function showTestResults(' in line:
            test_results_start = i
            break
    
    if test_results_start:
        print(f"  showTestResults starts at line {test_results_start}")
        
        # See what showTestResults calls
        for i in range(test_results_start - 1, min(test_results_start + 30, len(lines))):
            line = lines[i]
            if 'activateProfile(' in line:
                print(f"    ✅ showTestResults calls activateProfile at line {i + 1}")
                print(f"    📋 SECRET CODE PATH: showTestResults → activateProfile → setCollapsibleSections")
                break
    
    # 6. Determine the fix needed
    print(f"\n📋 ISSUE DIAGNOSIS:")
    print("  SECRET CODES work because:")
    print("    showTestResults → activateProfile → setCollapsibleSections")
    print("  ACTUAL RESULTS fail because:")
    print("    showResults → ??? (missing setCollapsibleSections call)")
    
    print(f"\n🔧 REQUIRED FIX:")
    print("  showResults function needs to call setCollapsibleSections")
    print("  This should be added AFTER profile is created but BEFORE results display")
    
    # 7. Find the exact location where the call should be added
    print(f"\n🎯 EXACT INSERTION POINT:")
    
    show_results_start = None
    for i, line in enumerate(lines, 1):
        if 'function showResults()' in line:
            show_results_start = i
            break
    
    if show_results_start:
        # Find where profile is created and where we should add the call
        for i in range(show_results_start - 1, min(show_results_start + 50, len(lines))):
            line = lines[i]
            if 'const profile = determineProfile(' in line or 'var profile = determineProfile(' in line:
                print(f"    Profile created at line {i + 1}: {line.strip()}")
                print(f"    ➡️  Add 'setCollapsibleSections(profile.code);' after this line")
                break
    
    return True

if __name__ == "__main__":
    analyze_collapsible_sections()