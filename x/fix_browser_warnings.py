#!/usr/bin/env python3
"""
Fix browser console warnings
Following tenet #4: One surgical change at a time
"""

def fix_browser_warnings():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Fixing browser console warnings...")
    
    # 1. Fix favicon.ico 404 error by adding favicon link in head
    head_end = content.find('</head>')
    if head_end != -1:
        # Check if favicon already exists
        if 'favicon.ico' not in content:
            favicon_link = '    <link rel="icon" href="data:," type="image/x-icon">\n'
            content = content[:head_end] + favicon_link + content[head_end:]
            print("✅ Added empty favicon to prevent 404 error")
        else:
            print("✅ Favicon already exists")
    
    # 2. Fix Permissions-Policy header warning by adding meta tag
    if 'Permissions-Policy' not in content:
        meta_tag = '    <meta http-equiv="Permissions-Policy" content="browsing-topics=()">\n'
        content = content[:head_end] + meta_tag + content[head_end:]
        print("✅ Added Permissions-Policy meta tag to suppress browsing-topics warning")
    else:
        print("✅ Permissions-Policy already configured")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ Browser console warnings should be eliminated")

if __name__ == "__main__":
    fix_browser_warnings()