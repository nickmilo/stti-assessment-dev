#!/usr/bin/env python3
"""
Fix IS-Gardener wording: change "drop into" to "move into"
"""

def fix_is_gardener_wording():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing IS-Gardener wording...")
    
    # Change "drop into" to "move into" in the prompts section
    old_text = "you\\'ll likely find it becomes easier to drop into your Producer archetype"
    new_text = "you\\'ll likely find it becomes easier to move into your Producer archetype"
    
    if old_text in content:
        content = content.replace(old_text, new_text)
        print("✅ Changed 'drop into' to 'move into' in IS-Gardener prompts")
    else:
        print("❌ Could not find the text to replace")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ IS-Gardener wording updated")

if __name__ == "__main__":
    fix_is_gardener_wording()