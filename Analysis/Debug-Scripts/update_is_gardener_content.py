#!/usr/bin/env python3
"""
Update IS-Gardener collapsible sections to match IS-Architect template
"""

def update_is_gardener_content():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Updating IS-Gardener collapsible sections...")
    
    # Find the setCollapsibleSections function
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Find the end of the function
    brace_count = 0
    end = start
    for i, char in enumerate(content[start:], start):
        if char == '{':
            brace_count += 1
        elif char == '}':
            brace_count -= 1
            if brace_count == 0:
                end = i + 1
                break
    
    function_content = content[start:end]
    
    # Update the stuck/unstuck section for IS-Gardener
    old_westerner_gardener = '''            } else {
                stuckContent.innerHTML = 'As a Westerner with a Gardener tendency, you have natural flexibility in your approach but may get stuck in endless reflection. Your path to expression often flows through your Creative archetype, allowing organic emergence of ideas. Trust the process and let insights unfold naturally into creative output.';
            }'''
    
    new_westerner_gardener = '''            } else {
                stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
            }'''
    
    # Update the prompts section for IS-Gardener
    old_westerner_gardener_prompts = '''                } else {
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Trust the natural flow from inner knowing to creative expression, allowing your insights to find their own unique form of manifestation.';
                }'''
    
    new_westerner_gardener_prompts = '''                } else {
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Once your Creative is activated, you\\'ll likely find it becomes easier to drop into your Producer archetype, allowing you to find natural ways to manifest your deep insights.';
                }'''
    
    # Apply the changes
    function_content = function_content.replace(old_westerner_gardener, new_westerner_gardener)
    function_content = function_content.replace(old_westerner_gardener_prompts, new_westerner_gardener_prompts)
    
    # Replace the function in the main content
    content = content[:start] + function_content + content[end:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Updated IS-Gardener collapsible sections:")
    print("   - When Westerners feel overwhelmed: Same as IS-Architect (already correct)")
    print("   - Getting stuck and unstuck: Updated to focus on Creative→Producer pathway")
    print("   - Prompts: Updated to mention Creative→Producer activation sequence")
    print("📋 IS-Gardener now follows same template structure as IS-Architect")

if __name__ == "__main__":
    update_is_gardener_content()