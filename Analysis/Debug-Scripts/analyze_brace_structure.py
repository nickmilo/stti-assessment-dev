#!/usr/bin/env python3
"""
Analyze the brace structure around setCollapsibleSections more carefully
Following SOP Tenet #2: Use Python to understand structure completely
"""

def analyze_brace_structure():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING BRACE STRUCTURE IN SETCOLLAPSIBLESECTIONS ===")
    
    lines = content.split('\n')
    
    # Find function boundaries
    func_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            func_start = i
            break
    
    print(f"Function starts at line {func_start}")
    
    # Analyze brace structure around the suspected problem areas
    problem_areas = [
        ("SC-Architect end", 2114),
        ("SC-Gardener end", 2141), 
        ("Suspected problem", 2168),
        ("SP-Architect start", 2170)
    ]
    
    for area_name, line_num in problem_areas:
        print(f"\n🔍 {area_name.upper()} (around line {line_num}):")
        
        start = max(0, line_num - 5)
        end = min(len(lines), line_num + 5)
        
        brace_balance = 0
        for i in range(start, end):
            if i < len(lines):
                line = lines[i]
                # Count braces on this line
                opens = line.count('{')
                closes = line.count('}')
                brace_balance += opens - closes
                
                marker = ">>> " if i + 1 == line_num else "    "
                balance_str = f" [balance: {brace_balance:+d}]" if opens or closes else ""
                print(f"{marker}Line {i + 1}: {line.strip()}{balance_str}")
    
    # Let's trace the actual brace nesting level through the function
    print(f"\n🔍 BRACE BALANCE THROUGH ENTIRE FUNCTION:")
    
    brace_level = 0
    function_ended = False
    
    for i in range(func_start - 1, min(func_start + 700, len(lines))):
        line = lines[i]
        
        # Skip empty lines and comments for clarity
        if not line.strip() or line.strip().startswith('//'):
            continue
            
        # Track brace level
        prev_level = brace_level
        brace_level += line.count('{') - line.count('}')
        
        # Important lines to show
        show_line = False
        if 'function setCollapsibleSections' in line:
            show_line = True
        elif 'if (code ===' in line and any(profile in line for profile in ['SC-Architect', 'SC-Gardener', 'SP-Architect']):
            show_line = True
        elif 'return;' in line and 'Exit early' in line:
            show_line = True
        elif '}' in line and (prev_level == 1 and brace_level == 0):
            show_line = True
            if not function_ended:
                print(f"    Line {i + 1}: {line.strip()} [FUNCTION ENDS HERE - brace level: {brace_level}]")
                function_ended = True
                continue
        elif function_ended and 'if (code ===' in line:
            print(f"    Line {i + 1}: {line.strip()} [OUTSIDE FUNCTION - brace level: {brace_level}]")
            continue
            
        if show_line:
            level_str = f" [brace level: {brace_level}]"
            print(f"    Line {i + 1}: {line.strip()}{level_str}")

if __name__ == "__main__":
    analyze_brace_structure()