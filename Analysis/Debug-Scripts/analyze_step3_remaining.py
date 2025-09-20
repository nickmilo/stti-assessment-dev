#!/usr/bin/env python3
"""
Analyze what parts of Step 3 are still missing for all 24 profiles
"""

def analyze_missing_step3():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== STEP 3 ANALYSIS: What's Missing for All 24 Profiles ===\n")
    
    # Check what IS-Architect has that other profiles need
    print("🔍 Analyzing IS-Architect implementation as reference:")
    
    # 1. Tendency pills and descriptions
    if 'tendencyPill.textContent = ' in content:
        tendency_assignments = content.count('tendencyPill.textContent = ')
        print(f"📊 Tendency pill assignments: {tendency_assignments}")
    
    if 'tendencyDesc.innerHTML = ' in content:
        tendency_descriptions = content.count('tendencyDesc.innerHTML = ')
        print(f"📊 Tendency descriptions: {tendency_descriptions}")
    
    # 2. Archetype descriptions  
    if 'archetypeDesc.innerHTML = ' in content:
        archetype_descriptions = content.count('archetypeDesc.innerHTML = ')
        print(f"📊 Archetype descriptions: {archetype_descriptions}")
    
    # 3. Collapsible sections
    sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection']
    for section in sections:
        if f"'{section}'" in content:
            print(f"📊 {section}: referenced in code")
    
    # Check if we have dynamic functions for these
    functions_needed = [
        'setTendencyPills',
        'setArchetypeDescription', 
        'setCollapsibleSections'
    ]
    
    print("\n🔍 Checking for dynamic functions:")
    for func in functions_needed:
        if f'function {func}' in content:
            print(f"✅ {func} exists")
        else:
            print(f"❌ {func} MISSING - needs to be created")
    
    # Check activateProfile calls
    print("\n🔍 Checking activateProfile function calls:")
    if 'setTendencyPills(code)' in content:
        print("✅ setTendencyPills called in activateProfile")
    else:
        print("❌ setTendencyPills NOT called in activateProfile")
        
    if 'setArchetypeDescription(code)' in content:
        print("✅ setArchetypeDescription called in activateProfile")
    else:
        print("❌ setArchetypeDescription NOT called in activateProfile")
        
    if 'setCollapsibleSections(code)' in content:
        print("✅ setCollapsibleSections called in activateProfile")
    else:
        print("❌ setCollapsibleSections NOT called in activateProfile")
    
    print("\n=== STEP 3 REMAINING TASKS ===")
    print("1. Create setTendencyPills(code) function for all 24 profiles")
    print("2. Create setArchetypeDescription(code) function for all 24 profiles") 
    print("3. Create setCollapsibleSections(code) function for all 24 profiles")
    print("4. Add these function calls to activateProfile()")
    print("5. Remove duplicate logic from loadISArchitectContent()")

if __name__ == "__main__":
    analyze_missing_step3()