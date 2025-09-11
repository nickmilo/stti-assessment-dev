#!/usr/bin/env python3
"""
Implement remaining profile batches efficiently
Following SOP Tenet #4: One batch at a time with validation
"""

def implement_sc_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== IMPLEMENTING SC PROFILES ===")
    print("SC = Synthesizer + Creative = Diagonal/Translator")
    
    insertion_point = content.find('return; // Exit early, don\'t use generic logic\n            }\n            \n            // Set overwhelmed content')
    
    sc_implementation = '''
            if (code === 'SC-Architect') {
                // Set overwhelmed content for SC-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for SC-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SC-Architect';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with an Architect tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to bridge perspectives with meaning is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for SC-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to bridge perspectives with meaning as an SC-Architect';
                    promptsContent.innerHTML = 'What deeper meaning connects the perspectives you\\'re translating? How can your Synthesizer help you structure these connections systematically? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the intrinsic meaning behind your translations.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            
            if (code === 'SC-Gardener') {
                // Set overwhelmed content for SC-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Translators feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.';
                }
                
                // Set stuck/unstuck content for SC-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SC-Gardener';
                    stuckContent.innerHTML = 'When you combine your Translator archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to bridge perspectives with action is by tapping into your Creative archetype, which aligns with your flexible approach to innovative expression.';
                }
                
                // Set prompts content for SC-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to bridge perspectives with action as an SC-Gardener';
                    promptsContent.innerHTML = 'What creative expressions could emerge from the perspectives you\\'re bridging? How can your Creative help you manifest your translations in innovative ways? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to take systematic action on your synthesized insights.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            '''
    
    if insertion_point != -1:
        new_content = content[:insertion_point] + sc_implementation + content[insertion_point:]
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
            f.write(new_content)
        print("✅ SC profiles added")
        return True
    else:
        print("❌ Could not find insertion point")
        return False

def implement_sp_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("\n=== IMPLEMENTING SP PROFILES ===")
    print("SP = Synthesizer + Producer = Northerner/Builder")
    
    insertion_point = content.find('return; // Exit early, don\'t use generic logic\n            }\n            \n            // Set overwhelmed content')
    
    sp_implementation = '''
            if (code === 'SP-Architect') {
                // Set overwhelmed content for SP-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for SP-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SP-Architect';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with an Architect tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance building with innovation is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for SP-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with innovation as an SP-Architect';
                    promptsContent.innerHTML = 'How can you systematically analyze what you\\'re building for creative opportunities? What patterns in your work suggest new innovative directions? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to inject fresh innovation into your systematic building process.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            
            if (code === 'SP-Gardener') {
                // Set overwhelmed content for SP-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for SP-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SP-Gardener';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with a Gardener tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance building with meaning is by tapping into your Producer archetype, which aligns with your flexible approach to systematic action.';
                }
                
                // Set prompts content for SP-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with meaning as an SP-Gardener';
                    promptsContent.innerHTML = 'What meaningful action could emerge organically from your building process? How can your Producer help you manifest progress in ways that feel naturally flowing? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access deeper meaning in your systematic work.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            '''
    
    if insertion_point != -1:
        new_content = content[:insertion_point] + sp_implementation + content[insertion_point:]
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
            f.write(new_content)
        print("✅ SP profiles added")
        return True
    else:
        print("❌ Could not find insertion point")
        return False

