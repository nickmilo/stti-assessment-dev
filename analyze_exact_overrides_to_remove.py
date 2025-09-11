#!/usr/bin/env python3
"""
Carefully analyze EXACTLY what needs to be removed in showResults()
Following SOP Tenet #1: Understand what we're changing completely
Following SOP Tenet #2: Use Python to understand structure completely
"""

def analyze_exact_overrides():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING EXACT OVERRIDES TO REMOVE IN SHOWRESULTS ===")
    
    lines = content.split('\n')
    
    # Find showResults function boundaries
    show_results_start = None
    show_results_end = None
    
    for i, line in enumerate(lines, 1):
        if 'function showResults(' in line:
            show_results_start = i
        elif show_results_start and line.strip() == '}' and 'function' in lines[i] if i < len(lines) else False:
            show_results_end = i
            break
    
    if not show_results_start:
        print("❌ Could not find showResults function")
        return
    
    # Look for the actual end by finding the next function
    for i in range(show_results_start, len(lines)):
        if 'function ' in lines[i] and i > show_results_start:
            show_results_end = i - 1
            break
    
    if not show_results_end:
        show_results_end = len(lines)
    
    print(f"showResults function: lines {show_results_start} to {show_results_end}")
    
    # Find where setCollapsibleSections is called
    setcollapsible_call_line = None
    for i in range(show_results_start - 1, show_results_end):
        if 'setCollapsibleSections(profile.code)' in lines[i]:
            setcollapsible_call_line = i + 1
            break
    
    print(f"setCollapsibleSections called at line: {setcollapsible_call_line}")
    
    # Find all lines that override collapsible sections AFTER the setCollapsibleSections call
    override_lines = []
    collapsible_keywords = [
        'overwhelmedTitle.textContent', 'overwhelmedContent.innerHTML',
        'stuckTitle.textContent', 'stuckContent.innerHTML', 
        'promptsTitle.textContent', 'promptsContent.innerHTML'
    ]
    
    search_start = setcollapsible_call_line if setcollapsible_call_line else show_results_start
    
    for i in range(search_start, show_results_end):
        line = lines[i]
        for keyword in collapsible_keywords:
            if keyword in line:
                override_lines.append((i + 1, keyword, line.strip()))
    
    print(f"\n🔍 FOUND {len(override_lines)} OVERRIDE LINES AFTER setCollapsibleSections:")
    
    # Group the overrides by logical blocks
    override_blocks = []
    current_block = []
    current_block_start = None
    
    for line_num, keyword, line_content in override_lines:
        if not current_block_start:
            current_block_start = line_num
            
        current_block.append((line_num, keyword, line_content))
        
        # Check if this is the end of a block (next line is different type or far away)
        if line_num == override_lines[-1][0] or (len(override_lines) > override_lines.index((line_num, keyword, line_content)) + 1 and override_lines[override_lines.index((line_num, keyword, line_content)) + 1][0] > line_num + 5):
            override_blocks.append((current_block_start, line_num, current_block))
            current_block = []
            current_block_start = None
    
    print(f"\nGrouped into {len(override_blocks)} logical blocks:")
    
    for block_start, block_end, block_lines in override_blocks:
        print(f"\n📦 BLOCK: Lines {block_start} to {block_end}")
        print(f"   Contains {len(block_lines)} override lines")
        
        # Show a sample of what this block does
        sample_lines = block_lines[:3]  # First 3 lines of block
        for line_num, keyword, line_content in sample_lines:
            print(f"   Line {line_num}: {line_content[:80]}...")
        
        if len(block_lines) > 3:
            print(f"   ... and {len(block_lines) - 3} more lines")
    
    # Check what comes immediately before and after these blocks to ensure safe removal
    print(f"\n🔍 CONTEXT ANALYSIS FOR SAFE REMOVAL:")
    
    for block_start, block_end, block_lines in override_blocks:
        print(f"\nBlock {block_start}-{block_end} context:")
        
        # Show lines before
        before_start = max(0, block_start - 3)
        print(f"  Lines before ({before_start}-{block_start-1}):")
        for i in range(before_start - 1, block_start - 1):
            if i >= 0 and i < len(lines):
                print(f"    Line {i + 1}: {lines[i].strip()}")
        
        # Show lines after  
        after_end = min(len(lines), block_end + 3)
        print(f"  Lines after ({block_end+1}-{after_end}):")
        for i in range(block_end, after_end):
            if i < len(lines):
                print(f"    Line {i + 1}: {lines[i].strip()}")
    
    print(f"\n🎯 REMOVAL STRATEGY:")
    print("These override blocks should be removed because:")
    print("1. They override the correct content set by setCollapsibleSections()")
    print("2. They use generic orientation-based content instead of specific profile content")
    print("3. Secret codes work because activateProfile() doesn't have these overrides")
    print("4. Assessment completion fails because showResults() has these overrides")
    
    print(f"\n⚠️  SAFETY CHECK:")
    print("Before removal, verify:")
    print("1. No other important logic is mixed in with these overrides")
    print("2. The blocks are cleanly separated from other functionality")
    print("3. Removing them won't break the function structure")
    
    return override_blocks

if __name__ == "__main__":
    analyze_exact_overrides()