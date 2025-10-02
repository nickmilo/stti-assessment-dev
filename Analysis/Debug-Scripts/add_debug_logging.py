#!/usr/bin/env python3
"""
Add debug logging to track question 53 execution
Following SOP Tenet #4: Surgical change with debugging
"""

def add_debug_logging():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ADDING DEBUG LOGGING FOR Q53 ===\n")
    
    # Add logging in selectAnswer function
    # Find the else block in selectAnswer
    select_answer_else = content.find('} else {\n                setTimeout(() => {\n                    showResults();')
    if select_answer_else != -1:
        # Add debug log before the else block
        debug_log = '''            console.log('Q53 DEBUG: On last question, calling showResults in 400ms');
            '''
        
        new_content = content[:select_answer_else + 8] + debug_log + content[select_answer_else + 8:]
    else:
        print("❌ Could not find selectAnswer else block")
        return False
    
    # Add logging at start of showResults function
    show_results_start = new_content.find('function showResults() {')
    if show_results_start != -1:
        opening_brace = new_content.find('{', show_results_start)
        debug_log2 = '''
            console.log('Q53 DEBUG: showResults() called, hasSubmitted =', hasSubmitted);'''
        
        new_content = new_content[:opening_brace+1] + debug_log2 + new_content[opening_brace+1:]
    else:
        print("❌ Could not find showResults function")
        return False
    
    # Add logging in selectAnswer when answer is selected
    answer_selected = new_content.find('answers[currentQuestion] = {')
    if answer_selected != -1:
        # Find the end of that assignment
        end_assignment = new_content.find('};', answer_selected) + 2
        debug_log3 = '''
            console.log('Q53 DEBUG: Answer selected for question', currentQuestion + 1, 'of', questions.length);'''
        
        new_content = new_content[:end_assignment] + debug_log3 + new_content[end_assignment:]
    else:
        print("❌ Could not find answer assignment")
        return False
    
    # Write the updated content
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(new_content)
    
    print("✅ Added debug logging:")
    print("   - Answer selection logging")
    print("   - Last question detection logging") 
    print("   - showResults() entry logging")
    print("   Check browser console when testing question 53")
    return True

if __name__ == "__main__":
    add_debug_logging()