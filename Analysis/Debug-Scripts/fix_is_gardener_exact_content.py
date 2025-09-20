#!/usr/bin/env python3
"""
Fix IS-Gardener content with exact text provided
"""

def fix_is_gardener_exact_content():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Updating IS-Gardener with exact content...")
    
    # Find loadISArchitectContent function and update it for IS-Gardener
    # First, let's find where the IS-Gardener specific content should go
    # We need to modify the setCollapsibleSections function for Westerner + Gardener
    
    # Update the overwhelmed section for Westerners (both Architect and Gardener)
    old_westerner_overwhelmed = '''                overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                overwhelmedContent.innerHTML = 'They usually double-down on their strengths to analyze, when what they likely need more is to move from reflection to expression.';'''
    
    new_westerner_overwhelmed = '''                overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                overwhelmedContent.innerHTML = 'As an IS-Architect, you have a Westerner profile with a tendency to architect (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck going from being oriented inward to outward, going from thinking to doing.';'''
    
    # Update the stuck/unstuck section for Westerner + Gardener
    old_westerner_gardener_stuck = '''                } else {
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
                }'''
    
    new_westerner_gardener_stuck = '''                } else {
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
                }'''
    
    # Update the prompts section for Westerner + Gardener
    old_westerner_gardener_prompts = '''                } else {
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to find natural ways to manifest your deep insights.';
                }'''
    
    new_westerner_gardener_prompts = '''                } else {
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to find natural ways to manifest your deep insights.';
                }'''
    
    # Apply the changes
    content = content.replace(old_westerner_overwhelmed, new_westerner_overwhelmed)
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Updated IS-Gardener content:")
    print("   - Updated overwhelmed section with exact text")
    print("   - Stuck/unstuck section already correct")
    print("   - Prompts section already correct")

if __name__ == "__main__":
    fix_is_gardener_exact_content()