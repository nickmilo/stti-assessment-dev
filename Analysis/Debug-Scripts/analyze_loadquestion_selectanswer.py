#!/usr/bin/env python3
"""
Analyze loadQuestion and selectAnswer functions
Following SOP Tenet #1: Understand the actual error locations
"""

def analyze_actual_errors():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING ACTUAL ERROR LOCATIONS ===")
    print("Error 1: Line 2728 in loadQuestion - orientationArchetypes")
    print("Error 2: Line 2760 in selectAnswer - reading 'id'\n")
    
    lines = content.split('\n')
    
    # 1. Check line 2728 in loadQuestion
    print("🔍 LINE 2728 ANALYSIS (loadQuestion):")
    if len(lines) >= 2728:
        print(f"  Line 2728: {lines[2727].strip()}")
        print(f"  Line 2727: {lines[2726].strip()}")
        print(f"  Line 2729: {lines[2728].strip()}")
        
        # Check if orientationArchetypes is referenced here
        if 'orientationArchetypes' in lines[2727]:
            print("  ❌ orientationArchetypes found on line 2728!")
    
    # 2. Find loadQuestion function and check for orientationArchetypes usage
    print(f"\n🔍 LOADQUESTION FUNCTION ANALYSIS:")
    load_question_start = None
    for i, line in enumerate(lines, 1):
        if 'function loadQuestion(' in line:
            load_question_start = i
            break
    
    if load_question_start:
        print(f"  loadQuestion starts at line {load_question_start}")
        
        # Check next 50 lines for orientationArchetypes
        orientationArchetypes_found = []
        for i in range(load_question_start - 1, min(load_question_start + 49, len(lines))):
            if 'orientationArchetypes' in lines[i]:
                orientationArchetypes_found.append((i + 1, lines[i].strip()))
        
        if orientationArchetypes_found:
            print(f"  ❌ orientationArchetypes found in loadQuestion:")
            for line_num, line_content in orientationArchetypes_found:
                print(f"    Line {line_num}: {line_content}")
        else:
            print(f"  ✅ No orientationArchetypes found in loadQuestion")
    
    # 3. Check line 2760 in selectAnswer  
    print(f"\n🔍 LINE 2760 ANALYSIS (selectAnswer):")
    if len(lines) >= 2760:
        print(f"  Line 2760: {lines[2759].strip()}")
        print(f"  Line 2759: {lines[2758].strip()}")
        print(f"  Line 2761: {lines[2760].strip()}")
        
        # Check for .id references
        if '.id' in lines[2759]:
            print("  ❌ .id reference found on line 2760!")
    
    # 4. Find selectAnswer function and check for .id usage
    print(f"\n🔍 SELECTANSWER FUNCTION ANALYSIS:")
    select_answer_start = None
    for i, line in enumerate(lines, 1):
        if 'function selectAnswer(' in line:
            select_answer_start = i
            break
    
    if select_answer_start:
        print(f"  selectAnswer starts at line {select_answer_start}")
        
        # Check for .id references in function
        id_references = []
        for i in range(select_answer_start - 1, min(select_answer_start + 99, len(lines))):
            if '.id' in lines[i] and 'getElementById' not in lines[i]:
                id_references.append((i + 1, lines[i].strip()))
        
        if id_references:
            print(f"  Found .id references in selectAnswer:")
            for line_num, line_content in id_references:
                print(f"    Line {line_num}: {line_content}")
                if line_num == 2760:
                    print(f"      ❌ THIS IS THE ERROR LINE!")
        
        # Check for variable declarations that might be undefined
        print(f"\n  Variable usage in selectAnswer:")
        for i in range(select_answer_start - 1, min(select_answer_start + 99, len(lines))):
            line = lines[i]
            if ('questions[' in line or 'currentQuestion' in line or 
                'button' in line.lower() or 'event' in line.lower()):
                print(f"    Line {i + 1}: {line.strip()}")
    
    # 5. Check if these functions are in the global scope or have access issues
    print(f"\n🔍 GLOBAL SCOPE ANALYSIS:")
    
    # Check for global variable declarations
    global_vars = []
    for i, line in enumerate(lines[:100], 1):  # Check first 100 lines
        if ('let ' in line or 'const ' in line or 'var ' in line) and 'function' not in line:
            global_vars.append((i, line.strip()))
    
    print(f"  Global variables found:")
    for line_num, line_content in global_vars:
        print(f"    Line {line_num}: {line_content}")
    
    # 6. Check the specific error context
    print(f"\n🔍 ERROR CONTEXT ANALYSIS:")
    print("  The errors suggest:")
    print("  1. orientationArchetypes is being accessed before it's declared")
    print("  2. Some object's .id property is undefined")
    print("  3. These errors happen during question loading/answering, not results display")
    
    print(f"\n📋 INVESTIGATION NEEDED:")
    print("  1. Why is loadQuestion trying to access orientationArchetypes?")
    print("  2. What object in selectAnswer has an undefined .id property?")
    print("  3. Are these functions accidentally referencing variables from other scopes?")

if __name__ == "__main__":
    analyze_actual_errors()