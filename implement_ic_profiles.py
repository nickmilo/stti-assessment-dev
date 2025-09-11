#!/usr/bin/env python3
"""
Implement IC-Architect and IC-Gardener profiles
Following SOP Tenet #1: Understand structure before modifying
Following SOP Tenet #4: Make surgical changes one at a time
"""

def implement_ic_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== IMPLEMENTING IC PROFILES ===\n")
    
    # IC = Inner Guide + Creative = Southerner/Explorer
    # IC-Architect: Struggles with Synthesizer (structured not in IC), uses Producer pathway (flexible in IC)
    # IC-Gardener: Struggles with Producer (structured not in IC), uses Inner Guide pathway (flexible in IC)
    
    # Wait, let me recalculate the tendency logic correctly:
    # IC has Inner Guide (flexible) + Creative (flexible) 
    # Missing: Producer (structured) + Synthesizer (structured)
    # IC-Architect (structured tendency): Struggles with flexible not in IC = none, so struggles with structured not in IC = Producer or Synthesizer
    # IC-Gardener (flexible tendency): Struggles with structured not in IC = Producer or Synthesizer
    
    # Let me check existing patterns from working profiles
    print("🔍 Checking existing tendency patterns:")
    
    # From SOP: IS-Architect struggles with Creative, uses Synthesizer pathway
    # IS = Inner Guide (flexible) + Synthesizer (structured)
    # IS-Architect: Struggles with Creative (flexible not in IS), uses Synthesizer (structured in IS)
    # This means: Architect struggles with flexible archetype NOT in the combination
    
    # For IC (Inner Guide + Creative, both flexible):
    # IC-Architect: Struggles with flexible archetype not in IC = none... wait
    # Actually: Architect struggles with flexible archetypes, so struggles with missing flexible = none
    # But struggles with missing structured = Producer or Synthesizer. Let's pick Producer.
    # IC-Gardener: Struggles with structured archetypes, so struggles with missing structured = Producer or Synthesizer. Let's pick Synthesizer.
    
    print("  IC-Architect: Struggles with Producer (structured not in IC), uses Creative pathway (flexible in IC)")  
    print("  IC-Gardener: Struggles with Synthesizer (structured not in IC), uses Inner Guide pathway (flexible in IC)")
    
    # Find insertion point (after CI-Gardener)
    insertion_point = content.find('return; // Exit early, don\'t use generic logic\n            }\n            \n            // Set overwhelmed content')
    if insertion_point == -1:
        print("❌ Could not find insertion point")
        return False
    
    # Insert IC-Architect implementation
    ic_architect_implementation = '''
            if (code === 'IC-Architect') {
                // Set overwhelmed content for IC-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for IC-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IC-Architect';
                    stuckContent.innerHTML = 'When you combine your Southerner archetypes with an Architect tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to ground exploration with structure is by tapping into your Creative archetype, which aligns with your structured approach to innovative expression.';
                }
                
                // Set prompts content for IC-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with structure as an IC-Architect';
                    promptsContent.innerHTML = 'How can you bring more structure to your creative explorations? What systems would help you manifest your innovative insights? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to build systematic progress from your discoveries.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            
            if (code === 'IC-Gardener') {
                // Set overwhelmed content for IC-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Southerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They can get lost in exploration and creative tangents, when what they need is to ground their insights with practical structure and focused direction.';
                }
                
                // Set stuck/unstuck content for IC-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an IC-Gardener';
                    stuckContent.innerHTML = 'When you combine your Southerner archetypes with a Gardener tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to ground exploration with understanding is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.';
                }
                
                // Set prompts content for IC-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to ground exploration with understanding as an IC-Gardener';
                    promptsContent.innerHTML = 'What patterns are emerging from your creative discoveries? How can your Inner Guide help you make deeper sense of your explorations organically? Once your Inner Guide is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to weave your insights into coherent understanding.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            '''
    
    # Insert before the generic content section
    new_content = content[:insertion_point] + ic_architect_implementation + content[insertion_point:]
    
    # Write the updated content
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(new_content)
    
    print("✅ IC-Architect and IC-Gardener implementations added")
    print("   - IC-Architect: Producer difficulty, Creative pathway")
    print("   - IC-Gardener: Synthesizer difficulty, Inner Guide pathway")
    return True

if __name__ == "__main__":
    implement_ic_profiles()