#!/usr/bin/env python3
"""
Analyze hardcoded IS-Architect content issue
Following SOP Tenet #2: Use Python script to understand full structure
"""

def analyze_hardcoded_content():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING HARDCODED IS-ARCHITECT CONTENT ===")
    print("IC-Architect showing IS-Architect content - lines 2618-2643 suspected\n")
    
    lines = content.split('\n')
    
    # 1. Check lines 2618-2643 as mentioned
    print("🔍 EXAMINING LINES 2618-2643:")
    for i in range(2617, 2644):
        if i < len(lines):
            line = lines[i]
            if any(text in line for text in ['IS-Architect', 'Westerner', 'overwhelmed', 'stuck', 'prompts']):
                print(f"  Line {i + 1}: {line.strip()[:80]}...")
    
    # 2. Search for all IS-Architect hardcoded content
    print(f"\n🔍 SEARCHING FOR HARDCODED IS-ARCHITECT CONTENT:")
    
    is_architect_refs = []
    for i, line in enumerate(lines, 1):
        # Look for IS-Architect specific text from the screenshot
        if ('When Westerners feel overwhelmed' in line or 
            'Getting stuck and unstuck as an IS-Architect' in line or
            'Prompts to go from West to East as an IS-Architect' in line or
            'They usually double-down on their strengths' in line):
            is_architect_refs.append((i, line.strip()))
    
    if is_architect_refs:
        print("Found hardcoded IS-Architect content:")
        for line_num, content in is_architect_refs:
            print(f"  Line {line_num}: {content[:80]}...")
    
    # 3. Find the context of lines 2618-2643
    print(f"\n🔍 FUNCTION CONTEXT FOR LINES 2618-2643:")
    
    # Find what function contains these lines
    for i, line in enumerate(lines, 1):
        if 'function ' in line and i < 2618:
            func_name = line.strip().split('function ')[1].split('(')[0] if 'function ' in line else ''
            # Check if this function extends past line 2618
            brace_count = 0
            func_start = i
            for j in range(i - 1, len(lines)):
                brace_count += lines[j].count('{') - lines[j].count('}')
                if brace_count == 0 and j > i:
                    if j >= 2618:
                        print(f"Lines 2618-2643 are in function: {func_name} (starts at line {func_start})")
                    break
    
    # 4. Check what activateProfile does
    print(f"\n🔍 CHECKING ACTIVATEPROFILE FUNCTION:")
    
    activate_start = None
    for i, line in enumerate(lines, 1):
        if 'function activateProfile(' in line:
            activate_start = i
            print(f"activateProfile starts at line {i}")
            break
    
    if activate_start:
        # Check if activateProfile has hardcoded content
        for i in range(activate_start - 1, min(activate_start + 100, len(lines))):
            line = lines[i]
            if ('overwhelmedSection' in line or 'stuckUnstuckSection' in line or 
                'promptsSection' in line or 'querySelector' in line):
                print(f"  Line {i + 1}: {line.strip()[:80]}...")
    
    # 5. Look for duplicate content setting
    print(f"\n🔍 CHECKING FOR DUPLICATE CONTENT SETTING:")
    
    # Find all places where collapsible content is set
    content_setters = []
    for i, line in enumerate(lines, 1):
        if ('overwhelmedTitle.textContent' in line or 
            'overwhelmedContent.innerHTML' in line or
            'stuckTitle.textContent' in line or
            'stuckContent.innerHTML' in line or
            'promptsTitle.textContent' in line or
            'promptsContent.innerHTML' in line):
            content_setters.append((i, line.strip()[:80]))
    
    print(f"Found {len(content_setters)} places where collapsible content is set:")
    # Group by proximity
    if content_setters:
        current_group_start = content_setters[0][0]
        print(f"\nGroup starting at line {current_group_start}:")
        
        for i, (line_num, content) in enumerate(content_setters):
            if line_num - current_group_start > 50:
                current_group_start = line_num
                print(f"\nGroup starting at line {current_group_start}:")
            print(f"  Line {line_num}: {content}...")
    
    print(f"\n📋 DIAGNOSIS:")
    print("If lines 2618-2643 contain hardcoded IS-Architect content")
    print("that runs AFTER setCollapsibleSections sets the correct content,")
    print("then this hardcoded content will override the profile-specific content.")
    print("\nSOLUTION: Remove or comment out the hardcoded content.")

if __name__ == "__main__":
    analyze_hardcoded_content()