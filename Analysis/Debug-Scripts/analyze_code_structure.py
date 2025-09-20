#!/usr/bin/env python3
"""
Analyze the current code structure before adding IP-Architect and IP-Gardener
Following tenet #2: Re-familiarize with entirety of code before modifications
"""

def analyze_code_structure():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== CODE STRUCTURE ANALYSIS ===\n")
    
    # 1. Find all functions
    lines = content.split('\n')
    functions = []
    for i, line in enumerate(lines, 1):
        if 'function ' in line and not line.strip().startswith('//'):
            functions.append((i, line.strip()))
    
    print("📋 All JavaScript functions:")
    for line_num, func_line in functions:
        print(f"   Line {line_num}: {func_line}")
    
    # 2. Check current profile handling
    print(f"\n🔍 Current profile-specific handling:")
    if "code === 'IS-Architect'" in content:
        print("   ✅ IS-Architect: Has specific handling")
    if "code === 'IS-Gardener'" in content:
        print("   ✅ IS-Gardener: Has specific handling")
    if "code === 'IP-Architect'" in content:
        print("   ✅ IP-Architect: Has specific handling")
    else:
        print("   ❌ IP-Architect: No specific handling yet")
    if "code === 'IP-Gardener'" in content:
        print("   ✅ IP-Gardener: Has specific handling")
    else:
        print("   ❌ IP-Gardener: No specific handling yet")
    
    # 3. Check for redundancies or inefficiencies
    print(f"\n🔍 Potential cleanup opportunities:")
    
    # Check for duplicate orientation logic
    westerner_count = content.count("orientation === 'Westerner'")
    easterner_count = content.count("orientation === 'Easterner'")
    print(f"   - Orientation logic appears {westerner_count} times for Westerner, {easterner_count} times for Easterner")
    
    # Check for showSpecificProfile vs activateProfile confusion
    show_specific_calls = content.count('showSpecificProfile(')
    activate_profile_calls = content.count('activateProfile(')
    print(f"   - showSpecificProfile called {show_specific_calls} times")
    print(f"   - activateProfile called {activate_profile_calls} times")
    
    # Check file size
    line_count = len(lines)
    char_count = len(content)
    print(f"   - File size: {line_count} lines, {char_count:,} characters")
    
    # 4. Identify the specific structure for IS-Architect and IS-Gardener
    print(f"\n📋 Current IS-Architect/IS-Gardener structure:")
    
    # Check activateProfile logic
    activate_start = content.find('function activateProfile(code, name) {')
    if activate_start != -1:
        activate_end = content.find('function ', activate_start + 1)
        activate_section = content[activate_start:activate_end]
        
        if 'loadISArchitectContent()' in activate_section:
            print("   ✅ IS-Architect uses loadISArchitectContent() function")
        
        if "code === 'IS-Gardener'" in activate_section:
            print("   ❌ IS-Gardener uses inline logic in setCollapsibleSections (should be consistent)")
        
    # Check setCollapsibleSections for specific profile logic
    set_collapsible_start = content.find('function setCollapsibleSections(code) {')
    if set_collapsible_start != -1:
        set_collapsible_end = content.find('function ', set_collapsible_start + 1)
        set_collapsible_section = content[set_collapsible_start:set_collapsible_end]
        
        specific_profiles = []
        if "code === 'IS-Gardener'" in set_collapsible_section:
            specific_profiles.append('IS-Gardener')
        
        print(f"   📊 setCollapsibleSections has specific logic for: {specific_profiles}")
    
    print(f"\n💡 RECOMMENDATIONS:")
    print("   1. Maintain consistency - either all profiles use loadXXXContent() or all use setCollapsibleSections logic")
    print("   2. IP profiles should follow same pattern as IS profiles")
    print("   3. Consider if showSpecificProfile function is still needed or creates confusion")

if __name__ == "__main__":
    analyze_code_structure()