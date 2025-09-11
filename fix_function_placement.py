#!/usr/bin/env python3
"""
Check and fix function placement and potential syntax issues
"""

def fix_function_placement():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FUNCTION PLACEMENT ANALYSIS ===\n")
    
    # Find all function definitions
    functions = []
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'function ' in line and not line.strip().startswith('//'):
            functions.append((i, line.strip()))
    
    print("📋 Function definitions found:")
    for line_num, func_line in functions:
        print(f"   Line {line_num}: {func_line}")
    
    # Check the area around setTendencyPills
    tendency_line = None
    for line_num, func_line in functions:
        if 'setTendencyPills' in func_line:
            tendency_line = line_num
            break
    
    if tendency_line:
        print(f"\n🔍 Context around setTendencyPills (line {tendency_line}):")
        start = max(0, tendency_line - 5)
        end = min(len(lines), tendency_line + 10)
        for i in range(start, end):
            marker = " >>> " if i + 1 == tendency_line else "     "
            print(f"{marker}{i+1:4d}: {lines[i]}")
    
    # Check if there's a script tag closure issue
    script_end_count = content.count('</script>')
    print(f"\n📊 Script tag analysis:")
    print(f"   </script> tags found: {script_end_count}")
    
    # Look for the exact placement issue
    if 'function setTendencyPills' in content:
        start = content.find('function setTendencyPills')
        # Look 200 chars before
        context_before = content[max(0, start-200):start]
        print(f"\n📋 Context before setTendencyPills:")
        print(context_before[-100:])

if __name__ == "__main__":
    fix_function_placement()