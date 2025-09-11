#!/usr/bin/env python3
"""
Analyze code structure and plan PS and CI profiles (next batch)
Following tenet #2: Re-familiarize with entirety of code
"""

def analyze_next_ps_ci_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== NEXT PS AND CI PROFILES ANALYSIS ===\n")
    
    # 1. Review current status
    print("📋 Current profile status (8/24 complete):")
    completed = ['IS-Architect', 'IS-Gardener', 'IP-Architect', 'IP-Gardener', 
                'CP-Architect', 'CP-Gardener', 'CS-Architect', 'CS-Gardener']
    for profile in completed:
        print(f"   ✅ {profile}")
    
    # 2. Next logical profiles
    print(f"\n🎯 Next batch to implement:")
    next_profiles = ['PS-Architect', 'PS-Gardener', 'CI-Architect', 'CI-Gardener']
    for profile in next_profiles:
        print(f"   📝 {profile}: To implement")
    
    # 3. Orientation mappings
    print(f"\n🧭 Orientation mappings:")
    print("   PS (Producer + Synthesizer): Northerner (Builder)")
    print("   CI (Creative + Inner Guide): Southerner (Explorer)")
    
    # 4. Tendency logic for new profiles
    print(f"\n🎯 Tendency logic (following established pattern):")
    print("   PS-Architect: Creative difficult → Inner Guide pathway")
    print("   PS-Gardener: Inner Guide difficult → Creative pathway")
    print("   CI-Architect: Synthesizer difficult → Producer pathway")
    print("   CI-Gardener: Producer difficult → Synthesizer pathway")
    
    # 5. Overwhelmed content patterns
    print(f"\n📋 Overwhelmed content needed:")
    print("   Northerners: Over-plan/structure → need decisive action")
    print("   Southerners: Get lost in exploration → need grounding structure")
    
    # 6. Check current setCollapsibleSections structure
    start = content.find('function setCollapsibleSections(code) {')
    if start != -1:
        end = content.find('function ', start + 1)
        function_section = content[start:end]
        current_blocks = function_section.count("code === '")
        print(f"\n🔍 Current setCollapsibleSections:")
        print(f"   Profile blocks: {current_blocks}")
        print(f"   Pattern established: ✅")
    
    print(f"\n✅ READY TO IMPLEMENT PS AND CI PROFILES")
    print("   Following established setCollapsibleSections pattern")
    print("   Using tendency logic from working examples")
    print("   Adding new orientation overwhelmed patterns")

if __name__ == "__main__":
    analyze_next_ps_ci_profiles()