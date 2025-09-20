#!/usr/bin/env python3
"""
Debug the JavaScript syntax error with setTendencyPills
"""

def debug_javascript_error():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== JAVASCRIPT ERROR DEBUGGING ===\n")
    
    # Find the setTendencyPills function
    if 'function setTendencyPills' in content:
        print("✅ setTendencyPills function found")
        
        # Find where it's defined
        start = content.find('function setTendencyPills')
        end = content.find('        }', start) + 9
        function_code = content[start:end]
        
        print("📋 Function definition:")
        print(function_code[:200] + "..." if len(function_code) > 200 else function_code)
        
    else:
        print("❌ setTendencyPills function NOT found")
    
    # Check for syntax issues around function definitions
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'setTendencyPills' in line:
            print(f"Line {i}: {line.strip()}")
    
    # Check for missing closing braces or parentheses
    brace_count = content.count('{') - content.count('}')
    paren_count = content.count('(') - content.count(')')
    
    print(f"\n📊 Syntax check:")
    print(f"   Brace balance: {brace_count} (should be 0)")
    print(f"   Parentheses balance: {paren_count} (should be 0)")
    
    # Look for the activateProfile call
    if 'setTendencyPills(code)' in content:
        print("✅ setTendencyPills(code) call found in activateProfile")
    else:
        print("❌ setTendencyPills(code) call NOT found")

if __name__ == "__main__":
    debug_javascript_error()