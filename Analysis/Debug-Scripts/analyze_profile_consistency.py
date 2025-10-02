#!/usr/bin/env python3
"""
Analyze the inconsistency between IS-Architect and other profiles
Following tenet #2: Re-familiarize with code structure
"""

def analyze_profile_consistency():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== PROFILE IMPLEMENTATION CONSISTENCY ANALYSIS ===\n")
    
    # 1. Check how each profile is handled in activateProfile
    print("🔍 Profile handling in activateProfile:")
    
    profiles = ['IS-Architect', 'IS-Gardener', 'IP-Architect', 'IP-Gardener']
    for profile in profiles:
        if f"code === '{profile}'" in content:
            print(f"   ✅ {profile}: Has specific handling in activateProfile")
        else:
            print(f"   ❌ {profile}: No specific handling in activateProfile")
    
    # 2. Check for loadXXXContent functions
    print(f"\n🔍 Dedicated load functions:")
    if 'function loadISArchitectContent()' in content:
        print("   ✅ IS-Architect: Has loadISArchitectContent() function")
    else:
        print("   ❌ IS-Architect: No dedicated load function")
    
    for profile in ['IS-Gardener', 'IP-Architect', 'IP-Gardener']:
        function_name = f"load{profile.replace('-', '')}Content"
        if f'function {function_name}()' in content:
            print(f"   ✅ {profile}: Has {function_name}() function")
        else:
            print(f"   ❌ {profile}: No dedicated load function")
    
    # 3. Check setCollapsibleSections for specific profile logic
    print(f"\n🔍 setCollapsibleSections specific logic:")
    for profile in profiles:
        if f"code === '{profile}'" in content and 'setCollapsibleSections' in content:
            # Find the setCollapsibleSections function
            start = content.find('function setCollapsibleSections(code) {')
            end = content.find('function ', start + 1)
            section = content[start:end]
            
            if f"code === '{profile}'" in section:
                print(f"   ✅ {profile}: Has specific logic in setCollapsibleSections")
            else:
                print(f"   ❌ {profile}: No specific logic in setCollapsibleSections")
        else:
            print(f"   ❌ {profile}: No specific logic in setCollapsibleSections")
    
    # 4. Count lines of code for each approach
    print(f"\n📊 Code size analysis:")
    
    # Count loadISArchitectContent function size
    start = content.find('function loadISArchitectContent() {')
    if start != -1:
        end = content.find('function ', start + 1)
        if end == -1:
            end = len(content)
        function_size = len(content[start:end].split('\n'))
        print(f"   IS-Architect loadISArchitectContent(): ~{function_size} lines")
    
    # Count setCollapsibleSections profile-specific logic
    start = content.find('function setCollapsibleSections(code) {')
    if start != -1:
        end = content.find('function ', start + 1)
        section = content[start:end]
        
        specific_blocks = section.count("code === '")
        print(f"   setCollapsibleSections: {specific_blocks} profile-specific blocks")
    
    print(f"\n💡 RECOMMENDATIONS:")
    print("   Option A: Move IS-Architect to setCollapsibleSections pattern (consistent)")
    print("   Option B: Keep IS-Architect separate, move others to loadXXXContent pattern")
    print("   Option C: Leave as-is and continue with current mixed approach")
    
    print(f"\n🤔 DECISION FACTORS:")
    print("   - Consistency: Option A wins (all profiles use same pattern)")
    print("   - File size: Option A wins (eliminates duplicate function)")
    print("   - Maintainability: Option A wins (single place to add profile logic)")
    print("   - Risk: Option A has risk (need to carefully move IS-Architect logic)")
    
    print(f"\n✅ RECOMMENDATION: Option A - Move IS-Architect to setCollapsibleSections")
    print("   This makes all 4 profiles consistent and reduces code duplication.")

if __name__ == "__main__":
    analyze_profile_consistency()