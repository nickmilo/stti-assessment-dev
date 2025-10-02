#!/usr/bin/env python3
"""
Fix CP-Architect tendency logic: Inner Guide difficult → Creative pathway
Following tenet #4: One surgical change at a time
"""

def fix_cp_architect_tendency():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing CP-Architect tendency logic...")
    
    # Fix CP-Architect stuck/unstuck content
    old_cp_architect_stuck = '''stuckContent.innerHTML = 'When you combine your Easterner archetypes with an Architect tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from expression to reflection is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';'''
    
    new_cp_architect_stuck = '''stuckContent.innerHTML = 'When you combine your Easterner archetypes with an Architect tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from expression to reflection is by tapping into your Creative archetype, which aligns with your structured approach to innovation.';'''
    
    # Fix CP-Architect prompts content
    old_cp_architect_prompts = '''promptsContent.innerHTML = 'What patterns are emerging from your creative output? How can your Synthesizer help you step back and make sense of what you\\'ve created? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to create more systematically structured outcomes.';'''
    
    new_cp_architect_prompts = '''promptsContent.innerHTML = 'What patterns are emerging from your creative output? How can your Creative help you innovate within your structured approach? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access deeper meaning in your work.';'''
    
    if old_cp_architect_stuck in content:
        content = content.replace(old_cp_architect_stuck, new_cp_architect_stuck)
        print("✅ Fixed CP-Architect stuck/unstuck: Inner Guide difficult → Creative pathway")
    else:
        print("❌ Could not find CP-Architect stuck content to fix")
    
    if old_cp_architect_prompts in content:
        content = content.replace(old_cp_architect_prompts, new_cp_architect_prompts)
        print("✅ Fixed CP-Architect prompts: Creative → Inner Guide activation")
    else:
        print("❌ Could not find CP-Architect prompts content to fix")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ CP-Architect tendency logic corrected")

if __name__ == "__main__":
    fix_cp_architect_tendency()