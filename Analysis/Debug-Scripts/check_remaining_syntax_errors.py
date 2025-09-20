#!/usr/bin/env python3
"""
Check for remaining unmatched quotes in the setCollapsibleSections function
"""

def check_syntax_errors():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    print("=== CHECKING FOR REMAINING SYNTAX ERRORS ===")
    
    # Find setCollapsibleSections function boundaries
    func_start = None
    func_end = None
    
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            func_start = i
        elif func_start and line.strip() == '}' and 'function' in lines[i] if i < len(lines) else False:
            func_end = i
            break
    
    if not func_start:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    # Look for the actual end
    for i in range(func_start, len(lines)):
        if 'function ' in lines[i] and i > func_start:
            func_end = i - 1
            break
    
    if not func_end:
        func_end = len(lines)
    
    print(f"Checking lines {func_start} to {func_end}")
    
    syntax_errors = []
    
    for i in range(func_start - 1, func_end):
        line = lines[i]
        line_num = i + 1
        line_content = line.strip()
        
        if line_content and not line_content.startswith('//'):
            # Check for unmatched quotes (excluding escaped quotes)
            # Count single quotes not preceded by backslash
            single_quotes = 0
            j = 0
            while j < len(line_content):
                if line_content[j] == "'" and (j == 0 or line_content[j-1] != '\\'):
                    single_quotes += 1
                j += 1
            
            if single_quotes % 2 != 0:
                syntax_errors.append(f"Line {line_num}: Unmatched single quotes - {line_content[:100]}...")
    
    if syntax_errors:
        print(f"❌ FOUND {len(syntax_errors)} SYNTAX ERRORS:")
        for error in syntax_errors:
            print(f"  {error}")
    else:
        print("✅ No syntax errors found in setCollapsibleSections!")
    
    # Also check specifically for the patterns that were failing
    failing_profiles = ['IC-Architect', 'IC-Gardener', 'PI-Architect', 'PI-Gardener', 'PC-Architect', 
                       'SI-Architect', 'SI-Gardener', 'SP-Gardener', 'SC-Architect', 'SC-Gardener']
    
    print(f"\n🔍 CHECKING SPECIFIC FAILING PROFILES:")
    for profile in failing_profiles:
        for i, line in enumerate(lines, 1):
            if f"code === '{profile}'" in line:
                print(f"  ✅ {profile} found at line {i}")
                break
        else:
            print(f"  ❌ {profile} NOT FOUND")

if __name__ == "__main__":
    check_syntax_errors()