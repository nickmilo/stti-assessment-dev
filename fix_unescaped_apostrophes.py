#!/usr/bin/env python3
"""
Fix unescaped apostrophes in JavaScript strings
Following SOP Tenet #4: Make surgical changes
"""

def fix_apostrophes():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== FIXING UNESCAPED APOSTROPHES ===")
    
    lines = content.split('\n')
    changes_made = []
    
    # Focus on the area from SP-Architect onward where the issues were detected
    start_line = 2170 - 1  # 0-indexed
    
    for i in range(start_line, len(lines)):
        line = lines[i]
        original_line = line
        
        # Look for JavaScript string assignments with unescaped apostrophes
        if ('innerHTML =' in line or 'textContent =' in line) and "'" in line:
            # Find content within single quotes and escape apostrophes
            import re
            
            # Pattern to match: = 'content with apostrophes';
            pattern = r"(innerHTML|textContent)\s*=\s*'([^']*(?:\\'[^']*)*)'\s*;"
            
            def escape_apostrophes(match):
                prefix = match.group(1)
                content = match.group(2)
                
                # Count existing escaped apostrophes
                escaped_count = content.count("\\'")
                total_count = content.count("'")
                unescaped_count = total_count - escaped_count
                
                if unescaped_count > 0:
                    # Escape unescaped apostrophes
                    # Be careful not to double-escape
                    result_content = ''
                    j = 0
                    while j < len(content):
                        if content[j] == "'" and (j == 0 or content[j-1] != '\\'):
                            result_content += "\\'"
                        else:
                            result_content += content[j]
                        j += 1
                    
                    return f"{prefix} = '{result_content}';"
                
                return match.group(0)  # No changes needed
            
            new_line = re.sub(pattern, escape_apostrophes, line)
            
            if new_line != original_line:
                lines[i] = new_line
                changes_made.append((i + 1, original_line.strip(), new_line.strip()))
        
        # Also fix the comment line
        elif "return; // Exit early, don't use generic logic" in line:
            new_line = line.replace("don't", "dont")  # Simple fix for comment
            if new_line != original_line:
                lines[i] = new_line
                changes_made.append((i + 1, original_line.strip(), new_line.strip()))
    
    if changes_made:
        print(f"Found {len(changes_made)} lines that need fixing:")
        for line_num, old, new in changes_made[:10]:  # Show first 10
            print(f"  Line {line_num}:")
            print(f"    OLD: {old[:100]}...")
            print(f"    NEW: {new[:100]}...")
        
        if len(changes_made) > 10:
            print(f"    ... and {len(changes_made) - 10} more")
        
        # Write the fixed content back
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"\n✅ Fixed {len(changes_made)} lines with unescaped apostrophes")
        print("The SP-Architect case should now execute properly!")
    else:
        print("No unescaped apostrophes found that need fixing")

if __name__ == "__main__":
    fix_apostrophes()