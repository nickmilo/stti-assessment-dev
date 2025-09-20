#!/usr/bin/env python3
"""
Analyze remaining profiles structure and create implementation plan
Following SOP Tenet #2: Use Python script to re-familiarize with code structure
"""

def analyze_remaining_profiles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== REMAINING PROFILES ANALYSIS ===\n")
    
    # Check which profiles are NOT implemented
    remaining_profiles = [
        'IC-Architect', 'IC-Gardener',  # Southerner/Explorer
        'PC-Architect', 'PC-Gardener',  # Easterner/Maker  
        'SC-Architect', 'SC-Gardener',  # Diagonal Translator
        'SP-Architect', 'SP-Gardener',  # Northerner/Builder
        'SI-Architect', 'SI-Gardener',  # Westerner/Philosopher
        'PI-Architect', 'PI-Gardener'   # Diagonal Converter
    ]
    
    print("🔍 Checking implementation status:")
    for profile in remaining_profiles:
        if f"code === '{profile}'" in content:
            print(f"  ✅ {profile} - Already implemented")
        else:
            print(f"  ❌ {profile} - Needs implementation")
    
    # Check archetype combinations and orientations
    print(f"\n📋 Archetype combination mapping:")
    combinations = {
        'IC': 'Southerner/Explorer (Inner Guide + Creative)',
        'PC': 'Easterner/Maker (Producer + Creative)', 
        'SC': 'Diagonal/Translator (Synthesizer + Creative)',
        'SP': 'Northerner/Builder (Synthesizer + Producer)',
        'SI': 'Westerner/Philosopher (Synthesizer + Inner Guide)',
        'PI': 'Diagonal/Converter (Producer + Inner Guide)'
    }
    
    for combo, description in combinations.items():
        print(f"  {combo}: {description}")
    
    # Check tendency logic for each
    print(f"\n🎯 Tendency difficulty patterns:")
    for combo in ['IC', 'PC', 'SC', 'SP', 'SI', 'PI']:
        archetypes = list(combo)
        structured = [a for a in archetypes if a in ['P', 'S']]
        flexible = [a for a in archetypes if a in ['I', 'C']]
        
        print(f"  {combo}:")
        print(f"    Architect: Struggles with {''.join([a for a in ['I', 'C'] if a not in archetypes])}")
        print(f"    Gardener: Struggles with {''.join([a for a in ['P', 'S'] if a not in archetypes])}")
    
    # Validate secret code mappings
    print(f"\n🔑 Secret code mappings:")
    mappings = {
        'IC-Architect': '0005', 'IC-Gardener': '0006',
        'PC-Architect': '0011', 'PC-Gardener': '0012',
        'SC-Architect': '0017', 'SC-Gardener': '0018', 
        'SP-Architect': '0015', 'SP-Gardener': '0016',
        'SI-Architect': '0013', 'SI-Gardener': '0014',
        'PI-Architect': '0007', 'PI-Gardener': '0008'
    }
    
    for profile, code in mappings.items():
        if f"activateProfile('{profile}'" in content:
            print(f"  ✅ {code} → {profile}")
        else:
            print(f"  ❌ {code} → {profile} (mapping missing)")

if __name__ == "__main__":
    analyze_remaining_profiles()