#!/usr/bin/env python3
"""
Debug exactly what happens when secret code 0005 (IC-Architect) is pressed
Following SOP Tenet #2: Use Python to understand structure completely
"""

def debug_secret_code_0005():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    print("=== DEBUGGING SECRET CODE 0005 (IC-ARCHITECT) ===")
    
    # 1. Find the secret code mapping for 0005
    print("🔍 1. SECRET CODE MAPPING:")
    for i, line in enumerate(lines, 1):
        if "keySequence === '0005'" in line:
            print(f"  Line {i}: {line.strip()}")
            if i < len(lines):
                print(f"  Line {i+1}: {lines[i].strip()}")
            break
    
    # 2. Find the activateProfile function
    print("\n🔍 2. ACTIVATEPROFILE FUNCTION:")
    activate_start = None
    for i, line in enumerate(lines, 1):
        if 'function activateProfile(' in line:
            activate_start = i
            break
    
    if activate_start:
        print(f"  activateProfile starts at line {activate_start}")
        # Show first 10 lines of activateProfile
        for i in range(activate_start - 1, min(activate_start + 9, len(lines))):
            print(f"    Line {i + 1}: {lines[i].strip()}")
    
    # 3. Check if activateProfile calls setCollapsibleSections
    print("\n🔍 3. DOES ACTIVATEPROFILE CALL SETCOLLAPSIBLESECTIONS?")
    if activate_start:
        for i in range(activate_start, min(activate_start + 50, len(lines))):
            if 'setCollapsibleSections(' in lines[i]:
                print(f"  ✅ YES - Line {i + 1}: {lines[i].strip()}")
                break
        else:
            print("  ❌ NO - activateProfile doesn't call setCollapsibleSections")
    
    # 4. Check the IC-Architect implementation in setCollapsibleSections
    print("\n🔍 4. IC-ARCHITECT IMPLEMENTATION IN SETCOLLAPSIBLESECTIONS:")
    for i, line in enumerate(lines, 1):
        if "code === 'IC-Architect'" in line:
            print(f"  Found at line {i}: {line.strip()}")
            # Show next 20 lines
            for j in range(i, min(i + 20, len(lines))):
                line_content = lines[j - 1].strip()
                print(f"    Line {j}: {line_content}")
                if 'return;' in line_content:
                    break
            break
    else:
        print("  ❌ IC-Architect implementation NOT FOUND")
    
    # 5. Check for any JavaScript syntax errors in IC-Architect section
    print("\n🔍 5. SYNTAX ERROR CHECK FOR IC-ARCHITECT:")
    ic_architect_lines = []
    in_ic_architect = False
    
    for i, line in enumerate(lines, 1):
        if "code === 'IC-Architect'" in line:
            in_ic_architect = True
        elif in_ic_architect and ('code ===' in line or 'console.error' in line):
            break
        
        if in_ic_architect:
            ic_architect_lines.append((i, line))
    
    syntax_errors = []
    for line_num, line in ic_architect_lines:
        line_content = line.strip()
        if line_content and not line_content.startswith('//'):
            # Check for unmatched quotes
            single_quotes = line_content.count("'")
            double_quotes = line_content.count('"')
            
            if single_quotes % 2 != 0:
                syntax_errors.append(f"Line {line_num}: Unmatched single quotes - {line_content}")
            if double_quotes % 2 != 0:
                syntax_errors.append(f"Line {line_num}: Unmatched double quotes - {line_content}")
    
    if syntax_errors:
        print("  ❌ SYNTAX ERRORS FOUND:")
        for error in syntax_errors:
            print(f"    {error}")
    else:
        print("  ✅ No syntax errors found in IC-Architect section")
    
    # 6. Check if there are multiple IC-Architect definitions
    print("\n🔍 6. MULTIPLE IC-ARCHITECT DEFINITIONS CHECK:")
    ic_architect_count = 0
    for i, line in enumerate(lines, 1):
        if "code === 'IC-Architect'" in line:
            ic_architect_count += 1
            print(f"  Definition #{ic_architect_count} at line {i}")
    
    print(f"  Total IC-Architect definitions: {ic_architect_count}")
    
    # 7. Look for any code that might prevent execution
    print("\n🔍 7. POTENTIAL EXECUTION BLOCKERS:")
    
    # Check for early returns before IC-Architect
    setcollapsible_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            setcollapsible_start = i
            break
    
    if setcollapsible_start:
        ic_architect_line = None
        for i, line in enumerate(lines, 1):
            if "code === 'IC-Architect'" in line:
                ic_architect_line = i
                break
        
        if ic_architect_line:
            # Check for any early returns between function start and IC-Architect
            early_returns = []
            for i in range(setcollapsible_start, ic_architect_line):
                if 'return;' in lines[i - 1] and 'IC-Architect' not in lines[i - 1]:
                    early_returns.append((i, lines[i - 1].strip()))
            
            if early_returns:
                print("  ⚠️  EARLY RETURNS FOUND (could prevent IC-Architect from being reached):")
                for line_num, line_content in early_returns:
                    print(f"    Line {line_num}: {line_content}")
            else:
                print("  ✅ No early returns found before IC-Architect")
    
    print("\n💡 DEBUGGING STEPS:")
    print("1. Test secret code 0005 in browser")
    print("2. Check console for debug output from setCollapsibleSections")
    print("3. Look for any JavaScript errors that prevent execution")
    print("4. Verify the profile code being passed matches exactly 'IC-Architect'")

if __name__ == "__main__":
    debug_secret_code_0005()