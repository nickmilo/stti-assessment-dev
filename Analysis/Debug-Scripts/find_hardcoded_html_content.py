#!/usr/bin/env python3
"""
Find hardcoded IS-Architect content in HTML that overrides setCollapsibleSections
Following SOP Tenet #2: Use Python to understand structure completely
"""

def find_hardcoded_html():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FINDING HARDCODED HTML CONTENT ===")
    print("SP-Architect showing IS-Architect content - checking lines 1265-1290\n")
    
    lines = content.split('\n')
    
    # 1. Check lines 1265-1290 for hardcoded content
    print("🔍 EXAMINING LINES 1265-1290:")
    for i in range(1264, 1295):
        if i < len(lines):
            line = lines[i]
            if any(text in line for text in ['overwhelmed', 'stuck', 'prompt', 'IS-Architect', 'Westerner']):
                print(f"  Line {i + 1}: {line.strip()}")
    
    # 2. Find the HTML structure for collapsible sections
    print(f"\n🔍 COLLAPSIBLE SECTION HTML STRUCTURE:")
    
    section_ids = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection']
    
    for section_id in section_ids:
        for i, line in enumerate(lines, 1):
            if f'id="{section_id}"' in line:
                print(f"\n{section_id} found at line {i}:")
                # Show this line and next few lines
                for j in range(i - 1, min(i + 15, len(lines))):
                    if j >= 0:
                        content_line = lines[j]
                        if any(text in content_line for text in ['section-title', 'section-content', '</div>']):
                            print(f"    Line {j + 1}: {content_line.strip()}")
    
    # 3. Check setCollapsibleSections function for comparison
    print(f"\n🔍 SETCOLLAPSIBLESECTIONS FUNCTION:")
    
    setcollapsible_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            setcollapsible_start = i
            print(f"setCollapsibleSections starts at line {i}")
            break
    
    # 4. Show the issue
    print(f"\n📋 THE ISSUE:")
    print("HTML (lines 1265-1290) has hardcoded IS-Architect text:")
    print("- 'When Westerners feel overwhelmed...'")
    print("- 'Getting stuck and unstuck as an IS-Architect'")
    print("- 'Prompts to go from West to East as an IS-Architect'")
    print("\nThis HTML content is what initially loads in the browser.")
    print("setCollapsibleSections() tries to replace it, but if there's an error")
    print("or timing issue, the hardcoded content shows instead.")
    
    print(f"\n🔧 SOLUTION:")
    print("Replace hardcoded IS-Architect content in HTML with generic placeholders:")
    print("- 'When [Profile]s feel overwhelmed...' or 'Loading...'")
    print("- 'Getting stuck and unstuck as [Profile]'")
    print("- 'Prompts for [Profile]'")
    print("This ensures the HTML is neutral until JavaScript sets the correct content.")

if __name__ == "__main__":
    find_hardcoded_html()