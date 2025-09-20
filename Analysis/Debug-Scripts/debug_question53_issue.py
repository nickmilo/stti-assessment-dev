#!/usr/bin/env python3
"""
Debug Question 53 Issue - Following SOP Tenet #2 and #5
Comprehensive analysis of the assessment completion failure
"""

def debug_question53_issue():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== DEBUGGING QUESTION 53 ISSUE ===\n")
    
    # 1. Analyze the errors from screenshot
    print("🔍 SCREENSHOT ERROR ANALYSIS:")
    print("  Error 1: ReferenceError: Cannot access 'orientationArchetypes' before initialization")
    print("  Error 2: TypeError: Cannot read properties of undefined (reading 'id')")
    print("  Error 3: TypeError: Cannot read properties of undefined (reading 'id')")
    print("  Location: loadQuestion and selectAnswer functions")
    print()
    
    # 2. Find where orientationArchetypes is used
    print("🔍 ORIENTATIONARCHETYPES USAGE ANALYSIS:")
    lines = content.split('\n')
    orientation_usage = []
    
    for i, line in enumerate(lines, 1):
        if 'orientationArchetypes' in line:
            orientation_usage.append((i, line.strip()))
    
    print(f"  Found {len(orientation_usage)} references to orientationArchetypes:")
    for line_num, line_content in orientation_usage:
        print(f"    Line {line_num}: {line_content}")
    print()
    
    # 3. Find where orientationArchetypes is declared
    print("🔍 ORIENTATIONARCHETYPES DECLARATION ANALYSIS:")
    declarations = []
    for i, line in enumerate(lines, 1):
        if 'const orientationArchetypes' in line or 'let orientationArchetypes' in line:
            declarations.append((i, line.strip()))
    
    print(f"  Found {len(declarations)} declarations:")
    for line_num, line_content in declarations:
        print(f"    Line {line_num}: {line_content}")
    print()
    
    # 4. Check if orientationArchetypes is used before declaration
    if declarations and orientation_usage:
        first_declaration = min(declarations, key=lambda x: x[0])[0]
        early_usage = [usage for usage in orientation_usage if usage[0] < first_declaration]
        
        if early_usage:
            print("  ❌ PROBLEM FOUND: orientationArchetypes used before declaration!")
            for line_num, line_content in early_usage:
                print(f"    Line {line_num}: {line_content}")
        else:
            print("  ✅ orientationArchetypes is declared before all usage")
    print()
    
    # 5. Analyze selectAnswer function for undefined 'id' errors
    print("🔍 SELECTANSWER FUNCTION ANALYSIS:")
    select_answer_start = content.find('function selectAnswer(')
    if select_answer_start != -1:
        select_section = content[select_answer_start:select_answer_start + 2000]
        
        # Look for button and question references
        print("  Looking for button/question ID usage:")
        select_lines = select_section.split('\n')
        for i, line in enumerate(select_lines):
            if '.id' in line or 'currentQuestion' in line:
                print(f"    {line.strip()}")
    print()
    
    # 6. Analyze loadQuestion function
    print("🔍 LOADQUESTION FUNCTION ANALYSIS:")
    load_question_start = content.find('function loadQuestion(')
    if load_question_start != -1:
        load_section = content[load_question_start:load_question_start + 2000]
        
        print("  Looking for question loading logic:")
        load_lines = load_section.split('\n')
        for i, line in enumerate(load_lines):
            if 'questions[' in line or '.id' in line:
                print(f"    {line.strip()}")
    print()
    
    # 7. Check for missing variable declarations
    print("🔍 MISSING VARIABLE ANALYSIS:")
    variables_to_check = ['currentQuestion', 'questions', 'answers']
    
    for var in variables_to_check:
        if f'let {var}' in content or f'const {var}' in content or f'var {var}' in content:
            print(f"  ✅ {var} is declared")
        else:
            print(f"  ❌ {var} might not be properly declared")
    
    # 8. Check for scope issues in showResults
    print(f"\n🔍 SHOWRESULTS SCOPE ANALYSIS:")
    show_results_start = content.find('function showResults()')
    if show_results_start != -1:
        show_section = content[show_results_start:show_results_start + 500]
        
        print("  Checking variable scope in showResults:")
        if 'orientationArchetypes' in show_section:
            print("    ❌ orientationArchetypes referenced in showResults")
            print("    This might be a scope issue - variable declared in different function")
        else:
            print("    ✅ No orientationArchetypes reference in showResults")
    
    print(f"\n📋 RECOMMENDED FIXES:")
    print("  1. Move orientationArchetypes declaration to global scope or proper function")
    print("  2. Check that currentQuestion and questions variables are properly accessible")
    print("  3. Verify that all button/question ID references are valid")
    print("  4. Test that question 53 properly triggers showResults")

if __name__ == "__main__":
    debug_question53_issue()