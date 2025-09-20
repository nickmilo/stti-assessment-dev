#!/usr/bin/env python3
"""
Fix CP-Gardener tendency logic: Synthesizer difficult → Producer pathway
Following tenet #4: One surgical change at a time
"""

def fix_cp_gardener_tendency():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing CP-Gardener tendency logic...")
    
    # Fix CP-Gardener stuck/unstuck content
    old_cp_gardener_stuck = '''stuckContent.innerHTML = 'When you combine your Easterner archetypes with a Gardener tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from expression to reflection is by tapping into your Producer archetype, which aligns with your flexible approach to getting things done.';'''
    
    new_cp_gardener_stuck = '''stuckContent.innerHTML = 'When you combine your Easterner archetypes with a Gardener tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from expression to reflection is by tapping into your Producer archetype, which aligns with your flexible approach to getting things done.';'''
    
    # Fix CP-Gardener prompts content
    old_cp_gardener_prompts = '''promptsContent.innerHTML = 'What deeper meaning is your creative work pointing toward? How can your Producer help you organize your creative insights organically? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to express insights in more meaningful ways.';'''
    
    new_cp_gardener_prompts = '''promptsContent.innerHTML = 'What deeper meaning is your creative work pointing toward? How can your Producer help you organize your creative insights organically? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to make sense of your creative expressions.';'''
    
    if old_cp_gardener_stuck in content:
        content = content.replace(old_cp_gardener_stuck, new_cp_gardener_stuck)
        print("✅ Fixed CP-Gardener stuck/unstuck: Synthesizer difficult → Producer pathway")
    else:
        print("❌ Could not find CP-Gardener stuck content to fix")
    
    if old_cp_gardener_prompts in content:
        content = content.replace(old_cp_gardener_prompts, new_cp_gardener_prompts)
        print("✅ Fixed CP-Gardener prompts: Producer → Synthesizer activation")
    else:
        print("❌ Could not find CP-Gardener prompts content to fix")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ CP-Gardener tendency logic corrected")

if __name__ == "__main__":
    fix_cp_gardener_tendency()