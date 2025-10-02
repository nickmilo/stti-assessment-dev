#!/usr/bin/env python3
"""
Check which profiles are actually implemented in setCollapsibleSections
Following SOP Tenet #2: Use Python to analyze code structure
"""

import re

def check_setcollapsiblesections_profiles():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== PROFILES IN setCollapsibleSections ===\n")
    
    # Find setCollapsibleSections function
    func_start = content.find('function setCollapsibleSections(')
    if func_start != -1:
        # Find the function end
        brace_count = 0
        start_brace = content.find('{', func_start)
        end_pos = start_brace
        
        for i, char in enumerate(content[start_brace:], start_brace):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_pos = i
                    break
        
        func_content = content[func_start:end_pos]
        
        # Find all profile implementations using regex
        profile_pattern = r"code === '([^']+)'"
        matches = re.findall(profile_pattern, func_content)
        
        print("✅ Profiles implemented in setCollapsibleSections:")
        for i, profile in enumerate(matches, 1):
            print(f"  {i:2d}. {profile}")
        
        print(f"\nTotal profiles found: {len(matches)}")
        
        # Check specifically for profiles we care about
        critical_profiles = ['PS-Architect', 'PS-Gardener', 'CI-Architect', 'CI-Gardener', 'IS-Architect']
        
        print("\n🔍 Critical profile check:")
        for profile in critical_profiles:
            if profile in matches:
                print(f"  ✅ {profile}")
            else:
                print(f"  ❌ {profile} - NOT IMPLEMENTED")
        
        # Check if PS-Architect is missing
        if 'PS-Architect' not in matches:
            print("\n🚨 CRITICAL ISSUE FOUND:")
            print("   PS-Architect is NOT implemented in setCollapsibleSections!")
            print("   This means 0009 would fall back to generic content")
            print("   User is correct - PS-Architect is not working properly")
            
            # Check if it exists anywhere in the file
            if 'PS-Architect' in content:
                print("   PS-Architect exists elsewhere in the file")
                # Find where
                ps_positions = []
                start_search = 0
                while True:
                    pos = content.find('PS-Architect', start_search)
                    if pos == -1:
                        break
                    line_num = content[:pos].count('\n') + 1
                    ps_positions.append(line_num)
                    start_search = pos + 1
                
                print(f"   Found PS-Architect at lines: {ps_positions}")
            else:
                print("   PS-Architect does not exist anywhere in the file")
        
    else:
        print("❌ setCollapsibleSections function not found")

if __name__ == "__main__":
    check_setcollapsiblesections_profiles()