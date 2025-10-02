#!/usr/bin/env python3
"""
Implement tendency pills and descriptions for all 24 profiles (Step 3 continuation)
"""

def implement_tendency_for_all_profiles():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    # Find where to insert the setTendencyPills function (after setOrientation function)
    set_orientation_end = content.find('        }\n        \n        function loadISArchitectContent() {')
    if set_orientation_end == -1:
        set_orientation_end = content.find('        function loadISArchitectContent() {')
    
    # Create the setTendencyPills function
    tendency_function = '''
        function setTendencyPills(code) {
            const [archetypes, tendency] = code.split('-');
            
            // Set primary tendency pill
            const tendencyPill = document.getElementById('tendencyPill');
            if (tendencyPill) {
                tendencyPill.textContent = tendency;
                tendencyPill.className = `tendency-pill ${tendency.toLowerCase()}-pill`;
            }
            
            // Set secondary tendency pill (opposite of primary)
            const secondaryTendencyPill = document.getElementById('secondaryTendencyPill');
            if (secondaryTendencyPill) {
                const secondaryTendency = tendency === 'Architect' ? 'Gardener' : 'Architect';
                secondaryTendencyPill.textContent = secondaryTendency;
                secondaryTendencyPill.className = `tendency-pill secondary-tendency ${secondaryTendency.toLowerCase()}-pill`;
            }
            
            // Set tendency description
            const tendencyDesc = document.getElementById('tendencyDescription');
            if (tendencyDesc) {
                if (tendency === 'Architect') {
                    tendencyDesc.innerHTML = 'The <strong>Architect</strong> is your dominant sensemaking tendency. This means you gravitate towards structuring and organizing the things around you. However, it doesn\\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.';
                } else {
                    tendencyDesc.innerHTML = 'The <strong>Gardener</strong> is your dominant sensemaking tendency. This means you gravitate towards nurturing and cultivating the things around you. You prefer organic growth and emergence over rigid structure, allowing ideas and projects to develop naturally while providing gentle guidance.';
                }
            }
        }
'''
    
    # Insert the function
    content = content[:set_orientation_end] + tendency_function + content[set_orientation_end:]
    
    # Add the function call to activateProfile (after setOrientation call)
    old_call_section = '''                    // Set orientation for all profiles
                    setOrientation(code);
                    
                    // Load full content based on profile'''
    
    new_call_section = '''                    // Set orientation for all profiles
                    setOrientation(code);
                    
                    // Set tendency pills and descriptions for all profiles
                    setTendencyPills(code);
                    
                    // Load full content based on profile'''
    
    content = content.replace(old_call_section, new_call_section)
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Added setTendencyPills() function for all 24 profiles")
    print("✅ Added setTendencyPills(code) call to activateProfile()")
    print("📋 Tendency implementation covers:")
    print("   - Primary tendency pill (Architect/Gardener)")
    print("   - Secondary tendency pill (opposite)")
    print("   - Tendency descriptions for both types")

if __name__ == "__main__":
    implement_tendency_for_all_profiles()