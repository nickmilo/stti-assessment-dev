#!/usr/bin/env python3
"""
Clean main.js by removing duplicate hardcoded profile content.

The file currently has:
1. A proper setCollapsibleSections() that uses ProfileRenderer (lines 221-240)
2. Duplicate hardcoded profile blocks that should be deleted (lines 246-893)
3. A proper activateProfile() function (line 895+)

This script removes the duplicate hardcoded content between the two functions.
"""

def clean_main_js():
    input_file = '../Web-App/main.js'
    output_file = '../Web-App/main.js'

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Find the end of setCollapsibleSections (line with console.error and closing brace)
    # Find the start of the REAL activateProfile (line with "function activateProfile" followed by "try {")

    new_lines = []
    skip_mode = False
    line_num = 0

    for i, line in enumerate(lines, start=1):
        # When we hit the error line after setCollapsibleSections
        if 'console.error(`❌ setCollapsibleSections: ProfileRenderer failed' in line:
            new_lines.append(line)
            # Next line should be the closing brace for setCollapsibleSections
            if i < len(lines) and lines[i].strip() == '}':
                new_lines.append(lines[i])
                skip_mode = True  # Start skipping old hardcoded content
                line_num = i + 1
                continue

        # When we hit the REAL activateProfile with "try {" nearby
        elif skip_mode and 'function activateProfile(code, name)' in line:
            # Check if next couple lines have "try {"
            next_lines = ''.join(lines[i:min(i+3, len(lines))])
            if 'try {' in next_lines:
                skip_mode = False  # Stop skipping
                new_lines.append(line)  # Include this line
            continue

        # Normal mode - add line
        if not skip_mode:
            new_lines.append(line)

    # Write cleaned file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print(f"✅ Cleaned main.js")
    print(f"   Original: {len(lines)} lines")
    print(f"   Cleaned:  {len(new_lines)} lines")
    print(f"   Removed:  {len(lines) - len(new_lines)} lines")

if __name__ == '__main__':
    clean_main_js()
