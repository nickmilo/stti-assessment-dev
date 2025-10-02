import json

with open('/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/Web-App/profiles.json', 'r') as f:
    data = json.load(f)

print("Profile Completeness Analysis:")
print("=" * 80)

for code in sorted(data.keys()):
    profile = data[code]
    sections = []

    if 'archetypeDescription' in profile:
        sections.append('archetypeDesc')
    if 'orientationDescription' in profile:
        sections.append('orientationDesc')
    if 'tendencyDescription' in profile:
        sections.append('tendencyDesc')
    if 'overwhelmed' in profile:
        sections.append('overwhelmed')
    if 'stuckUnstuck' in profile:
        sections.append('stuckUnstuck')
    if 'prompts' in profile:
        sections.append('prompts')
    if 'archetypesSynergy' in profile:
        sections.append('synergy')

    section_count = len(sections)
    status = "COMPLETE (7/7)" if section_count == 7 else f"INCOMPLETE ({section_count}/7)"

    print(f"{code:15s} {status:20s} {', '.join(sections)}")
