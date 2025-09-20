#!/usr/bin/env python3
"""
Remove duplicate logic from loadISArchitectContent since it's now handled globally
"""

def cleanup_duplicate_logic():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Removing duplicate logic from loadISArchitectContent...")
    
    # Remove tendency pills logic (now handled by setTendencyPills)
    tendency_block = '''            // Set tendency pills
            const tendencyPill = document.getElementById('tendencyPill');
            if (tendencyPill) {
                tendencyPill.textContent = 'Architect';
                tendencyPill.className = 'tendency-pill architect-pill';
            }
            
            const secondaryTendencyPill = document.getElementById('secondaryTendencyPill');
            if (secondaryTendencyPill) {
                secondaryTendencyPill.textContent = 'Gardener';
                secondaryTendencyPill.className = 'tendency-pill secondary-tendency gardener-pill';
            }
            
            // Set tendency description
            const tendencyDesc = document.getElementById('tendencyDescription');
            if (tendencyDesc) {
                tendencyDesc.innerHTML = 'The <strong>Architect</strong> is your dominant sensemaking tendency. This means you gravitate towards structuring and organizing the things around you. However, it doesn\\'t mean the things around you are organized, only that you prefer clarity and understanding over uncertainty, but sometimes even…opportunities.';
            }'''
    
    # Remove archetype description logic (now handled by setArchetypeDescription)
    archetype_block = '''            // Set archetype description
            const archetypeDesc = document.getElementById('archetypeDescription');
            if (archetypeDesc) {
                archetypeDesc.innerHTML = 'The <strong>Inner Guide</strong> is your dominant sensemaking archetype, followed by the <strong>Synthesizer</strong>. This means you naturally focus on things that you find intrinsically meaningful, along with having a desire to deeply make sense of those things.';
            }'''
    
    # Count occurrences
    tendency_count = content.count(tendency_block)
    archetype_count = content.count(archetype_block)
    
    print(f"Found {tendency_count} instances of tendency block to remove")
    print(f"Found {archetype_count} instances of archetype block to remove")
    
    # Remove the blocks
    content = content.replace(tendency_block, '')
    content = content.replace(archetype_block, '')
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Removed duplicate tendency logic from loadISArchitectContent")
    print("✅ Removed duplicate archetype logic from loadISArchitectContent")
    print("✅ All content now handled globally by the new functions")

if __name__ == "__main__":
    cleanup_duplicate_logic()