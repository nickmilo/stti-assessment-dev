#!/usr/bin/env python3
"""
Fix order for all new functions - move them before activateProfile
"""

def fix_all_function_order():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing order for all new functions...")
    
    # Functions to move (in order)
    functions_to_move = [
        'setArchetypeDescription',
        'setCollapsibleSections'
    ]
    
    for func_name in functions_to_move:
        start_marker = f'        function {func_name}(code) {{'
        
        start = content.find(start_marker)
        if start == -1:
            print(f"❌ Could not find {func_name} function")
            continue
        
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
        print(f"📋 Found {func_name} function ({end_pos - start} characters)")
        
        # Remove the function from its current location
        content = content[:start] + content[end_pos:]
        
        # Find where to insert it (before activateProfile)
        insert_point = content.find('        function activateProfile(code, name) {')
        if insert_point == -1:
            print(f"❌ Could not find activateProfile function")
            continue
        
        # Insert the function before activateProfile
        content = content[:insert_point] + function_code + '\n        \n' + content[insert_point:]
        
        print(f"✅ Moved {func_name} function before activateProfile")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ All functions now defined before activateProfile")

if __name__ == "__main__":
    fix_all_function_order()