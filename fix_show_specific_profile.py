#!/usr/bin/env python3
"""
Fix showSpecificProfile to use the new global functions instead of hardcoded logic
"""

def fix_show_specific_profile():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Replacing showSpecificProfile with activateProfile call...")
    
    # Find the showTestResults function and replace the call
    old_call = "showSpecificProfile(mockProfile);"
    new_call = "activateProfile(mockProfile.code, 'Test Profile');"
    
    if old_call in content:
        content = content.replace(old_call, new_call)
        print("✅ Updated showTestResults to call activateProfile instead of showSpecificProfile")
    else:
        print("❌ Could not find showSpecificProfile call in showTestResults")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Secret codes will now use the new global functions")
    print("✅ This should fix the 'setTendencyPills is not defined' error")

if __name__ == "__main__":
    fix_show_specific_profile()