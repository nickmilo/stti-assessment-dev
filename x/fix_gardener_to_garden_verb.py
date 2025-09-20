#!/usr/bin/env python3
"""
Fix "tendency to gardener" to "tendency to garden" (verb form)
Following tenet #2: Analyze scope before making changes
"""

def fix_gardener_to_garden_verb():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Finding all instances of 'tendency to gardener'...")
    
    # Count instances first
    instances = content.count('tendency to gardener')
    print(f"Found {instances} instances of 'tendency to gardener'")
    
    if instances > 0:
        # Show context for each instance
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            if 'tendency to gardener' in line:
                print(f"   Line {i}: {line.strip()}")
        
        # Make the replacement
        content = content.replace('tendency to gardener', 'tendency to garden')
        
        # Write back
        with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
            f.write(content)
        
        print(f"✅ Fixed {instances} instances: 'tendency to gardener' → 'tendency to garden'")
    else:
        print("✅ No instances found - all already correct")

if __name__ == "__main__":
    fix_gardener_to_garden_verb()