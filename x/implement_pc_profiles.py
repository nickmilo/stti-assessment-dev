#!/usr/bin/env python3
"""
Implement PC-Architect and PC-Gardener profiles
Following SOP Tenet #4: One surgical change at a time
"""

def implement_pc_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== IMPLEMENTING PC PROFILES ===\n")
    
    # PC = Producer + Creative = Easterner/Maker
    # PC-Architect: Struggles with Inner Guide (flexible not in PC), uses Producer pathway (structured in PC)  
    # PC-Gardener: Struggles with Synthesizer (structured not in PC), uses Creative pathway (flexible in PC)
    
    print("🔍 PC tendency patterns:")
    print("  PC-Architect: Struggles with Inner Guide (flexible not in PC), uses Producer pathway (structured in PC)")  
    print("  PC-Gardener: Struggles with Synthesizer (structured not in PC), uses Creative pathway (flexible in PC)")
    
    # Find insertion point (after IC-Gardener)
    insertion_point = content.find('return; // Exit early, don\'t use generic logic\n            }\n            \n            // Set overwhelmed content')
    if insertion_point == -1:
        print("❌ Could not find insertion point")
        return False
    
    # Insert PC implementations
    pc_implementation = '''
            if (code === 'PC-Architect') {
                // Set overwhelmed content for PC-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for PC-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PC-Architect';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with an Architect tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance making with meaning is by tapping into your Producer archetype, which aligns with your structured approach to systematic action.';
                }
                
                // Set prompts content for PC-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance making with meaning as a PC-Architect';
                    promptsContent.innerHTML = 'How can you bring more systematic structure to your creative work? What processes would help you manifest your innovations more effectively? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access deeper meaning in your systematic creations.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            
            if (code === 'PC-Gardener') {
                // Set overwhelmed content for PC-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Easterners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to increase their activity and output, when what they actually need is to step back, slow down, and engage in deeper reflection and analysis.';
                }
                
                // Set stuck/unstuck content for PC-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PC-Gardener';
                    stuckContent.innerHTML = 'When you combine your Easterner archetypes with a Gardener tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance making with understanding is by tapping into your Creative archetype, which aligns with your flexible approach to innovative expression.';
                }
                
                // Set prompts content for PC-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance making with understanding as a PC-Gardener';
                    promptsContent.innerHTML = 'What new insights are emerging from your creative work? How can your Creative help you discover unexpected connections in your making process? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to weave deeper understanding into your innovative outputs.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            '''
    
    # Insert before the generic content section
    new_content = content[:insertion_point] + pc_implementation + content[insertion_point:]
    
    # Write the updated content
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(new_content)
    
    print("✅ PC-Architect and PC-Gardener implementations added")
    print("   - PC-Architect: Inner Guide difficulty, Producer pathway")
    print("   - PC-Gardener: Synthesizer difficulty, Creative pathway")
    return True

if __name__ == "__main__":
    implement_pc_profiles()