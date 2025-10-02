#!/usr/bin/env python3
"""
Script to update image paths in web application files after reorganization.
Updates paths from root directory references to new Assets/Images/ structure.
"""

import os
import re

def update_image_paths():
    """Update image paths in web application files"""
    
    web_app_dir = "/Users/nick/Dropbox/+/AI/STTI Assessment/Web-App"
    
    # Files to update
    files_to_update = [
        "index.html",
        "index-debug.html", 
        "lyt-branded-test.html",
        "simple-test.html",
        "results-sample.html",
        "test-secret-codes.html"
    ]
    
    # Path replacements
    replacements = [
        # Direct image references
        (r'src="Clean_STTI_', r'src="../Assets/Images/Clean_STTI_'),
        (r'src="lyt-logo\.png"', r'src="../Assets/Images/lyt-logo.png"'),
        
        # JavaScript template literals
        (r'`Clean_STTI_\$\{([^}]+)\}_Thin\.png`', r'`../Assets/Images/Clean_STTI_${\\1}_Thin.png`'),
        (r"'Clean_STTI_([^']+)\.png'", r"'../Assets/Images/Clean_STTI_\\1.png'"),
        
        # Font file references
        (r'url\("CanelaDeck-', r'url("../Assets/Fonts/CanelaDeck-'),
    ]
    
    for filename in files_to_update:
        filepath = os.path.join(web_app_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"Skipping {filename} - file not found")
            continue
            
        print(f"Updating {filename}...")
        
        # Read file content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original_content = content
        
        # Apply replacements
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
            
        # Write back if changed
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✓ Updated paths in {filename}")
        else:
            print(f"  - No changes needed in {filename}")

if __name__ == "__main__":
    update_image_paths()
    print("Image path updates complete!")