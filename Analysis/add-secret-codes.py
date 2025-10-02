#!/usr/bin/env python3
"""
Add secret codes as markdown comments to STTI Profiles Master Content.md
"""

# Map profile names to secret codes (from main.js secret code handler)
PROFILE_CODES = {
    'IP-Architect': '0001',
    'IP-Gardener': '0002',
    'IS-Architect': '0003',
    'IS-Gardener': '0004',
    'CP-Architect': '0005',
    'CP-Gardener': '0006',
    'CS-Architect': '0007',
    'CS-Gardener': '0008',
    'PS-Architect': '0009',
    'PS-Gardener': '0010',
    'CI-Architect': '0011',
    'CI-Gardener': '0012',
    'IC-Architect': '0013',
    'IC-Gardener': '0014',
    'PC-Architect': '0015',
    'PC-Gardener': '0016',
    'SC-Architect': '0017',
    'SC-Gardener': '0018',
    'SP-Architect': '0019',
    'SP-Gardener': '0020',
    'SI-Architect': '0021',
    'SI-Gardener': '0022',
    'PI-Architect': '0023',
    'PI-Gardener': '0024',
}

def add_secret_codes():
    input_file = '../STTI Profiles Master Content.md'

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add secret codes to each profile header
    for profile_name, code in PROFILE_CODES.items():
        # Find the profile header
        header_pattern = f'## {profile_name} ('
        comment_line = f'[comment]: # (Secret Code: {code})'

        # Check if code already exists for this profile
        if f'## {profile_name}' in content:
            # Split content to find the header
            lines = content.split('\n')
            new_lines = []
            i = 0
            while i < len(lines):
                line = lines[i]
                new_lines.append(line)

                # If this is the profile header, add comment on next line (if not already there)
                if line.startswith(f'## {profile_name} ('):
                    # Check if next line is already a comment
                    if i + 1 < len(lines) and '[comment]: #' not in lines[i + 1]:
                        new_lines.append(comment_line)

                i += 1

            content = '\n'.join(new_lines)

    # Write back
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"✅ Added secret codes to all 24 profiles in Master Content.md")
    print(f"   Codes are hidden as markdown comments: [comment]: # (Secret Code: XXXX)")

if __name__ == '__main__':
    add_secret_codes()
