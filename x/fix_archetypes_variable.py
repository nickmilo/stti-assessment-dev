#!/usr/bin/env python3
"""
Fix the missing archetypes variable in showResults function
Following SOP Tenet #4: Surgical fix for critical bug
"""

def fix_archetypes_variable():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FIXING MISSING ARCHETYPES VARIABLE ===\n")
    
    # Find where to add the archetypes variable definition
    # It should be right after profile.code is available
    profile_code_line = content.find('document.getElementById(\'profileCode\').textContent = profile.code;')
    
    if profile_code_line == -1:
        print("❌ Could not find profileCode assignment")
        return False
    
    # Find the end of that line
    end_of_line = content.find('\n', profile_code_line)
    
    # Add the archetypes variable definition
    archetypes_definition = '''
            
            // Extract archetypes from profile code for description logic
            const [archetypes, tendency] = profile.code.split('-');'''
    
    new_content = content[:end_of_line] + archetypes_definition + content[end_of_line:]
    
    # Write the fixed content
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(new_content)
    
    print("✅ Added missing archetypes variable definition")
    print("   - Extracts archetypes from profile.code using split('-')")
    print("   - This should fix the ReferenceError")
    return True

if __name__ == "__main__":
    fix_archetypes_variable()