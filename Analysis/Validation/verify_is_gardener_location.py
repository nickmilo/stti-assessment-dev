#!/usr/bin/env python3
"""
Verify where IS-Gardener content should be and if it was updated correctly
"""

def verify_is_gardener_location():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== VERIFYING IS-GARDENER CONTENT LOCATION ===\n")
    
    # Check if there's a specific loadISGardenerContent function
    if 'loadISGardenerContent' in content:
        print("✅ Found loadISGardenerContent function")
    else:
        print("❌ No loadISGardenerContent function found")
    
    # Check the activateProfile function to see how IS-Gardener is handled
    lines = content.split('\n')
    in_activate_profile = False
    
    print("🔍 Checking activateProfile function for IS-Gardener handling:")
    for i, line in enumerate(lines, 1):
        if 'function activateProfile' in line:
            in_activate_profile = True
            print(f"   Line {i}: Found activateProfile function")
        elif in_activate_profile and ('IS-Gardener' in line or 'Gardener' in line):
            print(f"   Line {i}: {line.strip()}")
        elif in_activate_profile and line.strip() == '}' and 'function' in lines[i] if i < len(lines) else False:
            break
    
    # Check if IS-Gardener gets any special treatment
    if "code === 'IS-Gardener'" in content:
        print("✅ Found IS-Gardener specific code")
    else:
        print("❌ No IS-Gardener specific code found")
        print("   This means IS-Gardener uses the generic setCollapsibleSections function")
    
    # Check what the current overwhelmed content says for Westerners
    if "They often get stuck going from being oriented inward to outward" in content:
        print("✅ Found updated overwhelmed content")
    else:
        print("❌ Overwhelmed content not updated")
    
    print("\n=== RECOMMENDATION ===")
    print("IS-Gardener likely needs its own specific loadISGardenerContent function")
    print("similar to loadISArchitectContent, or the generic functions need IS-Gardener")
    print("specific logic added to them.")

if __name__ == "__main__":
    verify_is_gardener_location()