#!/usr/bin/env python3
"""
Fix gardener pill CSS class assignment in setTendencyPills function
Following tenet #4: One surgical change at a time
"""

def fix_gardener_pill_class():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing gardener pill CSS class assignment...")
    
    # Fix primary tendency pill class assignment
    old_primary = 'tendencyPill.className = `tendency-pill ${tendency === "Architect" ? "architect" : "garden"}-pill`;'
    new_primary = 'tendencyPill.className = `tendency-pill ${tendency === "Architect" ? "architect" : "gardener"}-pill`;'
    
    if old_primary in content:
        content = content.replace(old_primary, new_primary)
        print("✅ Fixed primary tendency pill: 'garden-pill' → 'gardener-pill'")
    else:
        print("❌ Could not find primary tendency pill assignment to fix")
    
    # Also fix secondary tendency pill if it has similar issue
    old_secondary = 'secondaryTendencyPill.className = `tendency-pill secondary-tendency ${secondaryTendency.toLowerCase()}-pill`;'
    new_secondary = 'secondaryTendencyPill.className = `tendency-pill secondary-tendency ${secondaryTendency === "Architect" ? "architect" : "gardener"}-pill`;'
    
    if old_secondary in content:
        content = content.replace(old_secondary, new_secondary)
        print("✅ Fixed secondary tendency pill: consistent class assignment")
    else:
        print("❌ Could not find secondary tendency pill assignment to fix")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Gardener pills should now have proper green styling")

if __name__ == "__main__":
    fix_gardener_pill_class()