def implement_si_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("\n=== IMPLEMENTING SI PROFILES ===")
    print("SI = Synthesizer + Inner Guide = Westerner/Philosopher")
    
    insertion_point = content.find('return; // Exit early, don\'t use generic logic\n            }\n            \n            // Set overwhelmed content')
    
    si_implementation = '''
            if (code === 'SI-Architect') {
                // Set overwhelmed content for SI-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to double-down on reflection and analysis, when what they actually need is to move into expression and action, allowing their insights to manifest in the world.';
                }
                
                // Set stuck/unstuck content for SI-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SI-Architect';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with an Architect tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from understanding to expression is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.';
                }
                
                // Set prompts content for SI-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to move from understanding to expression as an SI-Architect';
                    promptsContent.innerHTML = 'How can you structure your insights for systematic creative expression? What frameworks would help you manifest your understanding in innovative ways? Once your Synthesizer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to express your deep understanding through original contributions.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            
            if (code === 'SI-Gardener') {
                // Set overwhelmed content for SI-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Westerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They tend to double-down on reflection and analysis, when what they actually need is to move into expression and action, allowing their insights to manifest in the world.';
                }
                
                // Set stuck/unstuck content for SI-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as an SI-Gardener';
                    stuckContent.innerHTML = 'When you combine your Westerner archetypes with a Gardener tendency, it\\'s most difficult to access your Producer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from understanding to action is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.';
                }
                
                // Set prompts content for SI-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to move from understanding to action as an SI-Gardener';
                    promptsContent.innerHTML = 'What meaningful action could emerge organically from your understanding? How can your Inner Guide help you sense what wants to be manifested? Once your Inner Guide is activated, you\\'ll likely find it becomes easier to move into your Producer archetype, allowing you to take systematic action on your deepest insights.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            '''
    
    if insertion_point != -1:
        new_content = content[:insertion_point] + si_implementation + content[insertion_point:]
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
            f.write(new_content)
        print("✅ SI profiles added")
        return True
    else:
        print("❌ Could not find insertion point")
        return False

def implement_pi_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("\n=== IMPLEMENTING PI PROFILES ===")
    print("PI = Producer + Inner Guide = Diagonal/Converter")
    
    insertion_point = content.find('return; // Exit early, don\'t use generic logic\n            }\n            \n            // Set overwhelmed content')
    
    pi_implementation = '''
            if (code === 'PI-Architect') {
                // Set overwhelmed content for PI-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may oscillate too rapidly between reflection and action, when what they need is to find a sustainable rhythm that honors both their need for meaning and their drive to make progress.';
                }
                
                // Set stuck/unstuck content for PI-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PI-Architect';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with an Architect tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance meaning with execution is by tapping into your Producer archetype, which aligns with your structured approach to systematic action.';
                }
                
                // Set prompts content for PI-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance meaning with execution as a PI-Architect';
                    promptsContent.innerHTML = 'How can you systematically structure your meaningful work for consistent progress? What processes would help you maintain momentum while honoring depth? Once your Producer is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to innovate within your systematic approach to meaningful action.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            
            if (code === 'PI-Gardener') {
                // Set overwhelmed content for PI-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Converters feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may oscillate too rapidly between reflection and action, when what they need is to find a sustainable rhythm that honors both their need for meaning and their drive to make progress.';
                }
                
                // Set stuck/unstuck content for PI-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PI-Gardener';
                    stuckContent.innerHTML = 'When you combine your Converter archetypes with a Gardener tendency, it\\'s most difficult to access your Synthesizer archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance meaning with execution is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.';
                }
                
                // Set prompts content for PI-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance meaning with execution as a PI-Gardener';
                    promptsContent.innerHTML = 'What natural rhythm emerges between meaningful reflection and purposeful action? How can your Inner Guide help you sense when to move between meaning and execution? Once your Inner Guide is activated, you\\'ll likely find it becomes easier to move into your Synthesizer archetype, allowing you to weave understanding into your action-oriented approach.';
                }
                return; // Exit early, don\\'t use generic logic
            }
            '''
    
    if insertion_point != -1:
        new_content = content[:insertion_point] + pi_implementation + content[insertion_point:]
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
            f.write(new_content)
        print("✅ PI profiles added")
        return True
    else:
        print("❌ Could not find insertion point")
        return False

if __name__ == "__main__":
    # Implement all remaining batches
    success = True
    success &= implement_sc_profiles()
    success &= implement_sp_profiles() 
    success &= implement_si_profiles()
    success &= implement_pi_profiles()
    
    if success:
        print("\n🎉 ALL REMAINING PROFILES IMPLEMENTED")
    else:
        print("\n❌ Some implementations failed")