#!/usr/bin/env python3
"""
Fix tendency verb forms by replacing tendency.toLowerCase() with proper verb mapping
"""

def fix_tendency_verb_form():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing tendency verb forms...")
    
    # Count instances of the pattern
    pattern = '${tendency.toLowerCase()}'
    instances = content.count(pattern)
    print(f"Found {instances} instances of the tendency.toLowerCase() pattern")
    
    # Replace with proper verb mapping
    old_pattern = '${tendency.toLowerCase()}'
    new_pattern = '${tendency === "Architect" ? "architect" : "garden"}'
    
    content = content.replace(old_pattern, new_pattern)
    
    # Also check for any hardcoded instances like "tendency to gardener"
    hardcoded_instances = content.count('tendency to gardener')
    if hardcoded_instances > 0:
        content = content.replace('tendency to gardener', 'tendency to garden')
        print(f"✅ Also fixed {hardcoded_instances} hardcoded instances")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print(f"✅ Fixed {instances} instances:")
    print("   - 'tendency to architect' (when Architect)")
    print("   - 'tendency to garden' (when Gardener)")

if __name__ == "__main__":
    fix_tendency_verb_form()