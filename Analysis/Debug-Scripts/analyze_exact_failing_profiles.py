#!/usr/bin/env python3
"""
Analyze exactly which profiles are failing based on the secret code mappings
Following SOP Tenet #2: Use Python to understand structure completely
"""

def analyze_failing_profiles():
    # Based on user's test results:
    working_codes = ['0001', '0002', '0003', '0004', '0009', '0010', '0012', '0019', '0020', '0021', '0022', '0023', '0024']
    failing_codes = ['0005', '0006', '0007', '0008', '0011', '0013', '0014', '0015', '0016', '0017', '0018']
    
    # Code to profile mapping from the keydown event handler
    code_mapping = {
        '0001': 'IP-Architect',
        '0002': 'IP-Gardener', 
        '0003': 'IS-Architect',
        '0004': 'IS-Gardener',
        '0005': 'IC-Architect',
        '0006': 'IC-Gardener',
        '0007': 'PI-Architect',
        '0008': 'PI-Gardener',
        '0009': 'PS-Architect',
        '0010': 'PS-Gardener',
        '0011': 'PC-Architect',
        '0012': 'PC-Gardener',
        '0013': 'SI-Architect',
        '0014': 'SI-Gardener',
        '0015': 'SP-Architect',
        '0016': 'SP-Gardener',
        '0017': 'SC-Architect',
        '0018': 'SC-Gardener',
        '0019': 'CI-Architect',
        '0020': 'CI-Gardener',
        '0021': 'CP-Architect',
        '0022': 'CP-Gardener',
        '0023': 'CS-Architect',
        '0024': 'CS-Gardener'
    }
    
    print("=== EXACT ANALYSIS OF FAILING PROFILES ===")
    print()
    
    working_profiles = [code_mapping[code] for code in working_codes]
    failing_profiles = [code_mapping[code] for code in failing_codes]
    
    print("✅ WORKING PROFILES:")
    for i, code in enumerate(working_codes):
        print(f"  {code} -> {working_profiles[i]}")
    
    print(f"\n❌ FAILING PROFILES:")
    for i, code in enumerate(failing_codes):
        print(f"  {code} -> {failing_profiles[i]}")
    
    # Now check what's broken in setCollapsibleSections for these specific profiles
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    print(f"\n🔍 CHECKING SETCOLLAPSIBLESECTIONS FOR FAILING PROFILES:")
    
    # Find setCollapsibleSections function
    setcollapsible_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            setcollapsible_start = i
            break
    
    if not setcollapsible_start:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    print(f"setCollapsibleSections function starts at line {setcollapsible_start}")
    
    # Check each failing profile
    for profile in failing_profiles:
        print(f"\n🔍 Checking {profile}:")
        
        # Find this profile's case statement
        profile_found = False
        profile_start = None
        profile_end = None
        
        for i in range(setcollapsible_start, min(setcollapsible_start + 1000, len(lines))):
            if f"code === '{profile}'" in lines[i]:
                profile_found = True
                profile_start = i + 1
                
                # Find the end (next profile or end of function)
                for j in range(i + 1, min(i + 50, len(lines))):
                    if ('code ===' in lines[j] or 
                        'console.error' in lines[j] or 
                        '} else if (code ===' in lines[j] or
                        lines[j].strip() == '}'):
                        profile_end = j
                        break
                
                if not profile_end:
                    profile_end = min(i + 30, len(lines))
                break
        
        if not profile_found:
            print(f"  ❌ {profile} NOT FOUND in setCollapsibleSections")
            continue
        
        print(f"  ✅ {profile} found at line {profile_start}")
        
        # Analyze the implementation
        profile_lines = []
        for i in range(profile_start - 1, profile_end):
            if i < len(lines):
                profile_lines.append((i + 1, lines[i]))
        
        print(f"  📝 Implementation ({len(profile_lines)} lines):")
        
        # Check for syntax errors and completeness
        syntax_errors = []
        has_title_updates = 0
        has_content_updates = 0
        
        for line_num, line in profile_lines:
            line_content = line.strip()
            print(f"    Line {line_num}: {line_content}")
            
            # Check for syntax errors
            if line_content and not line_content.startswith('//'):
                # Check for unmatched quotes
                single_quotes = line_content.count("'")
                double_quotes = line_content.count('"')
                
                if single_quotes % 2 != 0:
                    syntax_errors.append(f"Line {line_num}: Unmatched single quotes")
                if double_quotes % 2 != 0:
                    syntax_errors.append(f"Line {line_num}: Unmatched double quotes")
                
                # Check for essential operations
                if 'Title.textContent' in line_content:
                    has_title_updates += 1
                if 'Content.innerHTML' in line_content:
                    has_content_updates += 1
        
        # Report findings
        if syntax_errors:
            print(f"  ❌ SYNTAX ERRORS FOUND:")
            for error in syntax_errors:
                print(f"     {error}")
        else:
            print(f"  ✅ No obvious syntax errors")
        
        print(f"  📊 Content updates: {has_title_updates} titles, {has_content_updates} content blocks")
        
        if has_title_updates < 3 or has_content_updates < 3:
            print(f"  ⚠️  Incomplete implementation (expected 3 titles and 3 content blocks)")
    
    print(f"\n💡 SUMMARY:")
    print("Need to check each failing profile in setCollapsibleSections for:")
    print("1. Missing case statements")
    print("2. Syntax errors (especially unmatched quotes)")
    print("3. Incomplete implementations")
    print("4. JavaScript errors that break execution")

if __name__ == "__main__":
    analyze_failing_profiles()