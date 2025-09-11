#!/usr/bin/env python3
"""
Find the syntax error causing the 'catch' token issue
"""

def find_syntax_error():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        lines = f.readlines()
    
    print("=== SYNTAX ERROR ANALYSIS ===\n")
    
    # Check around line 1785
    start = max(0, 1785 - 10)
    end = min(len(lines), 1785 + 10)
    
    print(f"Lines {start+1} to {end}:")
    for i in range(start, end):
        marker = " >>> " if i + 1 == 1785 else "     "
        print(f"{marker}{i+1:4d}: {lines[i].rstrip()}")
    
    # Look for unmatched braces or try/catch issues
    print("\n🔍 Checking for try/catch issues:")
    
    try_count = 0
    catch_count = 0
    
    for i, line in enumerate(lines, 1):
        if 'try {' in line:
            try_count += 1
            print(f"   Line {i}: Found 'try' block")
        elif 'catch' in line and 'function' not in line:
            catch_count += 1
            print(f"   Line {i}: Found 'catch' block")
            
            # Check if there's a proper try before this catch
            if i > 5:
                context = ''.join(lines[max(0, i-6):i])
                if 'try {' not in context:
                    print(f"   ❌ PROBLEM: 'catch' without matching 'try' at line {i}")
    
    print(f"\n📊 Summary: {try_count} try blocks, {catch_count} catch blocks")
    
    # Check for missing closing braces
    print("\n🔍 Checking brace balance around line 1785:")
    start_check = max(0, 1780)
    end_check = min(len(lines), 1790)
    
    brace_balance = 0
    for i in range(start_check, end_check):
        line = lines[i]
        brace_balance += line.count('{') - line.count('}')
        print(f"   Line {i+1}: balance = {brace_balance}, line = {line.strip()}")

if __name__ == "__main__":
    find_syntax_error()