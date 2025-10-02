#!/usr/bin/env python3
"""
Create loadISGardenerContent function with the exact content specified
"""

def create_is_gardener_function():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Creating loadISGardenerContent function...")
    
    # Find the loadISArchitectContent function to use as a template
    start = content.find('function loadISArchitectContent() {')
    if start == -1:
        print("❌ Could not find loadISArchitectContent function")
        return
    
    # Find the end of the loadISArchitectContent function
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
    
    # Create the IS-Gardener function based on IS-Architect
    is_gardener_function = '''
        function loadISGardenerContent() {
            // Show and populate collapsible sections
            const sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection'];
            sections.forEach(sectionId => {
                const section = document.getElementById(sectionId);
                if (section) section.style.display = 'block';
            });
            
            // Set overwhelmed content
            const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
            const overwhelmedContent = document.getElementById('overwhelmedContent');
            if (overwhelmedTitle && overwhelmedContent) {
                overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                overwhelmedContent.innerHTML = 'As an IS-Architect, you have a Westerner profile with a tendency to architect (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck going from being oriented inward to outward, going from thinking to doing.';
            }
            
            // Set stuck/unstuck content
            const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
            const stuckContent = document.getElementById('stuckUnstuckContent');
            if (stuckTitle && stuckContent) {
                stuckTitle.textContent = 'Getting stuck and unstuck as an IS-Gardener';
                stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Creative archetype, which aligns with your flexible, emergent approach.';
            }
            
            // Set prompts content
            const promptsTitle = document.querySelector('#promptsSection .section-title');
            const promptsContent = document.getElementById('promptsContent');
            if (promptsTitle && promptsContent) {
                promptsTitle.textContent = 'Prompts to go from West to East as an IS-Gardener';
                promptsContent.innerHTML = 'What wants to emerge from your current reflection? How might your Creative archetype express this organically? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to find natural ways to manifest your deep insights.';
            }
        }
'''
    
    # Insert the function after loadISArchitectContent
    content = content[:end] + is_gardener_function + content[end:]
    
    # Update activateProfile to call loadISGardenerContent for IS-Gardener
    old_load_section = '''                    // Load full content based on profile
                    if (code === 'IS-Architect') {
                        loadISArchitectContent();
                    }
                    // TODO: Add other profiles here one by one'''
    
    new_load_section = '''                    // Load full content based on profile
                    if (code === 'IS-Architect') {
                        loadISArchitectContent();
                    } else if (code === 'IS-Gardener') {
                        loadISGardenerContent();
                    }
                    // TODO: Add other profiles here one by one'''
    
    content = content.replace(old_load_section, new_load_section)
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Created loadISGardenerContent function with exact content:")
    print("   - When Westerners feel overwhelmed: Exact text provided")
    print("   - Getting stuck and unstuck as an IS-Gardener: Exact text provided")
    print("   - Prompts to go from West to East as an IS-Gardener: Exact text provided")
    print("✅ Updated activateProfile to call loadISGardenerContent for IS-Gardener")

if __name__ == "__main__":
    create_is_gardener_function()