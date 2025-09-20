#!/usr/bin/env python3
"""
Analyze potential variable naming issue with westernerDesc
Following SOP Tenet #2: Use Python to understand structure completely
"""

def analyze_westerner_desc_issue():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== ANALYZING WESTERNER DESC VARIABLE NAMING ISSUE ===")
    print("Checking lines around 2473 and 2491 as suggested by user\n")
    
    lines = content.split('\n')
    
    # 1. Find all westernerDesc variable usages
    print("🔍 FINDING ALL WESTERNER DESC REFERENCES:")
    westerner_desc_refs = []
    
    for i, line in enumerate(lines, 1):
        if 'westernerDesc' in line:
            westerner_desc_refs.append((i, line.strip()))
    
    print(f"Found {len(westerner_desc_refs)} references to westernerDesc:")
    for line_num, line_content in westerner_desc_refs:
        print(f"  Line {line_num}: {line_content}")
    
    # 2. Analyze the context around lines 2473 and 2491
    print(f"\n🔍 CONTEXT AROUND SUGGESTED LINES:")
    
    target_lines = [2473, 2491]
    for target_line in target_lines:
        if target_line <= len(lines):
            print(f"\nLine {target_line} context:")
            start = max(0, target_line - 5)
            end = min(len(lines), target_line + 5)
            
            for i in range(start, end):
                marker = ">>> " if i + 1 == target_line else "    "
                print(f"{marker}Line {i + 1}: {lines[i]}")
    
    # 3. Check the pattern - does westernerDesc get used for ALL orientations?
    print(f"\n🔍 ANALYZING USAGE PATTERN:")
    
    # Find the function that contains these references
    for line_num, line_content in westerner_desc_refs:
        if 'const westernerDesc' in line_content:
            print(f"\nVariable declared at line {line_num}: {line_content}")
            
            # Look for usage in different orientation blocks
            func_start = max(0, line_num - 10)
            func_end = min(len(lines), line_num + 200)  # Reasonable function size
            
            orientations_found = []
            for i in range(func_start, func_end):
                line = lines[i]
                if 'orientation ===' in line:
                    # Extract orientation name
                    if "'Westerner'" in line:
                        orientations_found.append(('Westerner', i + 1))
                    elif "'Easterner'" in line:
                        orientations_found.append(('Easterner', i + 1))
                    elif "'Northerner'" in line:
                        orientations_found.append(('Northerner', i + 1))
                    elif "'Southerner'" in line:
                        orientations_found.append(('Southerner', i + 1))
                    elif "'Diagonal'" in line:
                        orientations_found.append(('Diagonal', i + 1))
            
            print(f"\nOrientations handled in this function:")
            for orientation, ori_line in orientations_found:
                print(f"  Line {ori_line}: {orientation}")
                
                # Check if westernerDesc is used in each orientation block
                block_start = ori_line
                block_end = min(len(lines), ori_line + 20)  # Look ahead in block
                
                westerner_usage_in_block = []
                for j in range(block_start, block_end):
                    if 'westernerDesc' in lines[j] and j + 1 != line_num:  # Exclude declaration line
                        westerner_usage_in_block.append(j + 1)
                
                if westerner_usage_in_block:
                    print(f"    westernerDesc used at lines: {westerner_usage_in_block}")
                else:
                    print(f"    No westernerDesc usage found in this block")
    
    # 4. The core issue analysis
    print(f"\n📋 ISSUE ANALYSIS:")
    print("The variable 'westernerDesc' suggests it's specifically for Westerner orientation,")
    print("but if it's being used for ALL orientations (Easterner, Northerner, etc.),")
    print("this creates semantic confusion and potential bugs.")
    print("\nPossible issues:")
    print("1. Developer confusion: 'westernerDesc' used for Easterner content")
    print("2. Copy-paste errors: Someone might assume it only applies to Westerners")
    print("3. Maintenance issues: Unclear what the variable actually represents")
    
    # 5. Recommendation
    print(f"\n🔧 RECOMMENDED SOLUTION:")
    print("Rename 'westernerDesc' to 'orientationDesc' to match the semantic meaning.")
    print("This aligns with the orientationDescription rename we just did.")
    print("Both variables reference the same DOM element and serve the same purpose.")
    
    # 6. Check if this could be related to SP-Architect issue
    print(f"\n🎯 CONNECTION TO SP-ARCHITECT ISSUE:")
    print("If there's confusion about orientation variables, it could contribute to")
    print("the 'Unknown profile code: SP-Architect' error by affecting how")
    print("profile data flows through the orientation determination logic.")
    
    return westerner_desc_refs

if __name__ == "__main__":
    analyze_westerner_desc_issue()