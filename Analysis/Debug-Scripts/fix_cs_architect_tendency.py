#!/usr/bin/env python3
"""
Fix CS-Architect tendency logic: Creative difficult → Producer pathway
Following tenet #4: One surgical change at a time
"""

def fix_cs_architect_tendency():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing CS-Architect tendency logic...")
    
    # Fix CS-Architect stuck/unstuck content
    old_cs_architect_stuck = '''stuckContent.innerHTML = 'When you combine your Translator archetypes with an Architect tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to focus your translation work is by tapping into your Inner Guide archetype, which aligns with your structured approach to meaning-making.';'''
    
    new_cs_architect_stuck = '''stuckContent.innerHTML = 'When you combine your Translator archetypes with an Architect tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to focus your translation work is by tapping into your Producer archetype, which aligns with your structured approach to getting things done.';'''
    
    # Fix CS-Architect prompts content
    old_cs_architect_prompts = '''promptsContent.innerHTML = 'What is the one key insight that most needs to be communicated? How can your Inner Guide help you access the deeper meaning behind this translation? Once your Inner Guide is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to structure clear bridges between complex concepts.';'''
    
    new_cs_architect_prompts = '''promptsContent.innerHTML = 'What is the one key insight that most needs to be communicated? How can your Producer help you structure this translation systematically? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to find innovative ways to bridge complex concepts.';'''
    
    if old_cs_architect_stuck in content:
        content = content.replace(old_cs_architect_stuck, new_cs_architect_stuck)
        print("✅ Fixed CS-Architect stuck/unstuck: Creative difficult → Producer pathway")
    else:
        print("❌ Could not find CS-Architect stuck content to fix")
    
    if old_cs_architect_prompts in content:
        content = content.replace(old_cs_architect_prompts, new_cs_architect_prompts)
        print("✅ Fixed CS-Architect prompts: Producer → Creative activation")
    else:
        print("❌ Could not find CS-Architect prompts content to fix")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ CS-Architect tendency logic corrected")

if __name__ == "__main__":
    fix_cs_architect_tendency()