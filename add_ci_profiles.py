#!/usr/bin/env python3
"""
Add CI-Architect and CI-Gardener profiles to setCollapsibleSections
Following tenet #4: One surgical change at a time
"""

def add_ci_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Adding CI-Architect and CI-Gardener profiles...")
    
    # Find the setCollapsibleSections function and locate insertion point
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Find the insertion point (after PS-Gardener logic)
    ps_gardener_end = content.find("code === 'PS-Gardener'", start)
    if ps_gardener_end != -1:
        # Find the end of PS-Gardener block
        return_point = content.find("return; // Exit early, don't use generic logic", ps_gardener_end)
        insertion_point = content.find('}', return_point) + 1
    else:
        print("❌ Could not find PS-Gardener block for insertion point")
        return
    
    # Create CI profile logic
    ci_logic = '''
            
            if (code === 'CI-Architect') {
                // Set overwhelmed content for CI-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for CI-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CI-Architect';
                    stuckContent.innerHTML = 'When you combine your Southerner archetypes with an Architect tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to ground exploration with direction is by tapping into your Producer archetype, which aligns with your structured approach to creating tangible outcomes.';
                }
                
                // Set prompts content for CI-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with direction as a CI-Architect';
                    promptsContent.innerHTML = 'Which of your creative insights are ready to become concrete outcomes? How can your Producer help you build something tangible from your explorations? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to make systematic sense of your discoveries.';
                }
                return; // Exit early, don't use generic logic
            }
            
            if (code === 'CI-Gardener') {
                // Set overwhelmed content for CI-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for CI-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CI-Gardener';
                    stuckContent.innerHTML = 'When you combine your Southerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to ground exploration with direction is by tapping into your Synthesizer archetype, which aligns with your flexible approach to making sense of discoveries.';
                }
                
                // Set prompts content for CI-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with direction as a CI-Gardener';
                    promptsContent.innerHTML = 'What patterns are emerging from your creative explorations? How can your Synthesizer help you make sense of your discoveries organically? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to manifest your insights into meaningful action.';
                }
                return; // Exit early, don't use generic logic
            }'''
    
    # Insert the CI logic
    content = content[:insertion_point] + ci_logic + content[insertion_point:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added CI-Architect and CI-Gardener profiles")
    print("📋 Content structure:")
    print("   - CI-Architect: Synthesizer difficulty → Producer pathway (structured)")
    print("   - CI-Gardener: Producer difficulty → Synthesizer pathway (flexible)")
    print("   - Both use Southerner orientation (explorers)")

if __name__ == "__main__":
    add_ci_profiles()