#!/usr/bin/env python3
"""
Remove duplicate orientationArchetypes declarations
Following SOP Tenet #4: Surgical fix for specific issue
"""

def fix_duplicate_orientationarchetypes():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Find and remove duplicate declarations but keep the first one we added
    declaration_found = False
    fixed_lines = []
    
    for i, line in enumerate(lines):
        if 'const orientationArchetypes = profile.dominantArchetypes.sort().join' in line:
            if not declaration_found:
                # Keep the first declaration (the one we added)
                fixed_lines.append(line)
                declaration_found = True
                print(f"✅ Keeping orientationArchetypes declaration at line {i+1}")
            else:
                # Remove subsequent declarations
                print(f"❌ Removing duplicate orientationArchetypes declaration at line {i+1}")
                # Skip this line (don't add to fixed_lines)
                continue
        else:
            fixed_lines.append(line)
    
    # Write the fixed content
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write('\n'.join(fixed_lines))
    
    print(f"✅ Fixed duplicate orientationArchetypes declarations")
    return True

if __name__ == "__main__":
    fix_duplicate_orientationarchetypes()