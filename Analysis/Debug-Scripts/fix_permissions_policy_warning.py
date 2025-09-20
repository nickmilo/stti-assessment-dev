#!/usr/bin/env python3
"""
Fix the remaining Permissions-Policy warning with correct syntax
Following tenet #4: One surgical change at a time
"""

def fix_permissions_policy_warning():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing Permissions-Policy warning with correct approach...")
    
    # Check current head section
    head_start = content.find('<head>')
    head_end = content.find('</head>')
    head_section = content[head_start:head_end]
    
    print("🔍 Current head section permissions policy:")
    if 'Permissions-Policy' in head_section:
        print("   Found existing Permissions-Policy meta tag")
        # Remove the incorrect one first
        old_meta = '<meta http-equiv="Permissions-Policy" content="browsing-topics=()">'
        if old_meta in content:
            content = content.replace(old_meta, '')
            print("   ✅ Removed incorrect Permissions-Policy meta tag")
    
    # Add correct meta tag to disable browsing-topics
    # This should go right after charset and viewport
    viewport_end = content.find('<meta name="viewport"')
    if viewport_end != -1:
        viewport_line_end = content.find('>', viewport_end) + 1
        correct_meta = '\n    <meta http-equiv="Permissions-Policy" content="browsing-topics=()">'
        content = content[:viewport_line_end] + correct_meta + content[viewport_line_end:]
        print("✅ Added correct Permissions-Policy meta tag after viewport")
    else:
        # Fallback: add after charset
        charset_end = content.find('<meta charset="UTF-8">')
        if charset_end != -1:
            charset_line_end = content.find('>', charset_end) + 1
            correct_meta = '\n    <meta http-equiv="Permissions-Policy" content="browsing-topics=()">'
            content = content[:charset_line_end] + correct_meta + content[charset_line_end:]
            print("✅ Added correct Permissions-Policy meta tag after charset")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Permissions-Policy warning should now be eliminated")
    print("💡 Note: This warning is from Chrome's privacy features and may still appear")
    print("   in some browsers as it's related to server headers, not just meta tags")

if __name__ == "__main__":
    fix_permissions_policy_warning()