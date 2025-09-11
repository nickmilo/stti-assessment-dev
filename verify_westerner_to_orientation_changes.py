#!/usr/bin/env python3
"""
Verify all westernerDescription -> orientationDescription changes were made correctly
Following SOP Tenet #2: Use Python to understand structure completely
"""

def verify_changes():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== VERIFYING WESTERNER -> ORIENTATION CHANGES ===")
    
    lines = content.split('\n')
    
    # 1. Check for any remaining westernerDescription references
    print("🔍 CHECKING FOR OLD REFERENCES:")
    old_refs_found = []
    
    for i, line in enumerate(lines, 1):
        if 'westernerDescription' in line:
            old_refs_found.append((i, line.strip()))
    
    if old_refs_found:
        print("❌ OLD REFERENCES STILL EXIST:")
        for line_num, line_content in old_refs_found:
            print(f"  Line {line_num}: {line_content}")
    else:
        print("✅ No old 'westernerDescription' references found")
    
    # 2. Verify new orientationDescription references
    print("\n🔍 CHECKING FOR NEW REFERENCES:")
    new_refs_found = []
    
    for i, line in enumerate(lines, 1):
        if 'orientationDescription' in line:
            new_refs_found.append((i, line.strip()))
    
    if new_refs_found:
        print(f"✅ Found {len(new_refs_found)} 'orientationDescription' references:")
        for line_num, line_content in new_refs_found:
            # Truncate long lines for readability
            display_content = line_content[:80] + "..." if len(line_content) > 80 else line_content
            print(f"  Line {line_num}: {display_content}")
    else:
        print("❌ No new 'orientationDescription' references found")
    
    # 3. Check HTML element ID was changed
    print("\n🔍 CHECKING HTML ELEMENT ID:")
    html_element_found = False
    
    for i, line in enumerate(lines, 1):
        if 'id="orientationDescription"' in line:
            html_element_found = True
            print(f"✅ HTML element ID updated at line {i}: {line.strip()}")
            break
        elif 'id="westernerDescription"' in line:
            print(f"❌ Old HTML element ID still exists at line {i}: {line.strip()}")
    
    if not html_element_found and 'id="westernerDescription"' not in content:
        print("⚠️  Could not find HTML element with either ID")
    
    # 4. Summary
    print(f"\n📋 SUMMARY:")
    print(f"- Old references remaining: {len(old_refs_found)}")
    print(f"- New references found: {len(new_refs_found)}")
    print(f"- HTML element ID updated: {'✅' if html_element_found else '❌'}")
    
    # 5. Expected count verification
    expected_js_refs = 14  # Based on grep output before changes
    expected_html_refs = 1  # The HTML element ID
    total_expected = expected_js_refs + expected_html_refs
    
    print(f"\n🎯 EXPECTED VS ACTUAL:")
    print(f"- Expected total references: {total_expected}")
    print(f"- Actual references found: {len(new_refs_found)}")
    
    if len(new_refs_found) == total_expected:
        print("✅ Reference count matches expected")
    else:
        print(f"⚠️  Reference count mismatch (expected {total_expected}, found {len(new_refs_found)})")
    
    # 6. Final verdict
    success = (
        len(old_refs_found) == 0 and 
        len(new_refs_found) > 0 and 
        html_element_found
    )
    
    print(f"\n🏆 FINAL VERDICT: {'✅ ALL CHANGES VERIFIED SUCCESSFULLY' if success else '❌ ISSUES FOUND - CHANGES INCOMPLETE'}")
    
    return success

if __name__ == "__main__":
    verify_changes()