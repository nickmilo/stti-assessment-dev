#!/usr/bin/env python3
"""
Add CS-Architect and CS-Gardener profiles to setCollapsibleSections
Following tenet #4: One surgical change at a time
"""

def add_cs_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Adding CS-Architect and CS-Gardener profiles...")
    
    # Find the setCollapsibleSections function and locate insertion point
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Find the insertion point (after CP-Gardener logic)
    cp_gardener_end = content.find("code === 'CP-Gardener'", start)
    if cp_gardener_end != -1:
        # Find the end of CP-Gardener block
        return_point = content.find("return; // Exit early, don't use generic logic", cp_gardener_end)
        insertion_point = content.find('}', return_point) + 1
    else:
        print("❌ Could not find CP-Gardener block for insertion point")
        return
    
    # Create CS profile logic
    cs_logic = '''
            
            if (code === 'CS-Architect') {
                // Set overwhelmed content for CS-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for CS-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CS-Architect';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with an Architect tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to focus your translation work is by tapping into your Inner Guide archetype, which aligns with your structured approach to meaning-making.';
                }
                
                // Set prompts content for CS-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to focus your translation work as a CS-Architect';
                    promptsContent.innerHTML = 'What is the one key insight that most needs to be communicated? How can your Inner Guide help you access the deeper meaning behind this translation? Once your Inner Guide is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to structure clear bridges between complex concepts.';
                }
                return; // Exit early, don't use generic logic
            }
            
            if (code === 'CS-Gardener') {
                // Set overwhelmed content for CS-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for CS-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a CS-Gardener';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with a Gardener tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to focus your translation work is by tapping into your Synthesizer archetype, which aligns with your flexible approach to connecting ideas.';
                }
                
                // Set prompts content for CS-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to focus your translation work as a CS-Gardener';
                    promptsContent.innerHTML = 'Which perspectives are asking to be bridged right now? How can your Synthesizer help you make organic connections between ideas? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the deeper meaning that wants to be communicated.';
                }
                return; // Exit early, don't use generic logic
            }'''
    
    # Insert the CS logic
    content = content[:insertion_point] + cs_logic + content[insertion_point:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added CS-Architect and CS-Gardener profiles")
    print("📋 Content structure:")
    print("   - CS-Architect: Synthesizer difficulty → Inner Guide pathway (structured)")
    print("   - CS-Gardener: Inner Guide difficulty → Synthesizer pathway (flexible)")
    print("   - Both use Diagonal Translator orientation")

if __name__ == "__main__":
    add_cs_profiles()