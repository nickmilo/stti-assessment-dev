#!/usr/bin/env python3
"""
Test JavaScript syntax validation after IP profiles addition
Following tenet #3: Always validate syntax after modifications
"""

def test_syntax_validation():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== SYNTAX VALIDATION ===\n")
    
    # Basic syntax checks
    open_braces = content.count('{')
    close_braces = content.count('}')
    open_parens = content.count('(')
    close_parens = content.count(')')
    
    print("📊 Brace and parentheses balance:")
    print(f"   Open braces: {open_braces}")
    print(f"   Close braces: {close_braces}")
    print(f"   Balance: {open_braces - close_braces} (should be 0)")
    print(f"   Open parens: {open_parens}")
    print(f"   Close parens: {close_parens}")
    print(f"   Balance: {open_parens - close_parens} (should be 0)")
    
    # Check for try/catch balance
    try_count = content.count('try {')
    catch_count = content.count('} catch (')
    print(f"\n📊 Try/catch balance:")
    print(f"   Try blocks: {try_count}")
    print(f"   Catch blocks: {catch_count}")
    print(f"   Balance: {try_count - catch_count} (should be 0)")
    
    # Check for IP profile additions
    print(f"\n✅ IP Profile checks:")
    if "code === 'IP-Architect'" in content:
        print("   ✅ IP-Architect code found")
    if "code === 'IP-Gardener'" in content:
        print("   ✅ IP-Gardener code found")
    
    # Check for potential syntax issues around IP additions
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'IP-Architect' in line or 'IP-Gardener' in line:
            # Check surrounding lines for syntax issues
            start = max(0, i-3)
            end = min(len(lines), i+3)
            
            print(f"\n🔍 Context around line {i} (IP profile logic):")
            for j in range(start, end):
                marker = " >>> " if j+1 == i else "     "
                print(f"{marker}{j+1:4d}: {lines[j]}")
            break
    
    # Final validation
    if open_braces == close_braces and open_parens == close_parens and try_count == catch_count:
        print(f"\n✅ SYNTAX APPEARS VALID - Safe to test")
    else:
        print(f"\n❌ SYNTAX ISSUES DETECTED - Fix before testing")

if __name__ == "__main__":
    test_syntax_validation()