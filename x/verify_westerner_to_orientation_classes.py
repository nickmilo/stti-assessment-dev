#!/usr/bin/env python3
"""
Verify westerner→orientation class changes completed successfully
Following SOP Tenet #2: Use Python to understand structure completely
"""

def verify_class_changes():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== VERIFYING WESTERNER → ORIENTATION CLASS CHANGES ===")
    
    lines = content.split('\n')
    
    # 1. Check for remaining westerner references (should be minimal)
    remaining_westerner = []
    for i, line in enumerate(lines, 1):
        if 'westerner' in line.lower() and 'orientation' not in line:
            # Filter out comments and expected cases
            if not (line.strip().startswith('//') or line.strip().startswith('*')):
                remaining_westerner.append((i, line.strip()))
    
    print(f"🔍 REMAINING WESTERNER REFERENCES:")
    if remaining_westerner:
        print(f"Found {len(remaining_westerner)} remaining references:")
        for line_num, line_content in remaining_westerner:
            print(f"  Line {line_num}: {line_content[:80]}...")
    else:
        print("✅ No problematic westerner references found")
    
    # 2. Verify new orientation references
    orientation_refs = []
    for i, line in enumerate(lines, 1):
        if 'orientation-' in line or ('orientation' in line and ('Title' in line or 'Subtitle' in line or 'Description' in line)):
            orientation_refs.append((i, line.strip()))
    
    print(f"\n🔍 NEW ORIENTATION REFERENCES:")
    print(f"Found {len(orientation_refs)} orientation references:")
    for line_num, line_content in orientation_refs:
        display = line_content[:80] + "..." if len(line_content) > 80 else line_content
        print(f"  Line {line_num}: {display}")
    
    # 3. Check CSS class consistency
    css_classes = set()
    html_classes = set()
    
    # Find CSS definitions
    in_style = False
    for line in lines:
        if '<style>' in line:
            in_style = True
        elif '</style>' in line:
            in_style = False
        elif in_style and '.orientation-' in line:
            import re
            matches = re.findall(r'\.orientation-[\w-]+', line)
            for match in matches:
                css_classes.add(match.replace('.', ''))
    
    # Find HTML usage
    for line in lines:
        if 'class=' in line and 'orientation-' in line:
            import re
            # Extract class names from class="..." 
            class_matches = re.findall(r'class="([^"]*)"', line)
            for classes in class_matches:
                for class_name in classes.split():
                    if 'orientation-' in class_name:
                        html_classes.add(class_name)
    
    print(f"\n🔍 CSS/HTML CLASS CONSISTENCY CHECK:")
    print(f"CSS classes defined: {sorted(css_classes)}")
    print(f"HTML classes used: {sorted(html_classes)}")
    
    # Check for mismatches
    css_only = css_classes - html_classes
    html_only = html_classes - css_classes
    
    if css_only:
        print(f"⚠️  CSS classes not used in HTML: {css_only}")
    if html_only:
        print(f"⚠️  HTML classes not defined in CSS: {html_only}")
    if not css_only and not html_only:
        print("✅ All classes are consistently defined and used")
    
    # 4. Final verdict
    print(f"\n🏆 FINAL VERDICT:")
    issues = len(remaining_westerner) + len(css_only) + len(html_only)
    if issues == 0:
        print("✅ ALL WESTERNER → ORIENTATION CHANGES COMPLETED SUCCESSFULLY")
        print("✅ No inconsistencies found")
        print("✅ Ready for testing")
    else:
        print(f"⚠️  {issues} issues found - review needed")

if __name__ == "__main__":
    verify_class_changes()