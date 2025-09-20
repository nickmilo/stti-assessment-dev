#!/usr/bin/env python3
"""
Smart way: Add IS-Gardener specific logic to existing setCollapsibleSections function
"""

def fix_is_gardener_smart_way():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Adding IS-Gardener specific logic to setCollapsibleSections function...")
    
    # Find the setCollapsibleSections function
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Add specific logic for IS-Gardener at the beginning of the function
    insertion_point = content.find('// Set overwhelmed content', start)
    if insertion_point == -1:
        print("❌ Could not find insertion point")
        return
    
    is_gardener_logic = '''
            // Handle specific profile codes first
            if (code === 'IS-Gardener') {
                // Set overwhelmed content for IS-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'As an IS-Architect, you have a Westerner profile with a tendency to architect (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck going from being oriented inward to outward, going from thinking to doing.';
                }
                
                // Set stuck/unstuck content for IS-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IS-Gardener';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
                }
                
                // Set prompts content for IS-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from West to East as an IS-Gardener';
                    promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to find natural ways to manifest your deep insights.';
                }
                return; // Exit early, don't use generic logic
            }
            
            '''
    
    # Insert the IS-Gardener logic
    content = content[:insertion_point] + is_gardener_logic + content[insertion_point:]
    
    # Remove the separate loadISGardenerContent function I created earlier
    start_func = content.find('function loadISGardenerContent() {')
    if start_func != -1:
        brace_count = 0
        end_func = start_func
        for i, char in enumerate(content[start_func:], start_func):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_func = i + 1
                    break
        
        # Remove the function and the newlines around it
        content = content[:start_func-1] + content[end_func+1:]
        print("✅ Removed the unnecessary loadISGardenerContent function")
    
    # Remove the IS-Gardener call from activateProfile
    old_call = '''                    } else if (code === 'IS-Gardener') {
                        loadISGardenerContent();
                    }'''
    content = content.replace(old_call, '')
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added IS-Gardener specific logic to setCollapsibleSections")
    print("✅ Removed unnecessary separate function")
    print("✅ This approach scales for all 24 profiles without bloating the file")

if __name__ == "__main__":
    fix_is_gardener_smart_way()