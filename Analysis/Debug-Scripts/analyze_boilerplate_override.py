#!/usr/bin/env python3
"""
Find why boilerplate content overrides specific profile content
Following SOP Tenet #1: Understand structure completely
"""

def analyze_boilerplate_override():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING BOILERPLATE OVERRIDE ISSUE ===")
    print("IC-Gardener specific content exists but boilerplate shows instead\n")
    
    lines = content.split('\n')
    
    # 1. Find setCollapsibleSections function structure
    print("🔍 SETCOLLAPSIBLESECTIONS FUNCTION STRUCTURE:")
    
    setcollapsible_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            setcollapsible_start = i
            break
    
    if setcollapsible_start:
        print(f"Function starts at line {setcollapsible_start}")
        
        # Find IC-Gardener implementation
        ic_gardener_start = None
        ic_gardener_end = None
        
        for i in range(setcollapsible_start - 1, min(setcollapsible_start + 1000, len(lines))):
            line = lines[i]
            if "code === 'IC-Gardener'" in line:
                ic_gardener_start = i + 1
                print(f"\n✅ IC-Gardener specific code found at line {ic_gardener_start}")
                
                # Find where it ends (look for return statement)
                for j in range(i, min(i + 100, len(lines))):
                    if 'return;' in lines[j]:
                        ic_gardener_end = j + 1
                        print(f"   Ends at line {ic_gardener_end} with 'return;'")
                        break
                break
        
        # Find the boilerplate section
        boilerplate_start = None
        for i in range(setcollapsible_start - 1, len(lines)):
            line = lines[i]
            if '// Generic fallback for unspecified profiles' in line or '// Generic logic' in line:
                boilerplate_start = i + 1
                print(f"\n❌ Generic boilerplate starts at line {boilerplate_start}")
                break
        
        # Check for the issue
        if ic_gardener_end and boilerplate_start:
            print(f"\n🔍 CRITICAL ANALYSIS:")
            print(f"IC-Gardener code: lines {ic_gardener_start} to {ic_gardener_end}")
            print(f"Boilerplate code: starts at line {boilerplate_start}")
            
            # Check if IC-Gardener has proper return
            ic_has_return = False
            for i in range(ic_gardener_start - 1, ic_gardener_end):
                if 'return;' in lines[i] and '//' not in lines[i]:  # Not a comment
                    ic_has_return = True
                    print(f"✅ IC-Gardener has return statement at line {i + 1}")
                    break
            
            if not ic_has_return:
                print("❌ IC-Gardener missing return statement - will fall through to boilerplate!")
            
            # Check if there's an issue with the conditional
            for i in range(ic_gardener_start - 5, ic_gardener_start + 5):
                if i >= 0 and i < len(lines):
                    print(f"  Line {i + 1}: {lines[i]}")
        
        # Look for the actual boilerplate content around lines 2339-2360
        print(f"\n🔍 BOILERPLATE CONTENT ANALYSIS:")
        for i in range(2335, 2365):
            if i < len(lines):
                line = lines[i]
                if 'overwhelmedTitle' in line or 'overwhelmedContent' in line:
                    print(f"  Line {i + 1}: {line.strip()[:80]}...")
                if 'stuckTitle' in line or 'stuckContent' in line:
                    print(f"  Line {i + 1}: {line.strip()[:80]}...")
                if 'promptsTitle' in line or 'promptsContent' in line:
                    print(f"  Line {i + 1}: {line.strip()[:80]}...")
        
        # Find if there's a missing else/return
        print(f"\n🔍 CONTROL FLOW ANALYSIS:")
        
        # Check the structure of the function
        brace_count = 0
        in_profile_block = False
        missing_returns = []
        
        for i in range(setcollapsible_start - 1, min(setcollapsible_start + 1000, len(lines))):
            line = lines[i]
            
            if "if (code === " in line:
                in_profile_block = True
                profile_code = line.split("'")[1] if "'" in line else "unknown"
                
                # Check if this profile block has a return
                has_return = False
                j = i
                local_brace_count = 0
                while j < min(i + 100, len(lines)):
                    if '{' in lines[j]:
                        local_brace_count += lines[j].count('{')
                    if '}' in lines[j]:
                        local_brace_count -= lines[j].count('}')
                    if 'return;' in lines[j] and local_brace_count > 0:
                        has_return = True
                        break
                    if local_brace_count == 0 and j > i:
                        break
                    j += 1
                
                if not has_return:
                    missing_returns.append((i + 1, profile_code))
        
        if missing_returns:
            print("❌ PROFILES MISSING RETURN STATEMENTS:")
            for line_num, profile in missing_returns:
                print(f"   Line {line_num}: {profile}")
            print("\n⚠️  WITHOUT RETURN, CODE FALLS THROUGH TO BOILERPLATE!")
    
    print(f"\n📋 SOLUTION:")
    print("Add 'return;' statement after each profile's content is set")
    print("This prevents fall-through to generic boilerplate")
    
    return True

if __name__ == "__main__":
    analyze_boilerplate_override()