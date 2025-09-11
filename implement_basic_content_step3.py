#!/usr/bin/env python3
"""
Implement basic content (archetype descriptions and collapsible sections) for all 24 profiles
"""

def implement_basic_content_for_all_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    # Find where to insert the functions (after setTendencyPills function)
    insert_point = content.find('        function loadISArchitectContent() {')
    
    # Create archetype description function
    archetype_function = '''
        function setArchetypeDescription(code) {
            const [archetypes, tendency] = code.split('-');
            const primary = archetypes[0];
            const secondary = archetypes[1];
            
            const archetypeNames = {
                'I': 'Inner Guide',
                'S': 'Synthesizer', 
                'P': 'Producer',
                'C': 'Creative'
            };
            
            const archetypeDesc = document.getElementById('archetypeDescription');
            if (archetypeDesc) {
                const primaryName = archetypeNames[primary];
                const secondaryName = archetypeNames[secondary];
                archetypeDesc.innerHTML = `The <strong>${primaryName}</strong> is your dominant sensemaking archetype, followed by the <strong>${secondaryName}</strong>. This combination shapes how you naturally approach understanding and creating meaning from the world around you.`;
            }
        }

        function setCollapsibleSections(code) {
            const [archetypes, tendency] = code.split('-');
            
            // Show collapsible sections for all profiles
            const sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection'];
            sections.forEach(sectionId => {
                const section = document.getElementById(sectionId);
                if (section) section.style.display = 'block';
            });
            
            // Set overwhelmed content
            const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
            const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
            if (overwhelmedTitle && overwhelmedContent) {
                overwhelmedTitle.textContent = `When ${code}s Feel Overwhelmed`;
                overwhelmedContent.innerHTML = `<p>As an <strong>${code}</strong>, when you feel overwhelmed, try stepping back and focusing on your core strengths. Take time to process information in your preferred way before making decisions.</p>`;
            }
            
            // Set stuck/unstuck content  
            const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
            const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
            if (stuckTitle && stuckContent) {
                stuckTitle.textContent = `When ${code}s Get Stuck (and Unstuck)`;
                stuckContent.innerHTML = `<p>When you're stuck, remember that your <strong>${code}</strong> profile has unique ways of processing information. Try changing your environment or approach to align with your natural sensemaking patterns.</p>`;
            }
            
            // Set prompts content
            const promptsTitle = document.querySelector('#promptsSection .section-title');
            const promptsContent = document.querySelector('#promptsSection .section-content');
            if (promptsTitle && promptsContent) {
                promptsTitle.textContent = `Prompts for ${code}s`;
                promptsContent.innerHTML = `<p>Questions and prompts specifically designed for <strong>${code}</strong> profiles to help you leverage your unique sensemaking approach.</p>`;
            }
        }
'''
    
    # Insert the functions
    content = content[:insert_point] + archetype_function + content[insert_point:]
    
    # Add the function calls to activateProfile (after setTendencyPills call)
    old_call_section = '''                    // Set tendency pills and descriptions for all profiles
                    setTendencyPills(code);
                    
                    // Load full content based on profile'''
    
    new_call_section = '''                    // Set tendency pills and descriptions for all profiles
                    setTendencyPills(code);
                    
                    // Set archetype description for all profiles
                    setArchetypeDescription(code);
                    
                    // Set collapsible sections content for all profiles
                    setCollapsibleSections(code);
                    
                    // Load full content based on profile'''
    
    content = content.replace(old_call_section, new_call_section)
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added setArchetypeDescription() function for all 24 profiles")
    print("✅ Added setCollapsibleSections() function for all 24 profiles") 
    print("✅ Added function calls to activateProfile()")
    print("📋 Basic content implementation covers:")
    print("   - Dynamic archetype descriptions")
    print("   - Collapsible sections (overwhelmed, stuck/unstuck, prompts)")
    print("   - Profile-specific section titles and content")

if __name__ == "__main__":
    implement_basic_content_for_all_profiles()