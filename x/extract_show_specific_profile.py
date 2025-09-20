#!/usr/bin/env python3
"""
Extract the showSpecificProfile function to see what's missing
"""

def extract_show_specific_profile():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    # Find the showSpecificProfile function
    start = content.find('function showSpecificProfile(profile) {')
    if start == -1:
        print("❌ showSpecificProfile function not found")
        return
    
    # Find the end of the function
    brace_count = 0
    in_function = False
    end = start
    
    for i, char in enumerate(content[start:], start):
        if char == '{':
            brace_count += 1
            in_function = True
        elif char == '}':
            brace_count -= 1
            if in_function and brace_count == 0:
                end = i + 1
                break
    
    function_code = content[start:end]
    
    print("=== FULL showSpecificProfile FUNCTION ===")
    print(function_code)
    
    # Check for function calls
    function_calls = ['setStaticArchetypePills', 'setOrientation', 'setTendencyPills', 'setArchetypeDescription', 'setCollapsibleSections']
    
    print("\n📋 Function calls check:")
    for func_call in function_calls:
        if f'{func_call}(' in function_code:
            print(f"   ✅ {func_call} called")
        else:
            print(f"   ❌ {func_call} MISSING")

if __name__ == "__main__":
    extract_show_specific_profile()