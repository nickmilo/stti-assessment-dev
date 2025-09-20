#!/usr/bin/env python3
"""
Find ALL const declarations and check for duplicates
Following SOP Tenet #1: Understand the structure completely
"""

def find_duplicates():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FINDING DUPLICATE DECLARATIONS ===\n")
    
    lines = content.split('\n')
    
    # Find ALL const declarations
    const_declarations = {}
    
    for i, line in enumerate(lines, 1):
        if 'const ' in line and '=' in line:
            # Extract variable name
            const_part = line.split('const ')[1].split('=')[0].strip()
            
            # Handle destructuring
            if '[' in const_part and ']' in const_part:
                # Destructuring like [archetypes, tendency]
                vars_in_destructure = const_part.strip('[]').split(',')
                for var in vars_in_destructure:
                    var_name = var.strip()
                    if var_name not in const_declarations:
                        const_declarations[var_name] = []
                    const_declarations[var_name].append((i, line.strip()))
            else:
                # Regular const
                var_name = const_part.strip()
                if var_name not in const_declarations:
                    const_declarations[var_name] = []
                const_declarations[var_name].append((i, line.strip()))
    
    # Check for duplicates
    print("🔍 DUPLICATE CONST DECLARATIONS:")
    duplicates_found = False
    
    for var_name, declarations in const_declarations.items():
        if len(declarations) > 1:
            duplicates_found = True
            print(f"\n❌ Variable '{var_name}' declared {len(declarations)} times:")
            for line_num, line_content in declarations:
                print(f"    Line {line_num}: {line_content}")
    
    if not duplicates_found:
        print("✅ No duplicate const declarations found")
    
    # Specifically check orientationArchetypes
    print(f"\n🔍 ORIENTATIONARCHETYPES DECLARATIONS:")
    if 'orientationArchetypes' in const_declarations:
        for line_num, line_content in const_declarations['orientationArchetypes']:
            print(f"    Line {line_num}: {line_content}")
    else:
        print("❌ orientationArchetypes not found in const declarations!")
        
        # Search for it differently
        orientationArchetypes_lines = []
        for i, line in enumerate(lines, 1):
            if 'orientationArchetypes' in line and ('const' in line or 'let' in line or 'var' in line):
                orientationArchetypes_lines.append((i, line.strip()))
        
        if orientationArchetypes_lines:
            print("Found these orientationArchetypes declarations:")
            for line_num, line_content in orientationArchetypes_lines:
                print(f"    Line {line_num}: {line_content}")
    
    # Check for temporal dead zone issues
    print(f"\n🔍 TEMPORAL DEAD ZONE ANALYSIS:")
    
    # Find the showResults function boundaries
    show_results_start = None
    show_results_end = None
    
    for i, line in enumerate(lines, 1):
        if 'function showResults()' in line:
            show_results_start = i
            break
    
    if show_results_start:
        # Find the end of showResults
        brace_count = 0
        for i in range(show_results_start - 1, len(lines)):
            line = lines[i]
            brace_count += line.count('{') - line.count('}')
            if brace_count == 0 and i > show_results_start - 1:
                show_results_end = i + 1
                break
        
        print(f"showResults function: lines {show_results_start} to {show_results_end}")
        
        # Find ALL references to orientationArchetypes in this function
        orientationArchetypes_refs = []
        orientationArchetypes_decl = None
        
        for i in range(show_results_start - 1, show_results_end):
            line = lines[i]
            if 'orientationArchetypes' in line:
                if 'const orientationArchetypes' in line:
                    orientationArchetypes_decl = i + 1
                    print(f"Declaration at line {i + 1}: {line.strip()}")
                else:
                    orientationArchetypes_refs.append((i + 1, line.strip()))
        
        print(f"\nUsage references:")
        for line_num, line_content in orientationArchetypes_refs:
            if orientationArchetypes_decl and line_num < orientationArchetypes_decl:
                print(f"❌ Line {line_num} (BEFORE declaration): {line_content[:60]}...")
            else:
                print(f"✅ Line {line_num} (after declaration): {line_content[:60]}...")

if __name__ == "__main__":
    find_duplicates()