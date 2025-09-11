#!/usr/bin/env python3
"""
Fix multiple submission issue by adding a submission guard
Following SOP Tenet #4: One surgical change at a time
"""

def fix_multiple_submissions():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== FIXING MULTIPLE SUBMISSION ISSUE ===\n")
    
    # Add a global flag to prevent multiple submissions
    # Find where to add the flag (near other global variables)
    user_email_line = content.find('let userEmail')
    if user_email_line == -1:
        print("❌ Could not find userEmail variable location")
        return False
    
    # Find the end of that line
    end_of_line = content.find('\n', user_email_line)
    
    # Add the submission flag after userEmail declaration
    flag_declaration = "\n        let hasSubmitted = false; // Prevent multiple form submissions"
    
    new_content = content[:end_of_line] + flag_declaration + content[end_of_line:]
    
    # Now modify showResults function to check and set the flag
    show_results_start = new_content.find('function showResults() {')
    if show_results_start == -1:
        print("❌ Could not find showResults function")
        return False
    
    # Find the opening brace and add the guard
    opening_brace = new_content.find('{', show_results_start)
    
    guard_code = '''
            // Prevent multiple submissions
            if (hasSubmitted) {
                console.log('Results already submitted, skipping duplicate submission');
                return;
            }
            hasSubmitted = true;
'''
    
    new_content = new_content[:opening_brace+1] + guard_code + new_content[opening_brace+1:]
    
    # Write the fixed content
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(new_content)
    
    print("✅ Added submission guard to prevent multiple submissions")
    print("   - Added hasSubmitted flag")
    print("   - Added guard in showResults function")
    return True

if __name__ == "__main__":
    fix_multiple_submissions()