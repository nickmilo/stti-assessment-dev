#!/usr/bin/env python3
"""
Fix IP-Gardener stuck/unstuck content based on tendency clarification
Following tenet #4: One surgical change at a time
"""

def fix_ip_gardener_tendency():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing IP-Gardener stuck/unstuck content based on tendency...")
    
    # Find and fix the IP-Gardener stuck content
    old_ip_gardener_stuck = '''stuckContent.innerHTML = 'When you combine your Converter archetypes with a Gardener tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from meaning to execution is by tapping into your Synthesizer archetype, which aligns with your flexible approach to making sense of insights.';'''
    
    new_ip_gardener_stuck = '''stuckContent.innerHTML = 'When you combine your Converter archetypes with a Gardener tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from meaning to execution is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';'''
    
    # Find and fix the IP-Gardener prompts content
    old_ip_gardener_prompts = '''promptsContent.innerHTML = 'What rhythm naturally emerges between your inner knowing and outer creating? How can your Synthesizer help you recognize when to reflect and when to act? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to find organic ways to manifest your understanding.';'''
    
    new_ip_gardener_prompts = '''promptsContent.innerHTML = 'What rhythm naturally emerges between your inner knowing and outer creating? How can your Creative help you express insights organically? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to make sense of your creative expressions.';'''
    
    if old_ip_gardener_stuck in content:
        content = content.replace(old_ip_gardener_stuck, new_ip_gardener_stuck)
        print("✅ Fixed IP-Gardener stuck/unstuck content: Creative→Synthesizer pathway")
    else:
        print("❌ Could not find IP-Gardener stuck content to fix")
    
    if old_ip_gardener_prompts in content:
        content = content.replace(old_ip_gardener_prompts, new_ip_gardener_prompts)
        print("✅ Fixed IP-Gardener prompts content: Creative→Synthesizer pathway")
    else:
        print("❌ Could not find IP-Gardener prompts content to fix")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("\n📋 Corrected logic:")
    print("   IP-Architect (architect tendency): Creative most difficult → Synthesizer pathway")
    print("   IP-Gardener (gardener tendency): Synthesizer most difficult → Creative pathway")

if __name__ == "__main__":
    fix_ip_gardener_tendency()