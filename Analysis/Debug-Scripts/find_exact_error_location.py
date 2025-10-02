#!/usr/bin/env python3
"""
Find the exact location of orientationArchetypes error
Following SOP Tenet #2: Use Python script to understand full structure
"""

def find_exact_error():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FINDING EXACT orientationArchetypes ERROR ===\n")
    
    lines = content.split('\n')
    
    # Find showResults function
    print("🔍 SHOWRESULTS FUNCTION ANALYSIS:")
    show_results_start = None
    show_results_end = None
    
    for i, line in enumerate(lines):
        if 'function showResults()' in line:
            show_results_start = i
            print(f"  showResults starts at line {i+1}")
            break
    
    if show_results_start:
        brace_count = 0
        for i in range(show_results_start, len(lines)):
            line = lines[i]
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and i > show_results_start:
                show_results_end = i
                print(f"  showResults ends at line {i+1}")
                break
        
        # Check for orientationArchetypes usage in showResults
        print(f"\n  Checking for orientationArchetypes in showResults function:")
        for i in range(show_results_start, show_results_end + 1):
            if 'orientationArchetypes' in lines[i]:
                print(f"    ❌ LINE {i+1}: {lines[i].strip()}")
    
    # Find ALL orientationArchetypes usage
    print(f"\n🔍 ALL orientationArchetypes REFERENCES:")
    orientationArchetypes_lines = []
    
    for i, line in enumerate(lines, 1):
        if 'orientationArchetypes' in line:
            orientationArchetypes_lines.append((i, line.strip()))
    
    declaration_lines = []
    usage_lines = []
    
    for line_num, line_content in orientationArchetypes_lines:
        if 'const orientationArchetypes' in line_content:
            declaration_lines.append((line_num, line_content))
            print(f"  DECLARATION Line {line_num}: {line_content}")
        else:
            usage_lines.append((line_num, line_content))
            print(f"  USAGE Line {line_num}: {line_content}")
    
    # Check function scope for each usage
    print(f"\n🔍 FUNCTION SCOPE ANALYSIS:")
    
    # Find all function definitions
    function_starts = []
    for i, line in enumerate(lines, 1):
        if 'function ' in line and '{' in line:
            func_name = line.strip().split('function ')[1].split('(')[0]
            function_starts.append((i, func_name))
    
    print(f"  Found {len(function_starts)} functions")
    
    # For each orientationArchetypes usage, find which function it's in
    for usage_line, usage_content in usage_lines:
        current_function = None
        for func_line, func_name in function_starts:
            if func_line < usage_line:
                current_function = func_name
        
        print(f"    Line {usage_line} (in {current_function}): {usage_content[:60]}...")
    
    # Check if orientationArchetypes is declared in each function where it's used
    print(f"\n🔍 SCOPE VALIDATION:")
    
    # Group usage by function
    function_usage = {}
    for usage_line, usage_content in usage_lines:
        current_function = None
        for func_line, func_name in function_starts:
            if func_line < usage_line:
                current_function = func_name
        
        if current_function not in function_usage:
            function_usage[current_function] = []
        function_usage[current_function].append((usage_line, usage_content))
    
    for func_name, usages in function_usage.items():
        print(f"\n  Function: {func_name}")
        print(f"    Uses orientationArchetypes {len(usages)} times")
        
        # Check if this function has a declaration
        has_declaration = False
        for decl_line, decl_content in declaration_lines:
            # Check if declaration is in this function's scope
            func_start = None
            func_end = None
            
            for func_line, fname in function_starts:
                if fname == func_name:
                    func_start = func_line
                    break
            
            if func_start:
                brace_count = 0
                for i in range(func_start - 1, len(lines)):
                    line = lines[i]
                    brace_count += line.count('{') - line.count('}')
                    if brace_count == 0 and i > func_start - 1:
                        func_end = i + 1
                        break
                
                if func_start <= decl_line <= func_end:
                    has_declaration = True
                    print(f"    ✅ Has declaration at line {decl_line}")
                    break
        
        if not has_declaration:
            print(f"    ❌ NO DECLARATION - this will cause ReferenceError!")
            for usage_line, usage_content in usages:
                print(f"      Line {usage_line}: {usage_content[:60]}...")

if __name__ == "__main__":
    find_exact_error()