#!/usr/bin/env python3
"""
Script to update all folder path references after renaming stti-assessment to "STTI Assessment"
"""

import os
import glob
import re

def update_all_paths():
    """Update all path references in Python scripts"""
    
    # Base directory for analysis scripts
    base_dir = "/Users/nick/Dropbox/+/AI/STTI Assessment/Analysis"
    
    # Find all Python files
    py_files = []
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith('.py'):
                py_files.append(os.path.join(root, file))
    
    old_path = "/Users/nick/Dropbox/+/AI/STTI Assessment/"
    new_path = "/Users/nick/Dropbox/+/AI/STTI Assessment/"
    
    updated_count = 0
    
    for filepath in py_files:
        try:
            # Read file content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check if it contains the old path
            if old_path in content:
                # Replace old path with new path
                updated_content = content.replace(old_path, new_path)
                
                # Write back the updated content
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                    
                print(f"✓ Updated: {os.path.basename(filepath)}")
                updated_count += 1
            
        except Exception as e:
            print(f"✗ Error updating {filepath}: {e}")
    
    print(f"\nUpdate complete! {updated_count} files updated.")

if __name__ == "__main__":
    update_all_paths()