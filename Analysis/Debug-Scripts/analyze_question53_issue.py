#!/usr/bin/env python3
"""
Analyze why question 53 doesn't proceed to results
Following SOP Tenet #2: Use Python script to re-familiarize with code structure
Following SOP Tenet #1: Understand structure before modifying
"""

def analyze_question53_issue():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING QUESTION 53 ISSUE ===\n")
    
    # Find how many questions there are
    questions_start = content.find('const questions = [')
    if questions_start != -1:
        questions_section = content[questions_start:questions_start + 50000]
        question_count = questions_section.count('id:')
        print(f"📋 Total questions in array: {question_count}")
    
    # Find the logic that determines when to show results
    print(f"\n🔍 Finding result trigger logic:")
    
    # Look for showResults calls and their conditions
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        if 'showResults()' in line:
            # Show context around each showResults call
            start_context = max(0, i - 8)
            end_context = min(len(lines), i + 3)
            
            print(f"\n  showResults() call at line {i}:")
            for j in range(start_context, end_context):
                marker = " >>> " if j == i - 1 else "     "
                print(f"{marker}{j+1:4d}: {lines[j]}")
    
    # Check currentQuestion logic
    print(f"\n🔍 Analyzing currentQuestion logic:")
    
    # Find where currentQuestion is incremented
    current_question_increments = []
    for i, line in enumerate(lines, 1):
        if 'currentQuestion++' in line or 'currentQuestion =' in line:
            current_question_increments.append((i, line.strip()))
    
    print(f"  Found {len(current_question_increments)} currentQuestion modifications:")
    for line_num, line in current_question_increments:
        print(f"    Line {line_num}: {line}")
    
    # Check the specific condition for question 53
    print(f"\n🔍 Checking conditions for last question:")
    
    # Look for length checks
    for i, line in enumerate(lines, 1):
        if 'questions.length' in line and ('currentQuestion' in line or 'showResults' in line):
            print(f"  Line {i}: {line.strip()}")
            
            # Show more context for this line
            start_context = max(0, i - 5)
            end_context = min(len(lines), i + 5)
            print(f"    Context:")
            for j in range(start_context, end_context):
                marker = "   >>> " if j == i - 1 else "       "
                print(f"{marker}{j+1:4d}: {lines[j]}")
            print()
    
    # Check if there's an off-by-one error
    print(f"\n🔍 Checking for off-by-one errors:")
    print(f"  If there are {question_count} questions (ids 0-{question_count-1}):")
    print(f"  - questions.length = {question_count}")
    print(f"  - Last question index = {question_count-1}")
    print(f"  - currentQuestion should reach {question_count-1} for last question")
    print(f"  - Condition 'currentQuestion >= questions.length' means currentQuestion >= {question_count}")
    print(f"  - This triggers when currentQuestion = {question_count} (after answering last question)")
    
    # Look for the forward button logic specifically
    print(f"\n🔍 Analyzing forward button logic:")
    forward_logic_start = content.find('forwardBtn.addEventListener')
    if forward_logic_start != -1:
        forward_section = content[forward_logic_start:forward_logic_start + 1000]
        forward_lines = forward_section.split('\n')
        
        print(f"  Forward button event listener:")
        for i, line in enumerate(forward_lines[:15]):
            print(f"    {line}")
    
    # Check selectAnswer function
    print(f"\n🔍 Checking selectAnswer function:")
    select_answer_start = content.find('function selectAnswer(')
    if select_answer_start != -1:
        select_section = content[select_answer_start:select_answer_start + 2000]
        
        # Look for showResults calls in selectAnswer
        if 'showResults()' in select_section:
            print(f"  ✅ selectAnswer contains showResults() call")
        else:
            print(f"  ❌ selectAnswer does NOT contain showResults() call")
            
        # Show the end of selectAnswer function
        print(f"  End of selectAnswer function:")
        select_lines = select_section.split('\n')
        for i, line in enumerate(select_lines[-10:]):
            print(f"    {line}")

if __name__ == "__main__":
    analyze_question53_issue()