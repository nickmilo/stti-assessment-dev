#!/usr/bin/env python3
"""
Analyze setCollapsibleSections function structure completely
Following SOP Tenet #2: Use Python to understand structure completely
"""

def analyze_function_structure():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING SETCOLLAPSIBLESECTIONS FUNCTION STRUCTURE ===")
    
    lines = content.split('\n')
    
    # Find function boundaries
    func_start = None
    func_end = None
    
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            func_start = i
        elif func_start and 'console.error(\'setCollapsibleSections: Unknown profile code:\'' in line:
            func_end = i
            break
    
    print(f"Function spans lines {func_start} to {func_end}")
    
    # Find all profile cases within the function
    profile_cases = []
    current_profile = None
    
    for i in range(func_start - 1, func_end):
        line = lines[i]
        
        # Look for if (code === 'PROFILE') patterns
        if "if (code === '" in line and "') {" in line:
            # Extract profile name
            import re
            match = re.search(r"if \(code === '([^']+)'\)", line)
            if match:
                profile_name = match.group(1)
                profile_cases.append((i + 1, profile_name))
                current_profile = profile_name
    
    print(f"\n🔍 FOUND {len(profile_cases)} PROFILE CASES:")
    for line_num, profile in profile_cases:
        print(f"  Line {line_num}: {profile}")
    
    # Check if SP-Architect is in the list
    sp_architect_found = any(profile == 'SP-Architect' for _, profile in profile_cases)
    print(f"\n🎯 SP-ARCHITECT CHECK:")
    print(f"SP-Architect found in function: {'✅ YES' if sp_architect_found else '❌ NO'}")
    
    # Check for syntax issues that might prevent SP-Architect from being reached
    print(f"\n🔍 CHECKING FOR SYNTAX ISSUES BEFORE SP-ARCHITECT:")
    
    sp_architect_line = None
    for line_num, profile in profile_cases:
        if profile == 'SP-Architect':
            sp_architect_line = line_num
            break
    
    if sp_architect_line:
        print(f"SP-Architect case at line {sp_architect_line}")
        
        # Check preceding lines for unclosed braces or early returns
        check_start = max(func_start, sp_architect_line - 50)
        
        brace_count = 0
        for i in range(check_start - 1, sp_architect_line - 1):
            line = lines[i]
            
            # Count braces
            brace_count += line.count('{') - line.count('}')
            
            # Look for problematic patterns
            if 'return;' in line and i + 1 < sp_architect_line:
                preceding_lines = lines[max(0, i-2):i+3]
                print(f"⚠️  Early return at line {i + 1}:")
                for j, pline in enumerate(preceding_lines):
                    marker = ">>> " if j == 2 else "    "
                    print(f"{marker}Line {i + j - 1}: {pline.strip()}")
            
            # Check for function-ending patterns
            if '}' in line and brace_count <= 0:
                print(f"⚠️  Potential function closure at line {i + 1}: {line.strip()}")
    
    # Check what profiles are missing from the expected 24
    expected_profiles = [
        'IS-Architect', 'IS-Gardener', 'IP-Architect', 'IP-Gardener',
        'CP-Architect', 'CP-Gardener', 'CS-Architect', 'CS-Gardener', 
        'PS-Architect', 'PS-Gardener', 'CI-Architect', 'CI-Gardener',
        'IC-Architect', 'IC-Gardener', 'PC-Architect', 'PC-Gardener',
        'SC-Architect', 'SC-Gardener', 'SP-Architect', 'SP-Gardener',
        'SI-Architect', 'SI-Gardener', 'PI-Architect', 'PI-Gardener'
    ]
    
    found_profiles = [profile for _, profile in profile_cases]
    missing_profiles = [p for p in expected_profiles if p not in found_profiles]
    
    print(f"\n📋 PROFILE COVERAGE:")
    print(f"Expected profiles: {len(expected_profiles)}")
    print(f"Found profiles: {len(found_profiles)}")
    print(f"Missing profiles: {missing_profiles}")
    
    if 'SP-Architect' in missing_profiles:
        print("❌ SP-Architect is missing from the function!")
    elif sp_architect_found:
        print("✅ SP-Architect case exists but may be unreachable due to syntax issues")
    
    return profile_cases, missing_profiles

if __name__ == "__main__":
    analyze_function_structure()