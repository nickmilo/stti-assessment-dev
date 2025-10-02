#!/usr/bin/env python3
"""
Fix the try/catch syntax error
"""

def fix_try_catch_syntax():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing try/catch syntax error...")
    
    # The issue is that there's a missing 'try {' before the catch block
    # Looking at the activateProfile function, it should have a try block wrapping the main logic
    
    # Find the problematic section
    old_section = '''                    if (code === 'IS-Architect') {
                        loadISArchitectContent();

                    // TODO: Add other profiles here one by one

                    console.log(`${code} activated successfully`);
                }
            } catch (err) {'''
    
    new_section = '''                    if (code === 'IS-Architect') {
                        loadISArchitectContent();
                    }
                    // TODO: Add other profiles here one by one

                    console.log(`${code} activated successfully`);
                }
            } catch (err) {'''
    
    if old_section in content:
        content = content.replace(old_section, new_section)
        print("✅ Fixed missing closing brace in activateProfile function")
    else:
        print("❌ Could not find the problematic section")
        
        # Try alternative fix - look for the pattern more broadly
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'loadISArchitectContent();' in line and i < len(lines) - 5:
                # Check if the next few lines have the issue
                if lines[i+1].strip() == '' and lines[i+2].strip().startswith('// TODO'):
                    # Fix the structure
                    lines[i+1] = '                    }'
                    content = '\n'.join(lines)
                    print("✅ Fixed missing closing brace (alternative method)")
                    break
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Syntax error should be fixed - secret codes should work again")

if __name__ == "__main__":
    fix_try_catch_syntax()