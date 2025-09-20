#!/usr/bin/env python3
"""
Debug the specific question 53 flow
Following SOP Tenet #1: Understand the exact execution path
"""

def debug_q53_specific():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== DEBUGGING QUESTION 53 SPECIFIC FLOW ===\n")
    
    print("🔍 Expected flow for question 53 (index 52):")
    print("  1. User clicks answer on question 53")
    print("  2. selectAnswer() called")
    print("  3. currentQuestion = 52 (last question)")
    print("  4. Check: currentQuestion < questions.length - 1")
    print("  5. 52 < 53 - 1 = 52 < 52 = FALSE")
    print("  6. Goes to else block: setTimeout(() => showResults(), 400)")
    print("  7. After 400ms, showResults() should be called")
    
    print(f"\n🔍 Let's verify the math:")
    print(f"  questions.length = 53")
    print(f"  questions.length - 1 = 52") 
    print(f"  Last question index = 52")
    print(f"  When currentQuestion = 52:")
    print(f"    currentQuestion < questions.length - 1")
    print(f"    52 < 52 = FALSE ✅")
    print(f"  So it should go to else block and call showResults()")
    
    # Let me check if there are any other issues
    print(f"\n🔍 Checking for potential blocking issues:")
    
    # Check if there are any event listeners that might interfere
    lines = content.split('\n')
    
    # Look for any code that might prevent showResults from working
    potential_issues = []
    
    for i, line in enumerate(lines, 1):
        line_lower = line.lower()
        if any(keyword in line_lower for keyword in ['prevent', 'stop', 'return false', 'preventdefault']):
            if any(context in line_lower for context in ['result', 'submit', 'complete']):
                potential_issues.append((i, line.strip()))
    
    if potential_issues:
        print(f"  Found potential blocking code:")
        for line_num, line in potential_issues:
            print(f"    Line {line_num}: {line}")
    else:
        print(f"  No obvious blocking code found")
    
    # Check if showResults function has any early returns
    show_results_start = content.find('function showResults() {')
    if show_results_start != -1:
        show_results_section = content[show_results_start:show_results_start + 3000]
        early_returns = []
        
        for i, line in enumerate(show_results_section.split('\n')):
            if 'return' in line and i < 20:  # Check first 20 lines of function
                early_returns.append(line.strip())
        
        print(f"\n🔍 Early returns in showResults function:")
        for return_line in early_returns:
            print(f"    {return_line}")
    
    # Most likely issue: The hasSubmitted flag might be getting set elsewhere
    print(f"\n🔍 Checking hasSubmitted flag usage:")
    has_submitted_uses = []
    for i, line in enumerate(lines, 1):
        if 'hasSubmitted' in line:
            has_submitted_uses.append((i, line.strip()))
    
    print(f"  All hasSubmitted references:")
    for line_num, line in has_submitted_uses:
        print(f"    Line {line_num}: {line}")
        
    print(f"\n💡 DEBUGGING STEPS TO TRY:")
    print(f"  1. Add console.log in selectAnswer for last question")
    print(f"  2. Add console.log before setTimeout in else block") 
    print(f"  3. Add console.log at start of showResults")
    print(f"  4. Check if hasSubmitted is being set elsewhere")
    print(f"  5. Test with browser dev tools console open")

if __name__ == "__main__":
    debug_q53_specific()