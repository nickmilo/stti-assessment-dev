#!/usr/bin/env python3
"""
Fix syntax errors in PS-Architect section
Following SOP Tenet #1: Understand before modifying
Following SOP Tenet #3: Validate syntax after changes
"""

def fix_ps_architect_syntax():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FIXING PS-ARCHITECT SYNTAX ERRORS ===\n")
    
    # Define the fixes needed
    fixes = [
        # Line 1901 - CS-Gardener prompts (carries over into PS-Architect issues)
        {
            'old': "Once your Creative is activated, you\'ll likely find it becomes easier",
            'new': "Once your Creative is activated, you\\'ll likely find it becomes easier"
        },
        # Line 1912 - PS-Architect overwhelmed content
        {
            'old': "even if everything isn\'t perfectly planned",
            'new': "even if everything isn\\'t perfectly planned"
        },
        # Line 1920 - PS-Architect stuck content (2 apostrophes to fix)
        {
            'old': "it\'s most difficult to access your Creative archetype—yet that\'s exactly",
            'new': "it\\'s most difficult to access your Creative archetype—yet that\\'s exactly"
        },
        # Line 1928 - PS-Architect prompts content  
        {
            'old': "Once your Inner Guide is activated, you\'ll likely find it becomes easier",
            'new': "Once your Inner Guide is activated, you\\'ll likely find it becomes easier"
        }
    ]
    
    # Apply each fix
    original_content = content
    for i, fix in enumerate(fixes, 1):
        if fix['old'] in content:
            content = content.replace(fix['old'], fix['new'])
            print(f"✅ Fix {i}: Applied")
            print(f"   Changed: {fix['old'][:50]}...")
            print(f"   To:      {fix['new'][:50]}...")
        else:
            print(f"❌ Fix {i}: String not found")
            print(f"   Looking for: {fix['old'][:50]}...")
    
    # Write the fixed content
    if content != original_content:
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
            f.write(content)
        print(f"\n✅ FIXED! Applied {len([f for f in fixes if f['old'] in original_content])} syntax fixes")
        print("   PS-Architect should now load properly when using secret code 0009")
    else:
        print("\n❌ No changes made - strings not found")
    
    return content != original_content

if __name__ == "__main__":
    fix_ps_architect_syntax()