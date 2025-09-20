#!/usr/bin/env python3
"""
Fix function order - move setTendencyPills before activateProfile
"""

def fix_function_order():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing function order...")
    
    # Find and extract the setTendencyPills function
    start_marker = '        function setTendencyPills(code) {'
    end_marker = '        }'
    
    start = content.find(start_marker)
    if start == -1:
        print("❌ Could not find setTendencyPills function")
        return
    
    # Find the end of the function
    temp_content = content[start:]
    brace_count = 0
    end_pos = 0
    
    for i, char in enumerate(temp_content):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = start + i + 1
                break
    
    # Extract the function
    function_code = content[start:end_pos]
    print(f"📋 Found function ({end_pos - start} characters)")
    
    # Remove the function from its current location
    content = content[:start] + content[end_pos:]
    
    # Find where to insert it (before activateProfile)
    insert_point = content.find('        function activateProfile(code, name) {')
    if insert_point == -1:
        print("❌ Could not find activateProfile function")
        return
    
    # Insert the function before activateProfile
    content = content[:insert_point] + function_code + '\n        \n' + content[insert_point:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Moved setTendencyPills function before activateProfile")
    print("✅ Function is now defined before it's called")

if __name__ == "__main__":
    fix_function_order()