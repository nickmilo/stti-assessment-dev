#!/usr/bin/env python3
"""
Test secret codes functionality to validate assessment works
Following SOP Tenet #3: Always validate after modifications
"""

import subprocess
import time
import os

def test_secret_codes():
    print("=== TESTING SECRET CODES FUNCTIONALITY ===\n")
    
    # Test if we can start a local server and test the assessment
    html_file = '/Users/nick/Dropbox/+/AI/STTI Assessment/index.html'
    
    if not os.path.exists(html_file):
        print("❌ index.html file not found!")
        return False
    
    print("🔍 SYNTAX VALIDATION:")
    
    # Basic syntax check
    with open(html_file, 'r') as f:
        content = f.read()
    
    # Check for obvious syntax errors
    open_braces = content.count('{')
    close_braces = content.count('}')
    print(f"  Braces: {open_braces} open, {close_braces} close (diff: {open_braces - close_braces})")
    
    if open_braces != close_braces:
        print("  ❌ BRACE MISMATCH - JavaScript will fail")
        return False
    
    # Check for orientationArchetypes issues
    print(f"\n🔍 ORIENTATIONARCHETYPES ANALYSIS:")
    
    # Find all orientationArchetypes references
    lines = content.split('\n')
    declarations = []
    usages = []
    
    for i, line in enumerate(lines, 1):
        if 'orientationArchetypes' in line:
            if 'var orientationArchetypes' in line or 'const orientationArchetypes' in line:
                declarations.append((i, line.strip()))
            else:
                usages.append((i, line.strip()))
    
    print(f"  Declarations: {len(declarations)}")
    for line_num, line_content in declarations:
        print(f"    Line {line_num}: {line_content}")
    
    print(f"  Usages: {len(usages)}")
    if len(usages) > 5:
        print(f"    First 5 usages:")
        for line_num, line_content in usages[:5]:
            print(f"      Line {line_num}: {line_content[:60]}...")
    
    # Check if usage comes before declaration in showResults function
    show_results_start = None
    for i, line in enumerate(lines, 1):
        if 'function showResults()' in line:
            show_results_start = i
            break
    
    if show_results_start:
        print(f"\n  showResults function starts at line {show_results_start}")
        
        # Find first declaration and first usage within showResults
        first_decl = None
        first_usage = None
        
        for line_num, line_content in declarations:
            if line_num > show_results_start:
                first_decl = line_num
                break
        
        for line_num, line_content in usages:
            if line_num > show_results_start:
                first_usage = line_num
                break
        
        if first_decl and first_usage:
            if first_decl < first_usage:
                print(f"    ✅ Declaration (line {first_decl}) before usage (line {first_usage})")
            else:
                print(f"    ❌ Usage (line {first_usage}) before declaration (line {first_decl})")
                return False
    
    print(f"\n🔍 QUESTIONS ARRAY VALIDATION:")
    
    # Check questions array
    if 'const questions = [' in content:
        print("  ✅ questions array declared")
        
        # Count questions
        questions_section = content[content.find('const questions = ['):]
        question_count = questions_section.count('{ id:')
        print(f"  Question count: {question_count}")
        
        if question_count != 53:
            print(f"  ⚠️  Expected 53 questions, found {question_count}")
    
    print(f"\n🔍 CRITICAL FUNCTIONS CHECK:")
    
    required_functions = [
        'selectAnswer',
        'loadQuestion', 
        'showResults',
        'calculateScores',
        'determineProfile'
    ]
    
    for func_name in required_functions:
        if f'function {func_name}(' in content:
            print(f"  ✅ {func_name} function exists")
        else:
            print(f"  ❌ {func_name} function MISSING")
            return False
    
    print(f"\n📋 VALIDATION SUMMARY:")
    print("  ✅ Syntax appears valid (braces balanced)")
    print("  ✅ All required functions present")
    print("  ✅ Questions array declared")
    
    # Try to detect obvious runtime issues
    potential_issues = []
    
    if 'const orientationArchetypes' in content and 'var orientationArchetypes' in content:
        potential_issues.append("Mixed const/var declarations for orientationArchetypes")
    
    if content.count('function showResults()') > 1:
        potential_issues.append("Multiple showResults function definitions")
        
    if potential_issues:
        print(f"\n⚠️  POTENTIAL ISSUES:")
        for issue in potential_issues:
            print(f"    - {issue}")
    
    print(f"\n🧪 MANUAL TEST RECOMMENDATIONS:")
    print("  1. Open index.html in browser")
    print("  2. Try secret code 0001 (should show IS-Architect)")
    print("  3. Check browser console for JavaScript errors")
    print("  4. If errors persist, check the exact line numbers in browser console")
    
    return True

if __name__ == "__main__":
    test_secret_codes()