#!/usr/bin/env python3
"""
Analyze the secret code pattern bug
Following SOP Tenet #2: Use Python to understand structure completely

Working codes: 0001-0004, 0009-0010, 0012, 0019-0024
Failing codes: 0005-0008, 0011, 0013-0018

Pattern suggests specific profiles are broken in setCollapsibleSections
"""

def analyze_secret_code_pattern():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING SECRET CODE PATTERN BUG ===")
    print("Working: 0001-0004, 0009-0010, 0012, 0019-0024")
    print("Failing: 0005-0008, 0011, 0013-0018")
    print()
    
    # First, let's find the secret code mapping
    lines = content.split('\n')
    
    # Find where secret codes are mapped to profiles
    code_mappings = []
    for i, line in enumerate(lines, 1):
        if 'case ' in line and ':' in line and ('0' in line):
            # Look for pattern like: case '0001': or similar
            if 'activateProfile(' in lines[i] if i < len(lines) else '':
                code_mappings.append((i, line.strip(), lines[i].strip() if i < len(lines) else ''))
    
    print("🔍 SECRET CODE MAPPINGS FOUND:")
    for line_num, case_line, activate_line in code_mappings[:24]:  # First 24 codes
        print(f"  Line {line_num}: {case_line}")
        print(f"  Line {line_num + 1}: {activate_line}")
        print()
    
    # Extract profile codes from the mappings
    profile_codes = []
    for line_num, case_line, activate_line in code_mappings:
        if "activateProfile('" in activate_line:
            start = activate_line.find("activateProfile('") + len("activateProfile('")
            end = activate_line.find("'", start)
            if start < end:
                profile_code = activate_line[start:end]
                # Extract the secret code
                secret_code = case_line.split("'")[1] if "'" in case_line else "unknown"
                profile_codes.append((secret_code, profile_code, line_num))
    
    print("🗂️  SECRET CODE TO PROFILE MAPPING:")
    for secret_code, profile_code, line_num in profile_codes[:24]:
        status = "✅" if secret_code in ['0001','0002','0003','0004','0009','0010','0012','0019','0020','0021','0022','0023','0024'] else "❌"
        print(f"  {status} {secret_code} -> {profile_code}")
    
    # Now analyze which profiles are failing
    working_profiles = []
    failing_profiles = []
    
    working_codes = ['0001','0002','0003','0004','0009','0010','0012','0019','0020','0021','0022','0023','0024']
    failing_codes = ['0005','0006','0007','0008','0011','0013','0014','0015','0016','0017','0018']
    
    for secret_code, profile_code, line_num in profile_codes:
        if secret_code in working_codes:
            working_profiles.append(profile_code)
        elif secret_code in failing_codes:
            failing_profiles.append(profile_code)
    
    print(f"\n✅ WORKING PROFILES ({len(working_profiles)}):")
    for profile in working_profiles:
        print(f"  {profile}")
    
    print(f"\n❌ FAILING PROFILES ({len(failing_profiles)}):")
    for profile in failing_profiles:
        print(f"  {profile}")
    
    # Check what's different about failing profiles in setCollapsibleSections
    print(f"\n🔍 ANALYZING SETCOLLAPSIBLESECTIONS FOR FAILING PROFILES:")
    
    # Find setCollapsibleSections function
    setcollapsible_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            setcollapsible_start = i
            break
    
    if setcollapsible_start:
        print(f"setCollapsibleSections function starts at line {setcollapsible_start}")
        
        # Check if each failing profile has a case in setCollapsibleSections
        missing_profiles = []
        broken_profiles = []
        
        for profile in failing_profiles:
            profile_found = False
            profile_lines = []
            
            # Search for this profile in setCollapsibleSections
            for i in range(setcollapsible_start, min(setcollapsible_start + 1000, len(lines))):
                if f"code === '{profile}'" in lines[i] or f'code === "{profile}"' in lines[i]:
                    profile_found = True
                    # Collect the next 20 lines to see the implementation
                    for j in range(i, min(i + 20, len(lines))):
                        profile_lines.append((j + 1, lines[j].strip()))
                        if 'break;' in lines[j]:
                            break
                    break
            
            if not profile_found:
                missing_profiles.append(profile)
            else:
                # Check if the implementation looks complete
                implementation_text = '\n'.join([line for _, line in profile_lines])
                if len(profile_lines) < 5 or 'textContent' not in implementation_text:
                    broken_profiles.append((profile, profile_lines))
        
        if missing_profiles:
            print(f"\n❌ MISSING PROFILES IN SETCOLLAPSIBLESECTIONS ({len(missing_profiles)}):")
            for profile in missing_profiles:
                print(f"  {profile}")
        
        if broken_profiles:
            print(f"\n🔧 PROFILES WITH INCOMPLETE IMPLEMENTATIONS ({len(broken_profiles)}):")
            for profile, lines_list in broken_profiles:
                print(f"\n  {profile}:")
                for line_num, line_content in lines_list[:5]:  # Show first 5 lines
                    print(f"    Line {line_num}: {line_content}")
    
    # Check for syntax errors in the failing profile sections
    print(f"\n🔍 CHECKING FOR SYNTAX ERRORS IN FAILING PROFILE SECTIONS:")
    
    for profile in failing_profiles[:5]:  # Check first 5 failing profiles
        print(f"\nChecking {profile}:")
        
        # Find this profile's section
        for i in range(setcollapsible_start if setcollapsible_start else 0, len(lines)):
            if f"code === '{profile}'" in lines[i]:
                # Check the next 15 lines for syntax issues
                for j in range(i, min(i + 15, len(lines))):
                    line = lines[j]
                    line_num = j + 1
                    
                    # Check for common syntax errors
                    if line.count("'") % 2 != 0 and '//' not in line:
                        print(f"  ⚠️  Line {line_num}: Unmatched quotes - {line.strip()}")
                    if line.count('"') % 2 != 0 and '//' not in line:
                        print(f"  ⚠️  Line {line_num}: Unmatched double quotes - {line.strip()}")
                    if '{' in line and '}' not in line and 'if' in line:
                        # Check if the closing brace is on the next few lines
                        found_closing = False
                        for k in range(j + 1, min(j + 5, len(lines))):
                            if '}' in lines[k]:
                                found_closing = True
                                break
                        if not found_closing:
                            print(f"  ⚠️  Line {line_num}: Missing closing brace - {line.strip()}")
                    
                    if 'break;' in line:
                        break
                break
    
    print(f"\n💡 HYPOTHESIS:")
    print("The pattern suggests that specific profiles in setCollapsibleSections have:")
    print("1. Missing case statements")
    print("2. Syntax errors (unmatched quotes, missing braces)")
    print("3. Incomplete implementations")
    print("4. JavaScript errors that prevent execution")

if __name__ == "__main__":
    analyze_secret_code_pattern()