#!/usr/bin/env python3
"""
Extract all 24 secret codes and their profile mappings
Following tenet #2: Re-familiarize with code structure
"""

def extract_all_secret_codes():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ALL SECRET CODES AND PROFILES ===\n")
    
    # Find the secret code section
    lines = content.split('\n')
    secret_codes = {}
    
    for i, line in enumerate(lines):
        if 'keySequence ===' in line and "'0" in line:
            # Extract the code
            start = line.find("'") + 1
            end = line.find("'", start)
            code = line[start:end]
            
            # Look at the next few lines for the profile activation
            profile = None
            for j in range(i+1, min(i+5, len(lines))):
                next_line = lines[j]
                if 'activateProfile(' in next_line:
                    # Extract profile name from activateProfile call
                    start_profile = next_line.find("'") + 1
                    end_profile = next_line.find("'", start_profile)
                    profile = next_line[start_profile:end_profile]
                    break
            
            if profile:
                secret_codes[code] = profile
                print(f"{code} → {profile}")
    
    print(f"\nTotal secret codes found: {len(secret_codes)}")
    
    # Check which profiles are missing
    all_profiles = [
        'IS-Architect', 'IS-Gardener', 'IP-Architect', 'IP-Gardener',
        'CP-Architect', 'CP-Gardener', 'CS-Architect', 'CS-Gardener', 
        'PS-Architect', 'PS-Gardener', 'CI-Architect', 'CI-Gardener',
        'IC-Architect', 'IC-Gardener', 'PC-Architect', 'PC-Gardener',
        'SC-Architect', 'SC-Gardener', 'SP-Architect', 'SP-Gardener',
        'SI-Architect', 'SI-Gardener', 'PI-Architect', 'PI-Gardener'
    ]
    
    print(f"\n🔍 Missing profiles from secret codes:")
    mapped_profiles = set(secret_codes.values())
    for profile in all_profiles:
        if profile not in mapped_profiles:
            print(f"   ❌ {profile}")
    
    return secret_codes

if __name__ == "__main__":
    extract_all_secret_codes()