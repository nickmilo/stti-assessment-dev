#!/usr/bin/env python3
"""
Identify the exact range of lines to remove for surgical fix
Following SOP Tenet #2: Use Python to understand structure completely
Following SOP Tenet #4: Make surgical changes
"""

def identify_removal_range():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    print("=== IDENTIFYING EXACT REMOVAL RANGE ===")
    
    # Find start of override section
    override_start = None
    for i, line in enumerate(lines, 1):
        if '// Update overwhelmed section content based on orientation' in line:
            override_start = i
            break
    
    if not override_start:
        # Alternative search
        for i, line in enumerate(lines, 1):
            if 'overwhelmedTitle = overwhelmedSection.querySelector' in line:
                # Look backwards for the comment
                for j in range(i-5, i):
                    if j > 0 and 'Update overwhelmed' in lines[j-1]:
                        override_start = j
                        break
                if not override_start:
                    override_start = i - 1  # Start just before the const declaration
                break
    
    # Find end of override section  
    override_end = None
    if override_start:
        # Look for the next major section that's not override-related
        for i in range(override_start + 50, len(lines)):
            line = lines[i-1]  # 0-indexed
            if ('// Update chord diagram' in line or 
                'chordImage.src' in line or
                'function ' in line):
                override_end = i - 1  # Line before the next section
                break
    
    print(f"Override section: lines {override_start} to {override_end}")
    
    if override_start and override_end:
        print(f"\n🔍 CONTENT TO BE REMOVED ({override_end - override_start + 1} lines):")
        
        # Show first few lines
        print("First 5 lines:")
        for i in range(override_start - 1, min(override_start + 4, override_end)):
            print(f"  Line {i + 1}: {lines[i].strip()}")
        
        print("...")
        
        # Show last few lines
        print("Last 5 lines:")
        for i in range(max(override_start - 1, override_end - 5), override_end):
            print(f"  Line {i + 1}: {lines[i].strip()}")
    
    # Show context before and after
    if override_start:
        print(f"\n🔍 CONTEXT BEFORE (lines {override_start-3} to {override_start-1}):")
        for i in range(max(0, override_start - 4), override_start - 1):
            print(f"  Line {i + 1}: {lines[i].strip()}")
    
    if override_end:
        print(f"\n🔍 CONTEXT AFTER (lines {override_end+1} to {override_end+3}):")
        for i in range(override_end, min(len(lines), override_end + 3)):
            print(f"  Line {i + 1}: {lines[i].strip()}")
    
    # Safety check - make sure we're not removing anything critical
    print(f"\n🔍 SAFETY CHECK:")
    if override_start and override_end:
        section_content = '\n'.join(lines[override_start-1:override_end])
        
        # Check for any function definitions
        if 'function ' in section_content:
            print("⚠️  WARNING: Function definitions found in removal section!")
        else:
            print("✅ No function definitions in removal section")
        
        # Check for any important non-override code
        critical_patterns = ['setCollapsibleSections(', 'getElementById(', 'addEventListener']
        critical_found = []
        for pattern in critical_patterns:
            if pattern in section_content and 'overwhelmed' not in section_content.split(pattern)[0].split('\n')[-1]:
                critical_found.append(pattern)
        
        if critical_found:
            print(f"⚠️  WARNING: Critical patterns found: {critical_found}")
        else:
            print("✅ No critical patterns found that aren't override-related")
    
    return override_start, override_end

if __name__ == "__main__":
    identify_removal_range()