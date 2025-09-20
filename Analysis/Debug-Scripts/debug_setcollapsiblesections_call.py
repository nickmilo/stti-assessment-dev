#!/usr/bin/env python3
"""
Debug why setCollapsibleSections still shows "Unknown profile code: SP-Architect"
Following SOP Tenet #2: Use Python to understand structure completely
"""

def debug_setcollapsible_call():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== DEBUGGING SETCOLLAPSIBLESECTIONS CALL ===")
    print("Issue: Still getting 'Unknown profile code: SP-Architect'\n")
    
    lines = content.split('\n')
    
    # 1. Check where setCollapsibleSections is called
    print("🔍 WHERE IS SETCOLLAPSIBLESECTIONS CALLED?")
    calls = []
    for i, line in enumerate(lines, 1):
        if 'setCollapsibleSections(' in line and not line.strip().startswith('//'):
            calls.append((i, line.strip()))
    
    print(f"Found {len(calls)} calls:")
    for line_num, call in calls:
        print(f"  Line {line_num}: {call}")
    
    # 2. Check the function structure for syntax errors
    print(f"\n🔍 CHECKING SETCOLLAPSIBLESECTIONS FUNCTION STRUCTURE:")
    
    func_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            func_start = i
            break
    
    if func_start:
        print(f"Function starts at line {func_start}")
        
        # Check for SP-Architect case
        sp_found = False
        sp_line = None
        for i in range(func_start, min(func_start + 1000, len(lines))):
            if "code === 'SP-Architect'" in lines[i]:
                sp_found = True
                sp_line = i + 1
                break
        
        if sp_found:
            print(f"✅ SP-Architect case found at line {sp_line}")
        else:
            print("❌ SP-Architect case NOT found in function")
        
        # Check for syntax errors around SP-Architect
        if sp_found:
            print(f"\n🔍 SYNTAX CHECK AROUND SP-ARCHITECT (lines {sp_line-3} to {sp_line+10}):")
            start = max(0, sp_line - 4)
            end = min(len(lines), sp_line + 10)
            
            for i in range(start, end):
                marker = ">>> " if i + 1 == sp_line else "    "
                line_content = lines[i]
                print(f"{marker}Line {i + 1}: {line_content}")
                
                # Check for obvious syntax issues
                if i + 1 >= sp_line and i + 1 <= sp_line + 10:
                    issues = []
                    if line_content.count('(') != line_content.count(')'):
                        issues.append("Unmatched parentheses")
                    if line_content.count('{') != line_content.count('}'):
                        issues.append("Unmatched braces")
                    if line_content.count("'") % 2 != 0:
                        issues.append("Unmatched quotes")
                    if issues:
                        print(f"      ⚠️  Potential issues: {', '.join(issues)}")
    
    # 3. Check what happens after all profile cases
    print(f"\n🔍 CHECKING FUNCTION ENDING:")
    
    # Find where the error is logged
    error_line = None
    for i, line in enumerate(lines, 1):
        if 'Unknown profile code' in line:
            error_line = i
            break
    
    if error_line:
        print(f"Error logged at line {error_line}")
        print(f"Context around error:")
        start = max(0, error_line - 5)
        end = min(len(lines), error_line + 3)
        
        for i in range(start, end):
            marker = ">>> " if i + 1 == error_line else "    "
            print(f"{marker}Line {i + 1}: {lines[i]}")
    
    # 4. Hypothesis
    print(f"\n💡 DEBUGGING HYPOTHESIS:")
    print("If SP-Architect case exists but error still occurs, possible causes:")
    print("1. JavaScript syntax error preventing function from parsing correctly")
    print("2. Function is being called with incorrect parameter")
    print("3. Browser caching old version of the code")
    print("4. Race condition - function called before DOM is ready")
    print("5. SP-Architect case has syntax error preventing execution")
    
    print(f"\n🔧 SUGGESTED DEBUGGING STEPS:")
    print("1. Add console.log at start of setCollapsibleSections to see what code is received")
    print("2. Add console.log right before SP-Architect case")
    print("3. Check browser console for JavaScript syntax errors")
    print("4. Hard refresh browser (Cmd+Shift+R) to clear cache")

if __name__ == "__main__":
    debug_setcollapsible_call()