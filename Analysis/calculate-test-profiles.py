#!/usr/bin/env python3
"""
Calculate profile codes for secret test codes 0025 and 0026
Mimics the determineProfile() logic from main.js
"""

def determine_profile(scores):
    """
    Replicate main.js determineProfile() logic

    Args:
        scores: dict with keys I, S, P, C, A, G

    Returns:
        dict with code, dominantArchetypes, tendency
    """
    # Get all 4 archetypes sorted by score (highest to lowest)
    archetype_scores = [
        ('I', scores['I']),
        ('S', scores['S']),
        ('P', scores['P']),
        ('C', scores['C'])
    ]

    # Sort by score descending, then alphabetically for ties
    archetype_scores.sort(key=lambda x: (-x[1], x[0]))

    # Determine tendency
    tendency = 'Architect' if scores['A'] > scores['G'] else 'Gardener'

    # Get top 2 dominant archetypes
    dominant_archetypes = [archetype_scores[0][0], archetype_scores[1][0]]

    # Build profile code
    code = ''.join(dominant_archetypes) + '-' + tendency

    return {
        'code': code,
        'dominantArchetypes': dominant_archetypes,
        'tendency': tendency,
        'scores': scores,
        'archetypeScores': archetype_scores
    }

def calculate_orientation(code):
    """Calculate orientation based on archetype combination"""
    archetypes = code.split('-')[0]
    sorted_archetypes = ''.join(sorted(archetypes))

    orientation_map = {
        'IS': 'Westerner',
        'CP': 'Easterner',
        'PS': 'Northerner',
        'CI': 'Southern',
        'CS': 'Diagonal',
        'IP': 'Diagonal'
    }

    return orientation_map.get(sorted_archetypes, 'Mixed')

# Test code 0025: Extreme variance
scores_0025 = {
    'I': 32,
    'S': 8,
    'P': 26,
    'C': 15,
    'A': 32,
    'G': 10
}

profile_0025 = determine_profile(scores_0025)
orientation_0025 = calculate_orientation(profile_0025['code'])

print("=" * 70)
print("SECRET CODE 0025 - EXTREME VARIANCE TEST")
print("=" * 70)
print(f"Raw Scores: I={scores_0025['I']}, S={scores_0025['S']}, P={scores_0025['P']}, C={scores_0025['C']}, A={scores_0025['A']}, G={scores_0025['G']}")
print(f"Profile Code: {profile_0025['code']}")
print(f"Dominant Archetypes: {' & '.join(profile_0025['dominantArchetypes'])}")
print(f"Tendency: {profile_0025['tendency']}")
print(f"Orientation: {orientation_0025}")
print(f"\nArchetype Ranking:")
for rank, (archetype, score) in enumerate(profile_0025['archetypeScores'], 1):
    print(f"  {rank}. {archetype}: {score}")
print(f"\nPurpose: Test radar chart rendering with extreme score variance (32 vs 8)")
print()

# Test code 0026: Balanced scores
scores_0026 = {
    'I': 24,
    'S': 18,
    'P': 33,
    'C': 20,
    'A': 20,
    'G': 18
}

profile_0026 = determine_profile(scores_0026)
orientation_0026 = calculate_orientation(profile_0026['code'])

print("=" * 70)
print("SECRET CODE 0026 - BALANCED SCORES TEST")
print("=" * 70)
print(f"Raw Scores: I={scores_0026['I']}, S={scores_0026['S']}, P={scores_0026['P']}, C={scores_0026['C']}, A={scores_0026['A']}, G={scores_0026['G']}")
print(f"Profile Code: {profile_0026['code']}")
print(f"Dominant Archetypes: {' & '.join(profile_0026['dominantArchetypes'])}")
print(f"Tendency: {profile_0026['tendency']}")
print(f"Orientation: {orientation_0026}")
print(f"\nArchetype Ranking:")
for rank, (archetype, score) in enumerate(profile_0026['archetypeScores'], 1):
    print(f"  {rank}. {archetype}: {score}")
print(f"\nPurpose: Test radar chart rendering with relatively balanced scores")
print()

# Summary
print("=" * 70)
print("IMPLEMENTATION NOTES")
print("=" * 70)
print(f"✓ Code 0025 should activate profile: {profile_0025['code']}")
print(f"✓ Code 0026 should activate profile: {profile_0026['code']}")
print()
print("Both profiles already exist in the system, so we can use:")
print("  Option A: Direct activation in secret code handler (recommended)")
print("  - Faster implementation")
print("  - No new profile data needed")
print("  - Uses existing activateProfile() function")
print()
