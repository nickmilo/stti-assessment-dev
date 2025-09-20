#!/usr/bin/env python3
"""
Analyze westerner CSS classes that need to be changed to orientation
Following SOP Tenet #2: Use Python to understand structure completely
Following SOP Tenet #1: Understand what we're changing completely
"""

def analyze_westerner_css_classes():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING WESTERNER CSS CLASSES FOR SAFE RENAME ===")
    print("Target: Change westerner-* classes to orientation-* classes\n")
    
    lines = content.split('\n')
    
    # 1. Find all westerner-related CSS classes in HTML
    print("🔍 FINDING ALL WESTERNER CSS CLASSES IN HTML:")
    westerner_classes_html = []
    
    for i, line in enumerate(lines, 1):
        # Look for class="..." with westerner in it
        if 'westerner-' in line and 'class=' in line:
            westerner_classes_html.append((i, line.strip()))
    
    print(f"Found {len(westerner_classes_html)} HTML elements with westerner classes:")
    for line_num, line_content in westerner_classes_html:
        print(f"  Line {line_num}: {line_content}")
    
    # 2. Find all westerner CSS style definitions
    print(f"\n🔍 FINDING ALL WESTERNER CSS STYLE DEFINITIONS:")
    westerner_css_styles = []
    in_style_block = False
    
    for i, line in enumerate(lines, 1):
        if '<style>' in line:
            in_style_block = True
        elif '</style>' in line:
            in_style_block = False
        elif in_style_block and '.westerner-' in line:
            westerner_css_styles.append((i, line.strip()))
    
    print(f"Found {len(westerner_css_styles)} CSS style definitions:")
    for line_num, line_content in westerner_css_styles:
        print(f"  Line {line_num}: {line_content}")
    
    # 3. Find all JavaScript references to westerner classes
    print(f"\n🔍 FINDING ALL JAVASCRIPT REFERENCES TO WESTERNER CLASSES:")
    westerner_js_refs = []
    
    for i, line in enumerate(lines, 1):
        # Look for getElementById, querySelector, etc. with westerner
        if ('getElementById(' in line or 'querySelector(' in line) and 'westerner' in line:
            westerner_js_refs.append((i, line.strip()))
    
    print(f"Found {len(westerner_js_refs)} JavaScript references:")
    for line_num, line_content in westerner_js_refs:
        print(f"  Line {line_num}: {line_content}")
    
    # 4. Extract the specific classes that need changing
    print(f"\n📋 CLASSES THAT NEED CHANGING:")
    classes_to_change = set()
    
    # From HTML
    for line_num, line_content in westerner_classes_html:
        import re
        # Extract westerner-* class names
        matches = re.findall(r'westerner-[\w-]+', line_content)
        for match in matches:
            classes_to_change.add(match)
    
    # From CSS
    for line_num, line_content in westerner_css_styles:
        import re
        # Extract .westerner-* class names
        matches = re.findall(r'\.westerner-[\w-]+', line_content)
        for match in matches:
            classes_to_change.add(match.replace('.', ''))  # Remove the dot
    
    print("Classes to rename:")
    for class_name in sorted(classes_to_change):
        new_name = class_name.replace('westerner-', 'orientation-')
        print(f"  {class_name} → {new_name}")
    
    # 5. Check for any IDs that need changing
    print(f"\n🔍 CHECKING FOR WESTERNER IDS:")
    westerner_ids = []
    
    for i, line in enumerate(lines, 1):
        if 'id=' in line and 'westerner' in line:
            westerner_ids.append((i, line.strip()))
    
    if westerner_ids:
        print(f"Found {len(westerner_ids)} IDs with westerner:")
        for line_num, line_content in westerner_ids:
            print(f"  Line {line_num}: {line_content}")
    else:
        print("✅ No westerner IDs found (already changed)")
    
    # 6. Safety check - make sure we understand dependencies
    print(f"\n🔍 SAFETY CHECK - DEPENDENCIES:")
    
    # Check if any external CSS or JS might depend on these classes
    external_deps = []
    for i, line in enumerate(lines, 1):
        if ('<link' in line and 'stylesheet' in line) or ('<script' in line and 'src=' in line):
            external_deps.append((i, line.strip()))
    
    if external_deps:
        print(f"⚠️  Found {len(external_deps)} external dependencies to review:")
        for line_num, line_content in external_deps:
            print(f"  Line {line_num}: {line_content}")
        print("  Make sure these don't reference westerner classes!")
    else:
        print("✅ No external CSS/JS dependencies found")
    
    # 7. Create change plan
    print(f"\n🔧 SAFE CHANGE PLAN:")
    print("1. Change CSS style definitions (.westerner-* → .orientation-*)")
    print("2. Change HTML class attributes (class=\"westerner-*\" → class=\"orientation-*\")")  
    print("3. Change any remaining JavaScript references")
    print("4. Verify no functionality breaks")
    
    print(f"\n⚠️  RISK ASSESSMENT:")
    print("- LOW RISK: These appear to be styling/layout classes")
    print("- MEDIUM RISK: Need to ensure all references are updated consistently")  
    print("- HIGH RISK: If external dependencies exist (check above)")
    
    return classes_to_change, westerner_css_styles, westerner_classes_html, westerner_js_refs

if __name__ == "__main__":
    analyze_westerner_css_classes()