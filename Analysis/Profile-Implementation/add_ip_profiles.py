#!/usr/bin/env python3
"""
Add IP-Architect and IP-Gardener content to setCollapsibleSections function
Following tenet #4: One surgical change at a time
"""

def add_ip_profiles():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Adding IP-Architect and IP-Gardener to setCollapsibleSections function...")
    
    # Find the setCollapsibleSections function and the IS-Gardener logic
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Find where to insert IP logic (after IS-Gardener logic)
    is_gardener_end = content.find("return; // Exit early, don't use generic logic", start)
    if is_gardener_end == -1:
        print("❌ Could not find IS-Gardener logic end")
        return
    
    # Find the insertion point (after the closing brace and before the generic logic)
    insertion_point = content.find('}', is_gardener_end) + 1
    
    # Create IP profile logic based on IS profiles
    ip_logic = '''
            
            if (code === 'IP-Architect') {
                // Set overwhelmed content for IP-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can oscillate between deep reflection and intense action, when what they need is to find a sustainable rhythm that honors both their inner wisdom and their drive to create tangible outcomes.';
                }
                
                // Set stuck/unstuck content for IP-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IP-Architect';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with an Architect tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from meaning to execution is by tapping into your Synthesizer archetype, which aligns with your structured approach to understanding.';
                }
                
                // Set prompts content for IP-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to sustain your conversion rhythm as an IP-Architect';
                    promptsContent.innerHTML = 'How can you create systematic pathways from insight to action? What would a sustainable process look like for converting your deep understanding into concrete outcomes? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to find innovative ways to bridge meaning and execution.';
                }
                return; // Exit early, don't use generic logic
            }
            
            if (code === 'IP-Gardener') {
                // Set overwhelmed content for IP-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can oscillate between deep reflection and intense action, when what they need is to find a sustainable rhythm that honors both their inner wisdom and their drive to create tangible outcomes.';
                }
                
                // Set stuck/unstuck content for IP-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IP-Gardener';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with a Gardener tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from meaning to execution is by tapping into your Synthesizer archetype, which aligns with your flexible approach to making sense of insights.';
                }
                
                // Set prompts content for IP-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to sustain your conversion rhythm as an IP-Gardener';
                    promptsContent.innerHTML = 'What rhythm naturally emerges between your inner knowing and outer creating? How can your Synthesizer help you recognize when to reflect and when to act? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to find organic ways to manifest your understanding.';
                }
                return; // Exit early, don't use generic logic
            }'''
    
    # Insert the IP logic
    content = content[:insertion_point] + ip_logic + content[insertion_point:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added IP-Architect and IP-Gardener specific content")
    print("📋 Content structure:")
    print("   - IP-Architect: Creative archetype difficulty, Synthesizer pathway (structured)")
    print("   - IP-Gardener: Creative archetype difficulty, Synthesizer pathway (flexible)")
    print("   - Both use Converter orientation (diagonal IP pattern)")

if __name__ == "__main__":
    add_ip_profiles()