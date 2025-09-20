#!/usr/bin/env python3
"""
Analyze the orientation implementation in the STTI assessment
"""

def analyze_orientation_code():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ORIENTATION ANALYSIS ===\n")
    
    # Find setOrientation function
    if 'function setOrientation' in content:
        print("✅ setOrientation function EXISTS")
        
        # Find where it's called
        if 'setOrientation(code);' in content:
            print("✅ setOrientation is CALLED in activateProfile")
        else:
            print("❌ setOrientation is NOT called")
    else:
        print("❌ setOrientation function MISSING")
    
    # Check for duplicate orientation logic
    orientation_desc_count = content.count('westernerDesc.innerHTML = ')
    print(f"📊 Found {orientation_desc_count} instances of westernerDesc.innerHTML assignment")
    
    if orientation_desc_count > 1:
        print("⚠️  DUPLICATE orientation logic detected")
        
        # Find all instances
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if 'westernerDesc.innerHTML = ' in line:
                print(f"   Line {i}: {line.strip()[:80]}...")
    
    # Check orientation mappings
    orientations = ['Westerner', 'Easterner', 'Northerner', 'Southerner', 'Diagonal']
    for orientation in orientations:
        count = content.count(f"orientation === '{orientation}'")
        print(f"📍 {orientation}: {count} condition(s)")
    
    print("\n=== RECOMMENDATIONS ===")
    if orientation_desc_count > 1:
        print("1. Remove duplicate orientation logic from loadISArchitectContent()")
    
    # Check if all profiles have orientation coverage
    archetype_combinations = ['IS', 'CP', 'PS', 'CI', 'CS', 'IP']
    print("2. Orientation coverage check:")
    for combo in archetype_combinations:
        if f"sortedArchetypes === '{combo}'" in content:
            print(f"   ✅ {combo} covered")
        else:
            print(f"   ❌ {combo} missing")

if __name__ == "__main__":
    analyze_orientation_code()