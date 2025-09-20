#!/usr/bin/env python3
"""
Add debugging to see exactly what profile code is being passed to setCollapsibleSections
Following SOP Tenet #2: Use Python to understand structure completely
"""

def add_debug_logging():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ADDING DEBUG LOGGING TO SETCOLLAPSIBLESECTIONS ===")
    
    lines = content.split('\n')
    
    # Find the start of setCollapsibleSections function
    func_start = None
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections(code)' in line:
            func_start = i
            break
    
    if not func_start:
        print("❌ Could not find setCollapsibleSections function")
        return
    
    print(f"Found function at line {func_start}")
    
    # Add debug logging right after the function declaration
    debug_code = [
        "            // DEBUG: Log exactly what profile code we received",
        "            console.log('=== setCollapsibleSections DEBUG ===');",
        "            console.log('Received code:', JSON.stringify(code));", 
        "            console.log('Code type:', typeof code);",
        "            console.log('Code length:', code ? code.length : 'null/undefined');",
        "            console.log('Code charCodes:', code ? Array.from(code).map(c => c.charCodeAt(0)) : 'null/undefined');",
        "            console.log('Expected: SP-Architect');",
        "            console.log('Match test:', code === 'SP-Architect');",
        "            console.log('=====================================');"
    ]
    
    # Find where to insert the debug code (after the function line and const line)
    insert_line = func_start + 2  # After function declaration and const [archetypes, tendency] line
    
    # Insert the debug code
    for j, debug_line in enumerate(debug_code):
        lines.insert(insert_line + j - 1, debug_line)
    
    # Write back the modified content
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write('\n'.join(lines))
    
    print(f"✅ Added debug logging at line {insert_line}")
    print("This will show exactly what profile code is being passed to setCollapsibleSections")
    print("Check browser console when running assessment to see debug output")

if __name__ == "__main__":
    add_debug_logging()