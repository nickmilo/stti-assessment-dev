#!/usr/bin/env python3
"""
Extract the full showTestResults function to find the error
"""

def extract_show_test_results():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    # Find the showTestResults function
    start = content.find('function showTestResults(targetProfile) {')
    if start == -1:
        print("❌ showTestResults function not found")
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
    
    print("=== FULL showTestResults FUNCTION ===")
    print(function_code)
    
    # Check specifically for the activateProfile call
    if 'activateProfile(' in function_code:
        print("\n✅ activateProfile call found in showTestResults")
    else:
        print("\n❌ activateProfile call NOT found in showTestResults")
    
    # Look for the specific line that calls setTendencyPills
    lines = function_code.split('\n')
    for i, line in enumerate(lines, 1):
        if 'activateProfile' in line:
            print(f"   Line {i}: {line.strip()}")

if __name__ == "__main__":
    extract_show_test_results()