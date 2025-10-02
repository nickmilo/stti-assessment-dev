#!/usr/bin/env python3
"""
Add CP-Architect and CP-Gardener profiles to setCollapsibleSections
Following tenet #4: One surgical change at a time
"""

def add_cp_profiles():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Adding CP-Architect and CP-Gardener profiles...")
    
    # Find the setCollapsibleSections function and locate insertion point
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Find the insertion point (after IP-Gardener logic)
    ip_gardener_end = content.find("code === 'IP-Gardener'", start)
    if ip_gardener_end != -1:
        # Find the end of IP-Gardener block
        return_point = content.find("return; // Exit early, don't use generic logic", ip_gardener_end)
        insertion_point = content.find('}', return_point) + 1
    else:
        print("❌ Could not find IP-Gardener block for insertion point")
        return
    
    # Create CP profile logic
    cp_logic = '''
            
            if (code === 'CP-Architect') {
                // Set overwhelmed content for CP-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for CP-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CP-Architect';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with an Architect tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from expression to reflection is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for CP-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from East to West as a CP-Architect';
                    promptsContent.innerHTML = 'What patterns are emerging from your creative output? How can your Synthesizer help you step back and make sense of what you\\'ve created? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to create more systematically structured outcomes.';
                }
                return; // Exit early, don't use generic logic
            }
            
            if (code === 'CP-Gardener') {
                // Set overwhelmed content for CP-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for CP-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CP-Gardener';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with a Gardener tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from expression to reflection is by tapping into your Producer archetype, which aligns with your flexible approach to getting things done.';
                }
                
                // Set prompts content for CP-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to go from East to West as a CP-Gardener';
                    promptsContent.innerHTML = 'What deeper meaning is your creative work pointing toward? How can your Producer help you organize your creative insights organically? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to express insights in more meaningful ways.';
                }
                return; // Exit early, don't use generic logic
            }'''
    
    # Insert the CP logic
    content = content[:insertion_point] + cp_logic + content[insertion_point:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added CP-Architect and CP-Gardener profiles")
    print("📋 Content structure:")
    print("   - CP-Architect: Producer difficulty → Synthesizer pathway (structured)")
    print("   - CP-Gardener: Creative difficulty → Producer pathway (flexible)")
    print("   - Both use Easterner orientation (makers)")

if __name__ == "__main__":
    add_cp_profiles()