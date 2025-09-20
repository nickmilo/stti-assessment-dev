#!/usr/bin/env python3
"""
Test the live assessment to see what's actually happening
Following Tenet #5: Use proper tools
"""

import subprocess
import time

def test_live_assessment():
    print("=== TESTING LIVE ASSESSMENT ===")
    print("Opening live site to check console errors...")
    
    # Open the live site
    url = "https://nickmilo.github.io/stti-assessment/"
    
    try:
        # Open in default browser
        if subprocess.call(['open', url]) == 0:
            print(f"✅ Opened {url}")
        else:
            print(f"❌ Failed to open {url}")
    except:
        print(f"❌ Error opening browser")
    
    print("\n🔍 MANUAL TESTING STEPS:")
    print("1. Check browser console for JavaScript errors")
    print("2. Enter email and complete assessment")
    print("3. On results page, check if collapsible sections exist in DOM")
    print("4. Look for these specific elements:")
    print("   - #overwhelmedSection")
    print("   - #stuckUnstuckSection") 
    print("   - #promptsSection")
    print("5. Check if setCollapsibleSections() was called in console")
    
    print(f"\n🧪 DEBUGGING IN BROWSER:")
    print("Open browser console and run:")
    print("console.log('Testing setCollapsibleSections...');")
    print("setCollapsibleSections('IS-Architect');")
    print("console.log('Sections after call:', document.querySelectorAll('.section-title').length);")
    
    print(f"\n🔍 CHECK EXACT ELEMENTS:")
    print("In browser console, check if elements exist:")
    print("document.getElementById('overwhelmedSection')")
    print("document.getElementById('stuckUnstuckSection')")
    print("document.getElementById('promptsSection')")
    
    return True

if __name__ == "__main__":
    test_live_assessment()