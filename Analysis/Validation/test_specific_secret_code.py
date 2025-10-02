#!/usr/bin/env python3
"""
Test what actually happens when specific secret codes are triggered
Following SOP Tenet #3: Validate functionality works as expected
"""

def test_specific_secret_code():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== TESTING SPECIFIC SECRET CODE 0009 ===\n")
    
    # Find the exact code for 0009
    lines = content.split('\n')
    found_0009 = False
    
    for i, line in enumerate(lines):
        if "'0009'" in line and 'keySequence' in line:
            print(f"📋 Found 0009 definition at line {i+1}:")
            print(f"   {line.strip()}")
            
            # Show next 5 lines to see the complete logic
            print(f"\n📋 Following lines:")
            for j in range(i+1, min(i+6, len(lines))):
                print(f"   {j+1:4d}: {lines[j]}")
            
            found_0009 = True
            break
    
    if not found_0009:
        print("❌ Could not find 0009 definition")
        return
    
    # Also check what PS-Architect profile actually contains
    print(f"\n🔍 CHECKING PS-ARCHITECT IMPLEMENTATION:")
    
    # Check if PS-Architect is in setCollapsibleSections
    if "code === 'PS-Architect'" in content:
        print("✅ PS-Architect found in setCollapsibleSections")
        
        # Find the PS-Architect block
        start = content.find("code === 'PS-Architect'")
        # Find the end of the block (return statement)
        end = content.find("return; // Exit early, don't use generic logic", start)
        if end != -1:
            ps_block = content[start:end]
            
            # Check for specific content indicators
            if "Northerner" in ps_block:
                print("✅ Contains Northerner content")
            else:
                print("❌ Missing Northerner content")
                
            if "Creative difficult" in ps_block:
                print("✅ Contains Creative difficulty logic")
            else:
                print("❌ Missing Creative difficulty logic")
                
            if "Inner Guide pathway" in ps_block:
                print("✅ Contains Inner Guide pathway")  
            else:
                print("❌ Missing Inner Guide pathway")
        
    else:
        print("❌ PS-Architect NOT found in setCollapsibleSections")
        print("   This could be why 0009 isn't working correctly")
    
    # Double-check if there are any issues with function definitions
    print(f"\n🔍 CHECKING FUNCTION DEFINITIONS:")
    if 'function setCollapsibleSections' in content:
        print("✅ setCollapsibleSections function exists")
    else:
        print("❌ setCollapsibleSections function missing")
        
    if 'function activateProfile' in content:
        print("✅ activateProfile function exists")
    else:
        print("❌ activateProfile function missing")

if __name__ == "__main__":
    test_specific_secret_code()