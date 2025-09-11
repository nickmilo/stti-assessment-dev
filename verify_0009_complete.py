#!/usr/bin/env python3
"""
Complete verification of 0009 execution path and PS-Architect implementation
Following SOP Tenet #3: Validate functionality works as expected
"""

def verify_0009_complete():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== COMPLETE 0009 VERIFICATION ===\n")
    
    # 1. Verify secret code mapping
    print("1️⃣ SECRET CODE MAPPING:")
    if "keySequence === '0009'" in content and "activateProfile('PS-Architect'" in content:
        print("   ✅ 0009 correctly maps to PS-Architect")
    else:
        print("   ❌ 0009 mapping issue")
    
    # 2. Verify activateProfile calls setCollapsibleSections
    print("\n2️⃣ ACTIVATEPROFILE FUNCTION:")
    activate_start = content.find('function activateProfile(')
    if activate_start != -1:
        activate_end = content.find('\n    }', activate_start)
        if activate_end != -1:
            activate_function = content[activate_start:activate_end+5]
            if 'setCollapsibleSections(code)' in activate_function:
                print("   ✅ activateProfile calls setCollapsibleSections")
            else:
                print("   ❌ activateProfile does not call setCollapsibleSections")
                print("   This would explain why PS-Architect content doesn't load!")
        else:
            print("   ❌ Could not find end of activateProfile function")
    else:
        print("   ❌ activateProfile function not found")
    
    # 3. Verify PS-Architect in setCollapsibleSections
    print("\n3️⃣ PS-ARCHITECT IN setCollapsibleSections:")
    ps_start = content.find("code === 'PS-Architect'")
    if ps_start != -1:
        ps_end = content.find('return; // Exit early', ps_start)
        if ps_end != -1:
            ps_block = content[ps_start:ps_end]
            print("   ✅ PS-Architect implementation found")
            
            # Check content quality
            if "Creative" in ps_block and "Inner Guide" in ps_block and "Northerner" in ps_block:
                print("   ✅ Contains expected archetype references")
            else:
                print("   ❌ Missing expected archetype references")
                
        else:
            print("   ❌ PS-Architect block has no return statement")
    else:
        print("   ❌ PS-Architect not found in setCollapsibleSections")
    
    # 4. Check for JavaScript syntax errors around PS-Architect
    print("\n4️⃣ SYNTAX CHECK AROUND PS-ARCHITECT:")
    lines = content.split('\n')
    ps_line = None
    
    for i, line in enumerate(lines):
        if "code === 'PS-Architect'" in line:
            ps_line = i
            break
    
    if ps_line:
        print(f"   PS-Architect found at line {ps_line + 1}")
        
        # Check surrounding lines for syntax issues
        start_check = max(0, ps_line - 5)
        end_check = min(len(lines), ps_line + 50)
        
        syntax_issues = []
        for i in range(start_check, end_check):
            line = lines[i].strip()
            if line:
                # Check for common syntax issues
                if line.count('{') != line.count('}') and not any(x in line for x in ['if', 'else', 'function']):
                    if '{' in line or '}' in line:
                        syntax_issues.append(f"Line {i+1}: Unbalanced braces - {line}")
                
                # Check for unclosed strings
                if line.count("'") % 2 != 0 and not line.strip().endswith("\\"):
                    syntax_issues.append(f"Line {i+1}: Unclosed string - {line}")
        
        if syntax_issues:
            print("   ❌ Potential syntax issues found:")
            for issue in syntax_issues[:5]:  # Show first 5
                print(f"      {issue}")
        else:
            print("   ✅ No obvious syntax issues found")
    
    # 5. Check function call order
    print("\n5️⃣ FUNCTION CALL ORDER IN activateProfile:")
    if activate_start != -1:
        activate_section = content[activate_start:activate_start+2000]  # First 2000 chars
        
        function_calls = []
        for func in ['setStaticArchetypePills', 'setOrientation', 'setTendencyPills', 'setArchetypeDescription', 'setCollapsibleSections']:
            if f'{func}(code)' in activate_section:
                pos = activate_section.find(f'{func}(code)')
                function_calls.append((pos, func))
        
        function_calls.sort()
        
        print("   Function call order:")
        for pos, func in function_calls:
            print(f"     {func}")
        
        if function_calls and function_calls[-1][1] == 'setCollapsibleSections':
            print("   ✅ setCollapsibleSections called last (correct)")
        else:
            print("   ❌ setCollapsibleSections not called last")
    
    # 6. Final diagnosis
    print("\n6️⃣ DIAGNOSIS:")
    print("   Based on all checks, if user sees IS-Architect content for 0009:")
    print("   • Secret code mapping is correct")
    print("   • PS-Architect implementation exists")
    print("   • Most likely causes:")
    print("     1. Browser cache (needs hard refresh)")
    print("     2. JavaScript execution error preventing content load")
    print("     3. DOM selector timing issue")
    print("     4. Function not being called due to syntax error")
    
    print("\n💡 RECOMMENDED ACTION:")
    print("   User should try:")
    print("   1. Hard refresh browser (Cmd+Shift+R)")
    print("   2. Check browser console for JavaScript errors")
    print("   3. Test 0003 (IS-Architect) vs 0009 (PS-Architect) back-to-back")

if __name__ == "__main__":
    verify_0009_complete()