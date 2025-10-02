#!/usr/bin/env python3
"""
Debug what happens when 0009 is executed vs 0003 (IS-Architect)
Following SOP Tenet #3: Validate functionality works as expected
"""

def debug_0009_execution():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== DEBUGGING 0009 vs 0003 EXECUTION ===\n")
    
    # Check the exact secret code triggering logic
    lines = content.split('\n')
    
    print("🔍 Secret code 0009 execution path:")
    for i, line in enumerate(lines):
        if "keySequence === '0009'" in line:
            print(f"   Line {i+1}: {line.strip()}")
            # Show next 3 lines
            for j in range(i+1, min(i+4, len(lines))):
                print(f"   Line {j+1}: {lines[j].strip()}")
            break
    
    print("\n🔍 Secret code 0003 execution path:")
    for i, line in enumerate(lines):
        if "keySequence === '0003'" in line:
            print(f"   Line {i+1}: {line.strip()}")
            # Show next 3 lines
            for j in range(i+1, min(i+4, len(lines))):
                print(f"   Line {j+1}: {lines[j].strip()}")
            break
    
    # Check activateProfile function
    print("\n🔍 activateProfile function calls:")
    activate_profile_start = content.find('function activateProfile(')
    if activate_profile_start != -1:
        # Find function end
        brace_count = 0
        func_start = content.find('{', activate_profile_start)
        func_end = func_start
        for i, char in enumerate(content[func_start:]):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    func_end = func_start + i
                    break
        
        activate_function = content[activate_profile_start:func_end+1]
        
        # Check if PS-Architect and IS-Architect are handled differently
        if "PS-Architect" in activate_function:
            print("   ✅ PS-Architect mentioned in activateProfile")
        else:
            print("   ❌ PS-Architect NOT mentioned in activateProfile")
            
        if "IS-Architect" in activate_function:
            print("   ✅ IS-Architect mentioned in activateProfile")
        else:
            print("   ❌ IS-Architect NOT mentioned in activateProfile")
            
        # Check for any special handling
        if "profile === 'PS-Architect'" in activate_function:
            print("   🔍 PS-Architect has special handling in activateProfile")
        if "profile === 'IS-Architect'" in activate_function:
            print("   🔍 IS-Architect has special handling in activateProfile")
    
    # Check setCollapsibleSections order
    print("\n🔍 setCollapsibleSections profile order:")
    collapsible_start = content.find('function setCollapsibleSections(')
    if collapsible_start != -1:
        # Find first few profile checks
        profile_checks = []
        lines_from_func = content[collapsible_start:].split('\n')[:50]  # First 50 lines
        
        for i, line in enumerate(lines_from_func):
            if "code === '" in line and "'" in line:
                # Extract profile name
                start = line.find("'") + 1
                end = line.find("'", start)
                if start > 0 and end > start:
                    profile = line[start:end]
                    profile_checks.append((i, profile))
        
        print("   Profile check order:")
        for line_num, profile in profile_checks[:10]:  # First 10
            print(f"     {line_num}: {profile}")
            
        # Check if PS-Architect comes before IS-Architect
        ps_pos = next((i for i, p in profile_checks if p == 'PS-Architect'), None)
        is_pos = next((i for i, p in profile_checks if p == 'IS-Architect'), None)
        
        if ps_pos is not None and is_pos is not None:
            if ps_pos < is_pos:
                print(f"   ✅ PS-Architect (pos {ps_pos}) comes before IS-Architect (pos {is_pos})")
            else:
                print(f"   ❌ IS-Architect (pos {is_pos}) comes before PS-Architect (pos {ps_pos})")
                print("       This could cause PS-Architect to use IS-Architect content!")
        
    print("\n💡 ANALYSIS:")
    print("   If 0009 is showing IS-Architect content, possible causes:")
    print("   1. Browser cache - user needs to hard refresh")
    print("   2. JavaScript error preventing PS-Architect execution")
    print("   3. Function order issue in setCollapsibleSections")
    print("   4. DOM selector issue preventing content update")

if __name__ == "__main__":
    debug_0009_execution()