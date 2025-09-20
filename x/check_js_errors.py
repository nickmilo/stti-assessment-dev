#!/usr/bin/env python3
"""
Check for potential JavaScript errors in the HTML file
"""

def check_js_errors(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    print("=== Checking for potential JavaScript issues ===\n")
    
    # Check for duplicate function definitions
    function_defs = {}
    for i, line in enumerate(lines):
        if 'function ' in line and '(' in line:
            # Extract function name
            func_match = line.strip()
            if 'function ' in func_match:
                parts = func_match.split('function ')
                if len(parts) > 1:
                    func_name = parts[1].split('(')[0].strip()
                    if func_name:
                        if func_name in function_defs:
                            print(f"DUPLICATE FUNCTION: {func_name}")
                            print(f"  First definition: line {function_defs[func_name]+1}")
                            print(f"  Second definition: line {i+1}")
                        else:
                            function_defs[func_name] = i
    
    # Check for syntax patterns that might cause issues
    issues = []
    
    for i, line in enumerate(lines):
        # Check for unclosed strings
        single_quotes = line.count("'")
        double_quotes = line.count('"')
        if single_quotes % 2 != 0:
            issues.append(f"Line {i+1}: Odd number of single quotes")
        
        # Check for console.log to verify they're running
        if 'console.log' in line:
            print(f"Console.log at line {i+1}: {line.strip()[:80]}...")
    
    # Find the exact showTestResults function
    print("\n=== showTestResults Function Definition ===")
    in_show_test = False
    brace_count = 0
    for i, line in enumerate(lines):
        if 'function showTestResults' in line:
            in_show_test = True
            start_line = i
            print(f"Found at line {i+1}")
        
        if in_show_test:
            if '{' in line:
                brace_count += line.count('{')
            if '}' in line:
                brace_count -= line.count('}')
            
            if brace_count == 0 and i > start_line:
                print(f"Function ends at line {i+1}")
                print(f"Function spans {i - start_line + 1} lines")
                break
    
    # Check event listener registration
    print("\n=== Event Listener Registration ===")
    for i, line in enumerate(lines):
        if "addEventListener('keydown'" in line or 'addEventListener("keydown"' in line:
            print(f"Keydown listener at line {i+1}: {line.strip()[:80]}...")
            
    # Check if the code is inside a DOMContentLoaded or similar
    print("\n=== Script Execution Context ===")
    dom_ready_found = False
    for i, line in enumerate(lines):
        if 'DOMContentLoaded' in line or 'window.onload' in line or '$(document).ready' in line:
            dom_ready_found = True
            print(f"Found DOM ready handler at line {i+1}")
    
    if not dom_ready_found:
        print("No explicit DOM ready handler found (code runs immediately)")
    
    # Check the actual email input handler
    print("\n=== Email Input Handler ===")
    for i, line in enumerate(lines):
        if "secretCodes[userEmail" in line:
            # Show context
            print(f"Secret code check at line {i+1}")
            for j in range(max(0, i-5), min(len(lines), i+5)):
                print(f"  {j+1}: {lines[j].rstrip()}")
    
    return issues

if __name__ == "__main__":
    issues = check_js_errors("/Users/nick/Dropbox/+/AI/stti-assessment/index.html")
    
    if issues:
        print("\n=== Potential Issues Found ===")
        for issue in issues:
            print(f"  {issue}")