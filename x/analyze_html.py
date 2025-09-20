#!/usr/bin/env python3
"""
Analyze the HTML file to understand its structure and find potential issues
"""

def analyze_html_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    print(f"File size: {len(content)} characters")
    print(f"File lines: {content.count(chr(10)) + 1}")
    
    # Find all script tags
    script_count = content.count('<script')
    print(f"\nNumber of <script> tags: {script_count}")
    
    # Find key functions
    key_functions = [
        'showTestResults',
        'showSpecificProfile', 
        'showScreen',
        'addEventListener',
        'profileMappings'
    ]
    
    print("\n=== Key Functions/Variables ===")
    for func in key_functions:
        count = content.count(func)
        if count > 0:
            # Find first occurrence
            index = content.find(func)
            line_num = content[:index].count('\n') + 1
            print(f"{func}: found {count} times, first at line {line_num}")
        else:
            print(f"{func}: NOT FOUND")
    
    # Find where script content starts
    script_start = content.find('<script>')
    if script_start != -1:
        script_start_line = content[:script_start].count('\n') + 1
        print(f"\n<script> tag starts at line: {script_start_line}")
    
    # Check if there are multiple script sections
    script_sections = []
    pos = 0
    while True:
        start = content.find('<script', pos)
        if start == -1:
            break
        end = content.find('</script>', start)
        if end == -1:
            break
        script_sections.append((start, end))
        pos = end + 1
    
    print(f"\nFound {len(script_sections)} script sections")
    for i, (start, end) in enumerate(script_sections):
        start_line = content[:start].count('\n') + 1
        end_line = content[:end].count('\n') + 1
        print(f"  Script {i+1}: lines {start_line}-{end_line}")
    
    # Look for console.log statements
    console_logs = content.count('console.log')
    print(f"\nNumber of console.log statements: {console_logs}")
    
    # Check if Z key handler exists
    z_key_checks = [
        "event.key === 'z'",
        'event.key === "z"',
        "Z key pressed"
    ]
    print("\n=== Z Key Handler Checks ===")
    for check in z_key_checks:
        if check in content:
            index = content.find(check)
            line_num = content[:index].count('\n') + 1
            print(f"Found '{check}' at line {line_num}")
            # Show context
            lines = content.split('\n')
            start = max(0, line_num - 3)
            end = min(len(lines), line_num + 3)
            print("  Context:")
            for i in range(start, end):
                print(f"    {i+1}: {lines[i][:80]}...")

if __name__ == "__main__":
    analyze_html_file("/Users/nick/Dropbox/+/AI/stti-assessment/index.html")