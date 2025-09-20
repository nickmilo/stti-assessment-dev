#!/usr/bin/env python3
"""
Extract PS-Architect current implementation to understand what user is seeing
Following SOP Tenet #2: Use Python scripts to re-familiarize with code
"""

def extract_ps_architect_implementation():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== PS-ARCHITECT CURRENT IMPLEMENTATION ===\n")
    
    # Find PS-Architect block in setCollapsibleSections
    start = content.find("code === 'PS-Architect'")
    if start != -1:
        # Find the end of the block (return statement)
        end = content.find('return; // Exit early', start)
        if end != -1:
            ps_block = content[start:end+25]
            print("📋 Current PS-Architect implementation:")
            print(ps_block)
            
            # Check for specific content that should be there
            print("\n🔍 Content Analysis:")
            if "Creative" in ps_block:
                print("✅ Contains 'Creative' reference")
            else:
                print("❌ Missing 'Creative' reference")
                
            if "Inner Guide" in ps_block:
                print("✅ Contains 'Inner Guide' reference")
            else:
                print("❌ Missing 'Inner Guide' reference")
                
            if "Northerner" in ps_block:
                print("✅ Contains 'Northerner' reference")
            else:
                print("❌ Missing 'Northerner' reference")
                
            if "Producer" in ps_block:
                print("✅ Contains 'Producer' reference")
            else:
                print("❌ Missing 'Producer' reference")
                
            if "Synthesizer" in ps_block:
                print("✅ Contains 'Synthesizer' reference")
            else:
                print("❌ Missing 'Synthesizer' reference")
        else:
            print("❌ Could not find end of PS-Architect block")
    else:
        print("❌ PS-Architect not found in setCollapsibleSections")
        print("   This means it would fall back to generic content")
        
        # Check if it exists at all
        if "PS-Architect" in content:
            print("✅ PS-Architect exists somewhere in the file")
            # Find all occurrences
            occurrences = []
            start_search = 0
            while True:
                pos = content.find("PS-Architect", start_search)
                if pos == -1:
                    break
                # Get line number
                line_num = content[:pos].count('\n') + 1
                occurrences.append(line_num)
                start_search = pos + 1
            
            print(f"   Found PS-Architect at lines: {occurrences}")
        else:
            print("❌ PS-Architect not found anywhere in the file")

if __name__ == "__main__":
    extract_ps_architect_implementation()