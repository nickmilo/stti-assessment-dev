#!/usr/bin/env python3
"""
Find exact location of unmatched quotes in SP-Architect case
Following SOP Tenet #2: Use Python to understand structure completely
"""

def find_quote_mismatch():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== FINDING UNMATCHED QUOTES IN SP-ARCHITECT CASE ===")
    
    lines = content.split('\n')
    
    # Extract SP-Architect case (lines 2170-2331)
    sp_start = 2170 - 1  # 0-indexed
    sp_end = 2331 - 1    # 0-indexed
    
    print(f"Analyzing SP-Architect case: lines {sp_start + 1} to {sp_end + 1}")
    
    quote_issues = []
    
    for i in range(sp_start, min(sp_end + 1, len(lines))):
        line = lines[i]
        line_num = i + 1
        
        # Count quotes carefully, handling escaped quotes
        single_quote_count = 0
        double_quote_count = 0
        
        j = 0
        while j < len(line):
            char = line[j]
            
            if char == "'":
                # Check if it's escaped
                if j > 0 and line[j-1] == '\\':
                    # Check if the backslash itself is escaped
                    backslash_count = 0
                    k = j - 1
                    while k >= 0 and line[k] == '\\':
                        backslash_count += 1
                        k -= 1
                    # If odd number of backslashes, the quote is escaped
                    if backslash_count % 2 == 0:
                        single_quote_count += 1
                else:
                    single_quote_count += 1
                    
            elif char == '"':
                # Check if it's escaped
                if j > 0 and line[j-1] == '\\':
                    # Check if the backslash itself is escaped
                    backslash_count = 0
                    k = j - 1
                    while k >= 0 and line[k] == '\\':
                        backslash_count += 1
                        k -= 1
                    # If odd number of backslashes, the quote is escaped
                    if backslash_count % 2 == 0:
                        double_quote_count += 1
                else:
                    double_quote_count += 1
            
            j += 1
        
        # Check for unmatched quotes on this line
        if single_quote_count % 2 != 0:
            quote_issues.append((line_num, 'single', single_quote_count, line.strip()))
        
        if double_quote_count % 2 != 0:
            quote_issues.append((line_num, 'double', double_quote_count, line.strip()))
    
    if quote_issues:
        print(f"\n❌ FOUND {len(quote_issues)} LINES WITH UNMATCHED QUOTES:")
        for line_num, quote_type, count, line in quote_issues:
            print(f"  Line {line_num}: {count} unmatched {quote_type} quotes")
            print(f"    Content: {line}")
            
            # Show character-by-character breakdown for this line
            print(f"    Quotes breakdown:")
            for j, char in enumerate(line):
                if char in ["'", '"']:
                    escaped = j > 0 and line[j-1] == '\\'
                    print(f"      Position {j}: {char} {'(escaped)' if escaped else '(unescaped)'}")
    else:
        print("✅ No unmatched quotes found in SP-Architect case")
    
    # Also check the overall balance across the entire case
    print(f"\n🔍 OVERALL QUOTE BALANCE IN SP-ARCHITECT CASE:")
    
    sp_content = '\n'.join(lines[sp_start:sp_end + 1])
    
    # Count all quotes in the entire case
    total_single = sp_content.count("'") - sp_content.count("\\'")
    total_double = sp_content.count('"') - sp_content.count('\\"')
    
    print(f"Total single quotes: {total_single} {'(balanced)' if total_single % 2 == 0 else '(UNBALANCED)'}")
    print(f"Total double quotes: {total_double} {'(balanced)' if total_double % 2 == 0 else '(UNBALANCED)'}")
    
    if total_single % 2 != 0 or total_double % 2 != 0:
        print("\n❌ QUOTE IMBALANCE CONFIRMED - THIS WILL CAUSE JAVASCRIPT SYNTAX ERROR")
        print("This prevents the SP-Architect case from executing properly!")
        
        # Try to identify the problematic line more specifically
        print(f"\n🔍 SCANNING FOR PROBLEMATIC PATTERNS:")
        
        problematic_patterns = [
            r"innerHTML\s*=\s*'[^']*'[^;]*'",  # innerHTML with multiple quotes
            r"textContent\s*=\s*'[^']*'[^;]*'",  # textContent with multiple quotes
            r"'[^']*\\'[^']*'",  # Escaped quotes within strings
        ]
        
        import re
        for pattern in problematic_patterns:
            matches = re.finditer(pattern, sp_content)
            for match in matches:
                start_pos = match.start()
                # Find which line this is on
                lines_before = sp_content[:start_pos].count('\n')
                actual_line_num = sp_start + 1 + lines_before
                print(f"    Suspicious pattern at line {actual_line_num}: {match.group()}")

if __name__ == "__main__":
    find_quote_mismatch()