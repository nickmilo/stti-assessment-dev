#!/usr/bin/env python3
"""
Analyze the multiple submission issue
Following SOP Tenet #2: Use Python script to re-familiarize with code structure
Following SOP Tenet #1: Understand structure before modifying
"""

def analyze_submission_issue():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING SUBMISSION ISSUE ===\n")
    
    # Find all calls to submitToFormspree
    print("🔍 Finding all submitToFormspree calls:")
    lines = content.split('\n')
    submission_calls = []
    
    for i, line in enumerate(lines, 1):
        if 'submitToFormspree' in line and not line.strip().startswith('//') and not 'function submitToFormspree' in line:
            submission_calls.append((i, line.strip()))
    
    print(f"Found {len(submission_calls)} submission calls:")
    for line_num, call in submission_calls:
        print(f"  Line {line_num}: {call}")
    
    # Check if submitToFormspree is called multiple times
    print(f"\n🔍 Analyzing submitToFormspree function:")
    
    # Find the function definition
    func_start = content.find('async function submitToFormspree(')
    if func_start != -1:
        # Get a reasonable chunk around the function
        func_section = content[func_start:func_start+2000]
        
        # Check for any loops or repeated calls within the function
        if 'for(' in func_section or 'while(' in func_section:
            print("  ⚠️  Found loop inside submitToFormspree function")
        
        # Check for multiple fetch calls
        fetch_count = func_section.count('fetch(')
        print(f"  Fetch calls in function: {fetch_count}")
        
        if fetch_count > 1:
            print("  ⚠️  Multiple fetch calls detected in function")
    
    # Check where submitToFormspree is called from
    print(f"\n🔍 Context of submission calls:")
    for line_num, call in submission_calls:
        start_context = max(0, line_num - 5)
        end_context = min(len(lines), line_num + 5)
        
        print(f"\n  Context around line {line_num}:")
        for i in range(start_context, end_context):
            marker = " >>> " if i == line_num - 1 else "     "
            print(f"{marker}{i+1:4d}: {lines[i]}")
    
    # Check for event listeners that might trigger multiple times
    print(f"\n🔍 Checking for problematic event listeners:")
    event_listeners = []
    for i, line in enumerate(lines, 1):
        if 'addEventListener' in line or 'onclick' in line:
            if any(word in line.lower() for word in ['submit', 'result', 'complete']):
                event_listeners.append((i, line.strip()))
    
    if event_listeners:
        print("  Found event listeners that might trigger submissions:")
        for line_num, listener in event_listeners:
            print(f"    Line {line_num}: {listener}")
    else:
        print("  No suspicious event listeners found")
    
    # Check showResults function specifically
    print(f"\n🔍 Analyzing showResults function:")
    show_results_start = content.find('function showResults(')
    if show_results_start != -1:
        # Find the end of the function
        brace_count = 0
        func_start_brace = content.find('{', show_results_start)
        func_end = func_start_brace
        
        for i, char in enumerate(content[func_start_brace:], func_start_brace):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    func_end = i
                    break
        
        show_results_function = content[show_results_start:func_end+1]
        
        # Count submitToFormspree calls in showResults
        submit_calls_in_results = show_results_function.count('submitToFormspree')
        print(f"  submitToFormspree calls in showResults: {submit_calls_in_results}")
        
        if submit_calls_in_results > 1:
            print("  ⚠️  Multiple submission calls in showResults function!")
    
    # Look for any secret code or test functionality that might cause issues
    print(f"\n🔍 Checking secret code functionality:")
    secret_code_section = content[content.find('keySequence'):content.find('keySequence') + 3000] if 'keySequence' in content else ""
    
    if 'submitToFormspree' in secret_code_section:
        print("  ⚠️  SECRET CODES MIGHT BE SUBMITTING TO FORMSPREE!")
        print("  This could cause multiple submissions during testing")
    else:
        print("  ✅ Secret codes don't appear to submit to Formspree")
    
    print(f"\n💡 LIKELY CAUSES:")
    print("  1. Multiple event listeners attached to the same button")
    print("  2. Function called multiple times due to navigation/back button")
    print("  3. Secret codes accidentally triggering submissions")
    print("  4. User clicking submit button multiple times")
    print("  5. Browser back/forward causing re-execution")

if __name__ == "__main__":
    analyze_submission_issue()