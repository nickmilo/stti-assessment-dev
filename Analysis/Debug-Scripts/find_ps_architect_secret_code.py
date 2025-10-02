#!/usr/bin/env python3
"""
Find which secret code corresponds to PS-Architect
Following tenet #2: Re-familiarize with code structure
"""

def find_ps_architect_secret_code():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== SECRET CODE MAPPING ANALYSIS ===\n")
    
    # Find all profile codes defined for secret codes
    lines = content.split('\n')
    profile_mappings = []
    
    for i, line in enumerate(lines, 1):
        if "'0" in line and "'" in line and ":" in line:
            # Look for pattern like '0001': 'Profile-Name'
            if line.strip().startswith("'0") or "'" in line:
                profile_mappings.append((i, line.strip()))
    
    print("🔍 Found secret code mappings:")
    for line_num, mapping in profile_mappings:
        print(f"   Line {line_num}: {mapping}")
    
    # Look for PS-Architect specifically
    ps_architect_found = False
    for line_num, mapping in profile_mappings:
        if 'PS-Architect' in mapping:
            print(f"\n✅ PS-Architect found: {mapping}")
            ps_architect_found = True
    
    if not ps_architect_found:
        print(f"\n❌ PS-Architect not found in secret code mappings")
        print("   This means PS-Architect may not have a secret code assigned yet")
        
        # Check if there's a pattern we can determine
        print(f"\n🔍 Checking for existing profile order pattern...")
        existing_profiles = []
        for line_num, mapping in profile_mappings:
            if ':' in mapping:
                parts = mapping.split(':')
                if len(parts) >= 2:
                    code = parts[0].strip().strip("'")
                    profile = parts[1].strip().strip("',")
                    existing_profiles.append((code, profile))
        
        print(f"   Existing mappings:")
        for code, profile in existing_profiles:
            print(f"     {code} → {profile}")
        
        # Predict where PS-Architect might be
        if len(existing_profiles) >= 8:
            next_codes = [f"{i:04d}" for i in range(9, 25)]
            print(f"\n💡 PS-Architect would likely be one of: {next_codes[:4]}")
            print(f"   (Profiles 9-12 are PS-Architect, PS-Gardener, CI-Architect, CI-Gardener)")

if __name__ == "__main__":
    find_ps_architect_secret_code()