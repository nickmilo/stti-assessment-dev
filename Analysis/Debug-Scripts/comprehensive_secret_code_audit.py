#!/usr/bin/env python3
"""
Comprehensive audit of all secret codes and their actual profile mappings
Following SOP Tenet #2: Use Python scripts to re-familiarize with entirety of code
Following SOP Tenet #5: Use appropriate tools for accurate analysis
"""

def comprehensive_secret_code_audit():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== COMPREHENSIVE SECRET CODE AUDIT ===\n")
    
    # Find the exact secret code implementation
    lines = content.split('\n')
    secret_code_mappings = {}
    current_code = None
    
    print("🔍 Extracting ACTUAL secret code mappings from source:")
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        
        # Look for keySequence === pattern
        if 'keySequence ===' in line_stripped and "'0" in line_stripped:
            # Extract the code
            start = line_stripped.find("'") + 1
            end = line_stripped.find("'", start)
            current_code = line_stripped[start:end]
            
            print(f"\n📋 Found code {current_code} at line {i+1}:")
            print(f"   {line_stripped}")
            
            # Look ahead for the activateProfile call
            profile_found = False
            for j in range(i+1, min(i+10, len(lines))):
                next_line = lines[j].strip()
                if 'activateProfile(' in next_line:
                    # Extract profile name
                    start_profile = next_line.find("'") + 1
                    end_profile = next_line.find("'", start_profile)
                    if start_profile > 0 and end_profile > start_profile:
                        profile = next_line[start_profile:end_profile]
                        secret_code_mappings[current_code] = profile
                        print(f"   → Maps to: {profile}")
                        profile_found = True
                        break
                elif 'keySequence' in next_line and current_code:
                    # Hit another code before finding profile
                    break
            
            if not profile_found:
                print(f"   ❌ No profile mapping found for {current_code}")
    
    print(f"\n📊 COMPLETE ACTUAL MAPPINGS:")
    for code in sorted(secret_code_mappings.keys()):
        profile = secret_code_mappings[code]
        print(f"   {code} → {profile}")
    
    # Check for duplicates
    print(f"\n🔍 CHECKING FOR DUPLICATE PROFILES:")
    profile_to_codes = {}
    for code, profile in secret_code_mappings.items():
        if profile in profile_to_codes:
            profile_to_codes[profile].append(code)
        else:
            profile_to_codes[profile] = [code]
    
    duplicates_found = False
    for profile, codes in profile_to_codes.items():
        if len(codes) > 1:
            print(f"   ❌ DUPLICATE: {profile} appears in codes: {codes}")
            duplicates_found = True
    
    if not duplicates_found:
        print("   ✅ No duplicate profiles found")
    
    # Check what SHOULD be mapped vs what IS mapped
    print(f"\n🎯 EXPECTED VS ACTUAL ANALYSIS:")
    
    expected_mappings = {
        '0001': 'IP-Architect', '0002': 'IP-Gardener', '0003': 'IS-Architect', '0004': 'IS-Gardener',
        '0005': 'IC-Architect', '0006': 'IC-Gardener', '0007': 'PI-Architect', '0008': 'PI-Gardener',
        '0009': 'PS-Architect', '0010': 'PS-Gardener', '0011': 'PC-Architect', '0012': 'PC-Gardener',
        '0013': 'SI-Architect', '0014': 'SI-Gardener', '0015': 'SP-Architect', '0016': 'SP-Gardener',
        '0017': 'SC-Architect', '0018': 'SC-Gardener', '0019': 'CI-Architect', '0020': 'CI-Gardener',
        '0021': 'CP-Architect', '0022': 'CP-Gardener', '0023': 'CS-Architect', '0024': 'CS-Gardener'
    }
    
    mismatches = []
    for code in sorted(expected_mappings.keys()):
        expected = expected_mappings[code]
        actual = secret_code_mappings.get(code, 'NOT FOUND')
        
        if expected != actual:
            mismatches.append((code, expected, actual))
            print(f"   ❌ {code}: Expected {expected}, Got {actual}")
        else:
            print(f"   ✅ {code}: {actual} (correct)")
    
    print(f"\n📋 SUMMARY:")
    print(f"   Total codes found: {len(secret_code_mappings)}")
    print(f"   Duplicates found: {len([p for p, c in profile_to_codes.items() if len(c) > 1])}")
    print(f"   Mismatches found: {len(mismatches)}")
    
    if mismatches:
        print(f"\n🚨 CRITICAL ISSUES FOUND:")
        for code, expected, actual in mismatches:
            print(f"   Code {code}: Should be {expected}, currently {actual}")
        print(f"\n   User is correct - secret codes need fixing!")
    else:
        print(f"\n✅ All secret codes are correctly mapped!")
    
    return secret_code_mappings, mismatches

if __name__ == "__main__":
    comprehensive_secret_code_audit()