#!/usr/bin/env python3
"""
Find button color styles for assessment answers
Following SOP Tenet #2: Use Python to understand structure
Following SOP Tenet #4: Make surgical change
"""

def find_button_styles():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FINDING BUTTON COLOR STYLES ===")
    print("Need to change Disagree from yellow to cyan-teal")
    print("Need to change Strongly Disagree to pink\n")
    
    lines = content.split('\n')
    
    # Find CSS styles for answer buttons
    print("🔍 SEARCHING FOR BUTTON STYLES:")
    
    button_styles = []
    in_style = False
    style_start = None
    
    for i, line in enumerate(lines, 1):
        if '<style>' in line:
            in_style = True
            style_start = i
        elif '</style>' in line:
            in_style = False
        elif in_style:
            # Look for button-related styles
            if any(keyword in line.lower() for keyword in ['btn', 'button', 'answer', 'yellow', 'cyan', 'pink', 'disagree', 'agree']):
                if 'background' in line or 'color:' in line or '--lyt' in line:
                    button_styles.append((i, line.strip()))
    
    print("Found button-related styles:")
    for line_num, style in button_styles:
        print(f"  Line {line_num}: {style}")
    
    # Look specifically for answer button classes
    print(f"\n🔍 SEARCHING FOR ANSWER BUTTON CLASSES:")
    
    answer_btn_styles = []
    for i, line in enumerate(lines, 1):
        if '.answer-btn' in line:
            # Capture this line and next few lines
            for j in range(i, min(i + 10, len(lines) + 1)):
                if j <= len(lines):
                    answer_btn_styles.append((j, lines[j - 1].strip()))
    
    if answer_btn_styles:
        print("Found .answer-btn styles:")
        current_section = None
        for line_num, style in answer_btn_styles:
            if '.answer-btn' in style:
                current_section = style
                print(f"\n  {current_section}")
            else:
                print(f"    Line {line_num}: {style}")
    
    # Find the actual button HTML to see class names
    print(f"\n🔍 SEARCHING FOR BUTTON HTML:")
    
    button_html = []
    for i, line in enumerate(lines, 1):
        if 'onclick="selectAnswer' in line and 'button' in line:
            button_html.append((i, line.strip()))
    
    if button_html:
        print("Found answer button HTML:")
        for line_num, html in button_html[:4]:  # Show first 4
            print(f"  Line {line_num}: {html[:100]}...")
    
    # Look for CSS variables
    print(f"\n🔍 CSS COLOR VARIABLES:")
    
    color_vars = []
    for i, line in enumerate(lines, 1):
        if '--lyt-' in line and ':' in line and '#' in line:
            color_vars.append((i, line.strip()))
    
    if color_vars:
        print("Found color variables:")
        for line_num, var in color_vars:
            print(f"  Line {line_num}: {var}")
    
    print(f"\n📋 SOLUTION:")
    print("1. Find .answer-btn styles for SD, D, A, SA")
    print("2. Change D (Disagree) from yellow to cyan (same as A)")
    print("3. Change SD (Strongly Disagree) to pink (same as SA)")
    print("4. This creates color symmetry and removes bias")

if __name__ == "__main__":
    find_button_styles()