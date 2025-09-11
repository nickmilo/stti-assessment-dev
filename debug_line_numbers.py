#!/usr/bin/env python3
"""
Debug the exact line numbers and function placement
"""

def debug_line_numbers():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        lines = f.readlines()
    
    print("=== LINE NUMBER ANALYSIS ===\n")
    
    # Find key line numbers
    key_lines = {
        'activateProfile': [],
        'setTendencyPills call': [],
        'setTendencyPills function': [],
        'setOrientation function': [],
        'setArchetypeDescription function': []
    }
    
    for i, line in enumerate(lines, 1):
        if 'function activateProfile' in line:
            key_lines['activateProfile'].append(i)
        elif 'setTendencyPills(code)' in line:
            key_lines['setTendencyPills call'].append(i)
        elif 'function setTendencyPills' in line:
            key_lines['setTendencyPills function'].append(i)
        elif 'function setOrientation' in line:
            key_lines['setOrientation function'].append(i)
        elif 'function setArchetypeDescription' in line:
            key_lines['setArchetypeDescription function'].append(i)
    
    print("📋 Key line numbers:")
    for key, line_nums in key_lines.items():
        if line_nums:
            print(f"   {key}: {line_nums}")
        else:
            print(f"   {key}: NOT FOUND")
    
    # Check the specific error line (1656)
    if len(lines) >= 1656:
        print(f"\n🔍 Line 1656 (error line): {lines[1655].strip()}")
        
        # Show context around line 1656
        start = max(0, 1656 - 5)
        end = min(len(lines), 1656 + 5)
        print(f"\nContext around line 1656:")
        for i in range(start, end):
            marker = " >>> " if i + 1 == 1656 else "     "
            print(f"{marker}{i+1:4d}: {lines[i].rstrip()}")
    
    # Check if functions are defined before they're called
    tendency_func_lines = key_lines['setTendencyPills function']
    tendency_call_lines = key_lines['setTendencyPills call']
    
    if tendency_func_lines and tendency_call_lines:
        func_line = tendency_func_lines[0]
        call_line = tendency_call_lines[0]
        print(f"\n📊 Function order check:")
        print(f"   setTendencyPills function defined: line {func_line}")
        print(f"   setTendencyPills called: line {call_line}")
        if func_line > call_line:
            print("   ❌ PROBLEM: Function called before it's defined!")
        else:
            print("   ✅ Function defined before it's called")

if __name__ == "__main__":
    debug_line_numbers()