#!/usr/bin/env python3
"""
Check syntax around PS-Architect implementation
"""

def check_syntax_around_ps():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== SYNTAX CHECK AROUND PS-ARCHITECT ===\n")
    
    # Overall balance check
    open_braces = content.count('{')
    close_braces = content.count('}')
    open_parens = content.count('(')
    close_parens = content.count(')')
    
    print(f"Overall balance:")
    print(f"  Braces: {open_braces} open, {close_braces} close (diff: {open_braces - close_braces})")
    print(f"  Parens: {open_parens} open, {close_parens} close (diff: {open_parens - close_parens})")
    
    # Find PS-Architect and surrounding context
    ps_start = content.find("code === 'PS-Architect'")
    if ps_start != -1:
        # Get line number
        line_num = content[:ps_start].count('\n') + 1
        print(f"\nPS-Architect found at line {line_num}")
        
        # Get surrounding lines
        lines = content.split('\n')
        start_line = max(0, line_num - 10)
        end_line = min(len(lines), line_num + 20)
        
        print(f"\nContext around PS-Architect (lines {start_line+1}-{end_line}):")
        for i in range(start_line, end_line):
            marker = " >>> " if i == line_num - 1 else "     "
            print(f"{marker}{i+1:4d}: {lines[i]}")
            
            # Check this specific line for issues
            line = lines[i]
            if i >= line_num - 1 and i <= line_num + 15:  # Around PS-Architect
                # Count quotes in line
                single_quotes = line.count("'")
                double_quotes = line.count('"')
                
                if single_quotes % 2 != 0:
                    print(f"      ⚠️  Odd number of single quotes: {single_quotes}")
                if double_quotes % 2 != 0:
                    print(f"      ⚠️  Odd number of double quotes: {double_quotes}")
                
                # Check for unbalanced braces on this line
                line_open = line.count('{')
                line_close = line.count('}')
                if line_open != line_close and (line_open > 0 or line_close > 0):
                    print(f"      ⚠️  Unbalanced braces: {line_open} open, {line_close} close")
    
    # Check if there are any unclosed string literals
    print(f"\n🔍 Checking for unclosed strings near PS-Architect:")
    
    # Simple check for common string errors
    lines = content.split('\n')
    for i in range(max(0, line_num - 5), min(len(lines), line_num + 15)):
        line = lines[i].strip()
        if "innerHTML =" in line and line.count("'") % 2 != 0:
            print(f"  Line {i+1}: Potential unclosed string - {line}")

if __name__ == "__main__":
    check_syntax_around_ps()