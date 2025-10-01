#!/usr/bin/env python3
"""
Fix secret codes in Master Content to match main.js mapping
"""

# Correct mapping from main.js (lines 86-157)
PROFILE_CODES = {
    '0001': 'IP-Architect',
    '0002': 'IP-Gardener',
    '0003': 'IS-Architect',
    '0004': 'IS-Gardener',
    '0005': 'IC-Architect',     # Note: Was CP in my original mapping
    '0006': 'IC-Gardener',
    '0007': 'PI-Architect',     # Note: Was CS in my original mapping
    '0008': 'PI-Gardener',
    '0009': 'PS-Architect',
    '0010': 'PS-Gardener',
    '0011': 'PC-Architect',     # Note: Was CI in my original mapping
    '0012': 'PC-Gardener',
    '0013': 'SI-Architect',     # Note: Was IC in my original mapping
    '0014': 'SI-Gardener',
    '0015': 'SP-Architect',     # Note: Was PC in my original mapping
    '0016': 'SP-Gardener',
    '0017': 'SC-Architect',
    '0018': 'SC-Gardener',
    '0019': 'CI-Architect',     # Note: Was SP in my original mapping
    '0020': 'CI-Gardener',
    '0021': 'CP-Architect',     # Note: Was SI in my original mapping
    '0022': 'CP-Gardener',
    '0023': 'CS-Architect',     # Note: Was PI in my original mapping
    '0024': 'CS-Gardener',
}

# Reverse mapping
CODE_BY_PROFILE = {profile: code for code, profile in PROFILE_CODES.items()}

def fix_secret_codes():
    input_file = '../STTI Profiles Master Content.md'

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for i, line in enumerate(lines):
        # Check if this is a profile header
        if line.startswith('## ') and '(' in line:
            # Extract profile name (e.g., "IP-Architect" from "## IP-Architect (Inner Guide + Producer, Architect Tendency)")
            profile_name = line.split('(')[0].replace('##', '').strip()

            if profile_name in CODE_BY_PROFILE:
                new_lines.append(line)

                # Check if next line is a comment
                if i + 1 < len(lines) and '[comment]: #' in lines[i + 1]:
                    # Replace with correct code
                    correct_code = CODE_BY_PROFILE[profile_name]
                    new_lines.append(f'[comment]: # (Secret Code: {correct_code})\n')
                    # Skip the old comment line
                    continue
                else:
                    # Add comment if it doesn't exist
                    correct_code = CODE_BY_PROFILE[profile_name]
                    new_lines.append(f'[comment]: # (Secret Code: {correct_code})\n')
            else:
                new_lines.append(line)
        elif '[comment]: #' in line and i > 0 and lines[i-1].startswith('##'):
            # Skip - already handled above
            continue
        else:
            new_lines.append(line)

    # Write back
    with open(input_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"✅ Fixed secret codes in Master Content.md to match main.js mapping")
    print(f"   All 24 profiles now have correct codes matching the secret code handler")

if __name__ == '__main__':
    fix_secret_codes()
