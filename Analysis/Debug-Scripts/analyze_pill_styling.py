#!/usr/bin/env python3
"""
Analyze pill styling structure before fixing Gardener pill styling
Following tenet #2: Re-familiarize with code structure
"""

def analyze_pill_styling():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== PILL STYLING ANALYSIS ===\n")
    
    # 1. Find CSS classes for tendency pills
    print("🎨 CSS classes for tendency pills:")
    css_classes = [
        '.architect-pill',
        '.gardener-pill',
        '.tendency-pill'
    ]
    
    for css_class in css_classes:
        if css_class in content:
            start = content.find(css_class)
            end = content.find('}', start) + 1
            css_block = content[start:end]
            print(f"   ✅ Found {css_class}:")
            print(f"      {css_block}")
        else:
            print(f"   ❌ Missing {css_class}")
    
    # 2. Check how pills are assigned classes in JavaScript
    print(f"\n📋 JavaScript class assignments:")
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'gardener-pill' in line or 'architect-pill' in line:
            print(f"   Line {i}: {line.strip()}")
    
    # 3. Check setTendencyPills function specifically
    print(f"\n🔍 setTendencyPills function analysis:")
    start = content.find('function setTendencyPills(code) {')
    if start != -1:
        end = content.find('        }', start) + 9
        function_code = content[start:end]
        print(f"   Function found, checking class assignments...")
        
        if 'gardener-pill' in function_code:
            print(f"   ✅ gardener-pill class referenced in setTendencyPills")
        else:
            print(f"   ❌ gardener-pill class NOT referenced in setTendencyPills")
            
        if 'architect-pill' in function_code:
            print(f"   ✅ architect-pill class referenced in setTendencyPills")
        else:
            print(f"   ❌ architect-pill class NOT referenced in setTendencyPills")
    
    # 4. Check the specific assignment logic
    print(f"\n🔍 Tendency assignment logic:")
    if '${tendency.toLowerCase()}-pill' in content:
        print(f"   ✅ Uses dynamic class assignment: ${tendency.toLowerCase()}-pill")
    if 'tendency === \'Architect\' ? \'architect-pill\' : \'gardener-pill\'' in content:
        print(f"   ✅ Uses ternary operator for class assignment")
    
    print(f"\n💡 DIAGNOSIS:")
    print("   - Check if CSS .gardener-pill class exists and has proper styling")
    print("   - Verify JavaScript assigns 'gardener-pill' class correctly")
    print("   - Ensure no conflicts in class assignment logic")

if __name__ == "__main__":
    analyze_pill_styling()