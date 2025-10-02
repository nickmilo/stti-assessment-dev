#!/usr/bin/env python3
"""
Remove duplicate orientation logic from loadISArchitectContent
"""

def fix_orientation_duplicates():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Removing duplicate orientation logic...")
    
    # Remove the duplicate orientation assignment in loadISArchitectContent (around line 1801-1804)
    old_block_1 = '''            // Set orientation description
            const westernerDesc = document.getElementById('westernerDescription');
            if (westernerDesc) {
                westernerDesc.innerHTML = 'As an <strong>IS-Architect</strong>, you have a <strong>Westerner</strong> profile with a tendency to <strong>architect</strong> (notice how the image is predominantly focused on the western side). Westerners are known as "philosophers." They often get stuck reflecting and ruminating, and have difficulty moving from thinking to doing.';
            }'''
    
    # Also remove orientation pill setting since it's handled globally
    old_block_2 = '''            // Set orientation pill
            const orientationPill = document.getElementById('orientationPill');
            if (orientationPill) orientationPill.textContent = 'Westerner';'''
    
    # Count occurrences before removal
    count_1 = content.count(old_block_1)
    count_2 = content.count(old_block_2)
    
    print(f"Found {count_1} instances of orientation description duplicate")
    print(f"Found {count_2} instances of orientation pill duplicate")
    
    # Remove duplicates
    content = content.replace(old_block_1, '')
    content = content.replace(old_block_2, '')
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Removed duplicate orientation logic")
    print("✅ Orientation is now handled globally by setOrientation() for all 24 profiles")

if __name__ == "__main__":
    fix_orientation_duplicates()