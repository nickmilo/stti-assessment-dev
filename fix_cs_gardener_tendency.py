#!/usr/bin/env python3
"""
Fix CS-Gardener tendency logic: Producer difficult → Creative pathway
Following tenet #4: One surgical change at a time
"""

def fix_cs_gardener_tendency():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing CS-Gardener tendency logic...")
    
    # Fix CS-Gardener stuck/unstuck content
    old_cs_gardener_stuck = '''stuckContent.innerHTML = 'When you combine your Translator archetypes with a Gardener tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to focus your translation work is by tapping into your Synthesizer archetype, which aligns with your flexible approach to connecting ideas.';'''
    
    new_cs_gardener_stuck = '''stuckContent.innerHTML = 'When you combine your Translator archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to focus your translation work is by tapping into your Creative archetype, which aligns with your flexible approach to innovation.';'''
    
    # Fix CS-Gardener prompts content
    old_cs_gardener_prompts = '''promptsContent.innerHTML = 'Which perspectives are asking to be bridged right now? How can your Synthesizer help you make organic connections between ideas? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the deeper meaning that wants to be communicated.';'''
    
    new_cs_gardener_prompts = '''promptsContent.innerHTML = 'Which perspectives are asking to be bridged right now? How can your Creative help you find innovative ways to connect ideas? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to manifest your translations into concrete outcomes.';'''
    
    if old_cs_gardener_stuck in content:
        content = content.replace(old_cs_gardener_stuck, new_cs_gardener_stuck)
        print("✅ Fixed CS-Gardener stuck/unstuck: Producer difficult → Creative pathway")
    else:
        print("❌ Could not find CS-Gardener stuck content to fix")
    
    if old_cs_gardener_prompts in content:
        content = content.replace(old_cs_gardener_prompts, new_cs_gardener_prompts)
        print("✅ Fixed CS-Gardener prompts: Creative → Producer activation")
    else:
        print("❌ Could not find CS-Gardener prompts content to fix")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ CS-Gardener tendency logic corrected")

if __name__ == "__main__":
    fix_cs_gardener_tendency()