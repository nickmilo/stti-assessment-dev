#!/usr/bin/env python3
"""
COMPREHENSIVE ERROR ANALYSIS - Following ALL 5 Tenets
Tenet #2: Use Python script to re-familiarize with ENTIRETY of code
Tenet #1: Understand structure completely before making ANY changes
"""

def comprehensive_analysis():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== COMPREHENSIVE ERROR ANALYSIS ===")
    print("Following SOP Tenet #2: Understanding ENTIRE codebase structure\n")
    
    lines = content.split('\n')
    
    # 1. Map ALL functions that exist
    print("🔍 COMPLETE FUNCTION MAPPING:")
    all_functions = []
    for i, line in enumerate(lines, 1):
        if 'function ' in line and '(' in line and '{' in line:
            func_name = line.strip().split('function ')[1].split('(')[0].strip()
            all_functions.append((i, func_name))
            print(f"  Line {i}: {func_name}()")
    
    print(f"\nTotal functions found: {len(all_functions)}")
    
    # 2. For EVERY function, check if it uses orientationArchetypes
    print(f"\n🔍 orientationArchetypes USAGE BY FUNCTION:")
    
    function_orientationArchetypes_usage = {}
    
    for i, (func_line, func_name) in enumerate(all_functions):
        # Find function boundaries
        func_start = func_line - 1  # 0-indexed
        func_end = len(lines)
        
        # Find next function or end of file
        if i + 1 < len(all_functions):
            func_end = all_functions[i + 1][0] - 1
        
        # Count orientationArchetypes usage in this function
        usage_count = 0
        declaration_count = 0
        usage_lines = []
        declaration_lines = []
        
        for line_num in range(func_start, min(func_end, len(lines))):
            line_content = lines[line_num]
            if 'orientationArchetypes' in line_content:
                if 'const orientationArchetypes' in line_content:
                    declaration_count += 1
                    declaration_lines.append(line_num + 1)
                else:
                    usage_count += 1
                    usage_lines.append(line_num + 1)
        
        if usage_count > 0 or declaration_count > 0:
            function_orientationArchetypes_usage[func_name] = {
                'usage_count': usage_count,
                'declaration_count': declaration_count,
                'usage_lines': usage_lines,
                'declaration_lines': declaration_lines,
                'func_start': func_line,
                'func_end': func_end
            }
            
            print(f"\n  Function: {func_name} (lines {func_line}-{func_end})")
            print(f"    Declarations: {declaration_count} at lines {declaration_lines}")
            print(f"    Usage: {usage_count} times at lines {usage_lines[:5]}{'...' if len(usage_lines) > 5 else ''}")
            
            if usage_count > 0 and declaration_count == 0:
                print(f"    ❌ CRITICAL ERROR: Uses orientationArchetypes but has NO declaration!")
            elif declaration_count > 0 and usage_count > 0:
                print(f"    ✅ Has both declaration and usage")
            elif declaration_count > 0 and usage_count == 0:
                print(f"    ⚠️  Has declaration but no usage (unused variable)")
    
    # 3. Check for scope bleeding between functions
    print(f"\n🔍 SCOPE BLEEDING ANALYSIS:")
    for func_name, data in function_orientationArchetypes_usage.items():
        if data['usage_count'] > 0 and data['declaration_count'] == 0:
            print(f"\n  ❌ {func_name} uses orientationArchetypes without declaring it")
            print(f"     This will cause ReferenceError unless variable comes from:")
            print(f"     - Global scope (not found)")
            print(f"     - Parent function scope (checking...)")
            
            # Check if any parent scope has declaration
            has_parent_declaration = False
            for other_func, other_data in function_orientationArchetypes_usage.items():
                if (other_data['func_start'] < data['func_start'] and 
                    other_data['func_end'] > data['func_end'] and 
                    other_data['declaration_count'] > 0):
                    print(f"     ✅ Found parent declaration in {other_func}")
                    has_parent_declaration = True
                    break
            
            if not has_parent_declaration:
                print(f"     ❌ NO PARENT DECLARATION FOUND - WILL CAUSE ERROR!")
    
    # 4. Check for execution flow that might call these functions
    print(f"\n🔍 FUNCTION CALL ANALYSIS:")
    
    critical_functions = []
    for func_name, data in function_orientationArchetypes_usage.items():
        if data['usage_count'] > 0 and data['declaration_count'] == 0:
            critical_functions.append(func_name)
    
    if critical_functions:
        print(f"  Functions with orientationArchetypes errors: {critical_functions}")
        
        # Find where these functions are called
        for func_name in critical_functions:
            print(f"\n  Calls to {func_name}:")
            for i, line in enumerate(lines, 1):
                if f'{func_name}(' in line and 'function ' not in line:
                    print(f"    Line {i}: {line.strip()}")
    
    # 5. Check question 53 completion flow specifically
    print(f"\n🔍 QUESTION 53 COMPLETION FLOW:")
    
    # Find selectAnswer function and trace its flow
    select_answer_start = content.find('function selectAnswer(')
    if select_answer_start != -1:
        select_section = content[select_answer_start:select_answer_start + 3000]
        
        print("  selectAnswer function flow:")
        if 'currentQuestion === questions.length - 1' in select_section:
            print("    ✅ Detects last question (53)")
        if 'showResults()' in select_section:
            print("    ✅ Calls showResults()")
            # Check if showResults has errors
            if 'showResults' in critical_functions:
                print("    ❌ showResults has orientationArchetypes error!")
        
        # Check for any function calls that might have errors
        for func_name in critical_functions:
            if f'{func_name}(' in select_section:
                print(f"    ❌ Calls {func_name} which has orientationArchetypes error!")
    
    # 6. Summary and action plan
    print(f"\n📋 ERROR SUMMARY:")
    if critical_functions:
        print(f"  ❌ {len(critical_functions)} functions have orientationArchetypes scope errors")
        for func_name in critical_functions:
            data = function_orientationArchetypes_usage[func_name]
            print(f"     - {func_name}: {data['usage_count']} uses, 0 declarations")
        
        print(f"\n📋 REQUIRED FIXES:")
        for func_name in critical_functions:
            print(f"  - Add 'const orientationArchetypes = profile.dominantArchetypes.sort().join(\\'\\');' to {func_name}")
    else:
        print("  ✅ No orientationArchetypes scope errors found")
    
    # 7. Check for other potential issues
    print(f"\n🔍 OTHER POTENTIAL ISSUES:")
    
    # Check for profile object availability
    profile_references = []
    for i, line in enumerate(lines, 1):
        if 'profile.' in line and 'function ' not in line:
            profile_references.append((i, line.strip()))
    
    print(f"  Found {len(profile_references)} profile object references")
    
    # Check if profile is passed as parameter or declared in functions with errors
    for func_name in critical_functions:
        func_line = function_orientationArchetypes_usage[func_name]['func_start']
        func_definition = lines[func_line - 1]
        
        if 'profile)' in func_definition:
            print(f"    ✅ {func_name} receives profile as parameter")
        else:
            print(f"    ❌ {func_name} might not have access to profile object!")

if __name__ == "__main__":
    comprehensive_analysis()