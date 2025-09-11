#!/usr/bin/env python3
"""
Add PS-Architect and PS-Gardener profiles to setCollapsibleSections
Following tenet #4: One surgical change at a time
"""

def add_ps_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Adding PS-Architect and PS-Gardener profiles...")
    
    # Find the setCollapsibleSections function and locate insertion point
    start = content.find('function setCollapsibleSections(code) {')
    if start == -1:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Find the insertion point (after CS-Gardener logic)
    cs_gardener_end = content.find("code === 'CS-Gardener'", start)
    if cs_gardener_end != -1:
        # Find the end of CS-Gardener block
        return_point = content.find("return; // Exit early, don't use generic logic", cs_gardener_end)
        insertion_point = content.find('}', return_point) + 1
    else:
        print("❌ Could not find CS-Gardener block for insertion point")
        return
    
    # Create PS profile logic
    ps_logic = '''
            
            if (code === 'PS-Architect') {
                // Set overwhelmed content for PS-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for PS-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PS-Architect';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with an Architect tendency, it\\'s most difficult to access your Creative archetype—yet that\\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance building with breakthrough is by tapping into your Inner Guide archetype, which aligns with your structured approach to meaning-making.';
                }
                
                // Set prompts content for PS-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with breakthrough as a PS-Architect';
                    promptsContent.innerHTML = 'What would happen if you approached this systematically but with creative flair? How can your Inner Guide help you access deeper meaning in your structured process? Once your Inner Guide is activated, you\\'ll likely find it becomes easier to move into your Creative archetype, allowing you to inject innovation into your methodical approach.';
                }
                return; // Exit early, don't use generic logic
            }
            
            if (code === 'PS-Gardener') {
                // Set overwhelmed content for PS-Gardener
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {
                    overwhelmedTitle.textContent = 'When Northerners feel overwhelmed…';
                    overwhelmedContent.innerHTML = 'They may get caught in endless planning and structuring, when what they need is to trust their process and move forward with decisive action, even if everything isn\\'t perfectly planned.';
                }
                
                // Set stuck/unstuck content for PS-Gardener
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {
                    stuckTitle.textContent = 'Getting stuck and unstuck as a PS-Gardener';
                    stuckContent.innerHTML = 'When you combine your Northerner archetypes with a Gardener tendency, it\\'s most difficult to access your Inner Guide archetype—yet that\\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance building with breakthrough is by tapping into your Creative archetype, which aligns with your flexible approach to innovation.';
                }
                
                // Set prompts content for PS-Gardener
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {
                    promptsTitle.textContent = 'Prompts to balance building with breakthrough as a PS-Gardener';
                    promptsContent.innerHTML = 'When does your systematic approach serve you, and when might exploration be more valuable? How can your Creative help you find innovative approaches to building? Once your Creative is activated, you\\'ll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the deeper meaning behind your systematic work.';
                }
                return; // Exit early, don't use generic logic
            }'''
    
    # Insert the PS logic
    content = content[:insertion_point] + ps_logic + content[insertion_point:]
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added PS-Architect and PS-Gardener profiles")
    print("📋 Content structure:")
    print("   - PS-Architect: Creative difficulty → Inner Guide pathway (structured)")
    print("   - PS-Gardener: Inner Guide difficulty → Creative pathway (flexible)")
    print("   - Both use Northerner orientation (builders)")

if __name__ == "__main__":
    add_ps_profiles()