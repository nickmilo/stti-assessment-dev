#!/usr/bin/env python3
"""
Analyze code structure and plan next 4 profiles
Following tenet #2: Re-familiarize with entirety of code
"""

def analyze_next_4_profiles():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== NEXT 4 PROFILES ANALYSIS ===\n")
    
    # 1. Review current profile coverage
    print("📋 Current profile coverage:")
    completed_profiles = ['IS-Architect', 'IS-Gardener', 'IP-Architect', 'IP-Gardener']
    for profile in completed_profiles:
        if f"code === '{profile}'" in content:
            print(f"   ✅ {profile}: Complete")
        else:
            print(f"   ❌ {profile}: Missing")
    
    # 2. Determine next 4 profiles logically
    print(f"\n🎯 Next 4 profiles to implement:")
    
    # Based on archetype combinations:
    # IS = Inner Guide + Synthesizer (Westerner) ✅ Done
    # IP = Inner Guide + Producer (Diagonal Converter) ✅ Done
    # Next logical: CP = Creative + Producer (Easterner), CS = Creative + Synthesizer (Diagonal Translator)
    
    next_profiles = ['CP-Architect', 'CP-Gardener', 'CS-Architect', 'CS-Gardener']
    for profile in next_profiles:
        print(f"   📝 {profile}: To implement")
    
    # 3. Review the established pattern
    print(f"\n🔍 Established pattern review:")
    
    # Check setCollapsibleSections structure
    start = content.find('function setCollapsibleSections(code) {')
    if start != -1:
        end = content.find('function ', start + 1)
        function_section = content[start:end]
        
        current_blocks = function_section.count("code === '")
        print(f"   Current profile blocks in setCollapsibleSections: {current_blocks}")
        
        # Check pattern consistency
        if "return; // Exit early, don't use generic logic" in function_section:
            print(f"   ✅ Early return pattern established")
        
        if "overwhelmedTitle.textContent =" in function_section:
            print(f"   ✅ Overwhelmed section pattern established")
            
        if "stuckTitle.textContent =" in function_section:
            print(f"   ✅ Stuck/unstuck section pattern established")
            
        if "promptsTitle.textContent =" in function_section:
            print(f"   ✅ Prompts section pattern established")
    
    # 4. Check orientation mappings for CP and CS
    print(f"\n🧭 Orientation mappings for next profiles:")
    
    orientation_mapping = {
        'CP': 'Easterner (Creative + Producer)',
        'CS': 'Diagonal Translator (Creative + Synthesizer)'
    }
    
    for combo, orientation in orientation_mapping.items():
        print(f"   {combo}: {orientation}")
    
    # 5. Review tendency logic we need to follow
    print(f"\n🎯 Tendency logic to implement:")
    print("   CP-Architect: Producer most difficult → Creative pathway (structured)")
    print("   CP-Gardener: Creative most difficult → Producer pathway (flexible)")
    print("   CS-Architect: Synthesizer most difficult → Inner Guide pathway (structured)")
    print("   CS-Gardener: Inner Guide most difficult → Synthesizer pathway (flexible)")
    
    print(f"\n✅ READY TO IMPLEMENT:")
    print("   1. Add CP-Architect and CP-Gardener (Easterners/Makers)")
    print("   2. Add CS-Architect and CS-Gardener (Diagonal Translators)")
    print("   3. Follow established setCollapsibleSections pattern")
    print("   4. Use consistent early return structure")

if __name__ == "__main__":
    analyze_next_4_profiles()