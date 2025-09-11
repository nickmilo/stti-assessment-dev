#!/usr/bin/env python3
"""
Comprehensive debug script for SP-Architect collapsible sections issue
Following SOP Tenet #2: Use Python to understand structure completely
"""

import re
import unicodedata
import jsbeautifier

def debug_sp_architect_comprehensive():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("=== COMPREHENSIVE SP-ARCHITECT DEBUG ANALYSIS ===")
    
    lines = content.split('\n')
    total_lines = len(lines)
    
    print(f"File has {total_lines} total lines")
    
    # 1. Find SP-Architect case and check for exact string issues
    print("\n🔍 1. EXACT STRING MATCHING ANALYSIS:")
    
    sp_architect_lines = []
    for i, line in enumerate(lines, 1):
        if 'SP-Architect' in line:
            sp_architect_lines.append((i, line))
    
    print(f"Found {len(sp_architect_lines)} lines containing 'SP-Architect':")
    for line_num, line in sp_architect_lines:
        # Check for hidden characters
        clean_line = line.strip()
        print(f"  Line {line_num}: {repr(clean_line)}")  # repr shows hidden chars
        
        # Check if this is the if statement
        if "if (code === 'SP-Architect')" in line:
            print(f"    ✅ Found SP-Architect condition at line {line_num}")
            
            # Check character by character for the comparison string
            match = re.search(r"code === ['\"]([^'\"]*)['\"]", line)
            if match:
                profile_string = match.group(1)
                print(f"    Profile string: {repr(profile_string)}")
                print(f"    Length: {len(profile_string)}")
                print(f"    Unicode categories: {[unicodedata.category(c) for c in profile_string]}")
                
                if profile_string != 'SP-Architect':
                    print(f"    ❌ STRING MISMATCH! Expected 'SP-Architect', found {repr(profile_string)}")
                else:
                    print(f"    ✅ String matches exactly")
    
    # 2. Check function boundaries and scope
    print("\n🔍 2. FUNCTION SCOPE ANALYSIS:")
    
    # Find setCollapsibleSections function
    func_starts = []
    func_ends = []
    
    for i, line in enumerate(lines, 1):
        if 'function setCollapsibleSections' in line:
            func_starts.append(i)
        elif 'console.error(\'setCollapsibleSections: Unknown profile code:\'' in line:
            func_ends.append(i)
    
    print(f"Function starts: {func_starts}")
    print(f"Function ends: {func_ends}")
    
    if func_starts and func_ends:
        func_start = func_starts[0]
        func_end = func_ends[0]
        
        # Check if SP-Architect is within function bounds
        sp_in_function = any(func_start <= line_num <= func_end for line_num, _ in sp_architect_lines if "if (code ===" in _)
        print(f"SP-Architect within function bounds: {'✅ YES' if sp_in_function else '❌ NO'}")
    
    # 3. Check for legacy code after line 2337
    print(f"\n🔍 3. LEGACY CODE ANALYSIS (lines 2337-{total_lines}):")
    
    legacy_start = 2337
    if legacy_start < total_lines:
        legacy_content = lines[legacy_start-1:]  # 0-indexed
        
        # Look for duplicate function definitions
        duplicate_functions = []
        for i, line in enumerate(legacy_content, legacy_start):
            if 'function setCollapsibleSections' in line:
                duplicate_functions.append(i)
            elif 'setCollapsibleSections =' in line:
                duplicate_functions.append(i)
        
        if duplicate_functions:
            print(f"❌ DUPLICATE FUNCTION DEFINITIONS FOUND:")
            for line_num in duplicate_functions:
                print(f"  Line {line_num}: {lines[line_num-1].strip()}")
        else:
            print("✅ No duplicate function definitions found")
        
        # Look for code that might override or interfere
        suspicious_patterns = [
            'setCollapsibleSections',
            'SP-Architect',
            'overwhelmedSection',
            'stuckUnstuckSection', 
            'promptsSection'
        ]
        
        suspicious_lines = []
        for pattern in suspicious_patterns:
            for i, line in enumerate(legacy_content, legacy_start):
                if pattern in line and not line.strip().startswith('//'):
                    suspicious_lines.append((i, pattern, line.strip()))
        
        if suspicious_lines:
            print(f"\n⚠️  SUSPICIOUS PATTERNS IN LEGACY CODE:")
            for line_num, pattern, line in suspicious_lines[:10]:  # Show first 10
                print(f"  Line {line_num} ({pattern}): {line[:100]}...")
        else:
            print("✅ No suspicious patterns in legacy code")
    
    # 4. Check for JavaScript syntax errors around SP-Architect
    print(f"\n🔍 4. JAVASCRIPT SYNTAX ANALYSIS:")
    
    # Extract just the SP-Architect case for syntax checking
    sp_case_start = None
    sp_case_end = None
    
    for i, line in enumerate(lines, 1):
        if "if (code === 'SP-Architect')" in line:
            sp_case_start = i
        elif sp_case_start and "return; // Exit early, don't use generic logic" in line and i > sp_case_start:
            sp_case_end = i
            break
    
    if sp_case_start and sp_case_end:
        print(f"SP-Architect case: lines {sp_case_start} to {sp_case_end}")
        
        sp_code = '\n'.join(lines[sp_case_start-1:sp_case_end])
        
        # Check for common syntax issues
        syntax_issues = []
        
        # Check balanced quotes
        single_quotes = sp_code.count("'") - sp_code.count("\\'")
        double_quotes = sp_code.count('"') - sp_code.count('\\"')
        
        if single_quotes % 2 != 0:
            syntax_issues.append("Unmatched single quotes")
        if double_quotes % 2 != 0:
            syntax_issues.append("Unmatched double quotes")
        
        # Check balanced braces
        if sp_code.count('{') != sp_code.count('}'):
            syntax_issues.append("Unmatched braces")
        
        # Check balanced parentheses  
        if sp_code.count('(') != sp_code.count(')'):
            syntax_issues.append("Unmatched parentheses")
        
        if syntax_issues:
            print(f"❌ SYNTAX ISSUES FOUND: {', '.join(syntax_issues)}")
        else:
            print("✅ No obvious syntax issues found")
            
        # Try to beautify the JavaScript
        try:
            beautified = jsbeautifier.beautify(sp_code)
            print("✅ JavaScript beautification successful")
        except Exception as e:
            print(f"❌ JavaScript beautification failed: {e}")
    
    # 5. Check for function call issues
    print(f"\n🔍 5. FUNCTION CALL ANALYSIS:")
    
    # Find all calls to setCollapsibleSections
    function_calls = []
    for i, line in enumerate(lines, 1):
        if 'setCollapsibleSections(' in line and 'function' not in line:
            function_calls.append((i, line.strip()))
    
    print(f"Found {len(function_calls)} calls to setCollapsibleSections:")
    for line_num, call in function_calls:
        print(f"  Line {line_num}: {call}")
        
        # Extract the parameter being passed
        match = re.search(r'setCollapsibleSections\(([^)]+)\)', call)
        if match:
            param = match.group(1)
            print(f"    Parameter: {param}")
    
    # 6. Final diagnosis
    print(f"\n🎯 DIAGNOSIS & RECOMMENDATIONS:")
    
    print("Possible causes of 'Unknown profile code: SP-Architect' error:")
    print("1. Character encoding issue in string comparison")
    print("2. Legacy code overriding the function after line 2337")  
    print("3. JavaScript execution error preventing SP-Architect case from being reached")
    print("4. Browser caching old version of the code")
    print("5. Function being called with incorrect parameter format")
    
    print(f"\n🔧 NEXT DEBUGGING STEPS:")
    print("1. Add console.log at start of setCollapsibleSections to see exact input")
    print("2. Add console.log right before SP-Architect case")
    print("3. Check browser console for JavaScript errors")
    print("4. Hard refresh browser (Cmd+Shift+R)")
    print("5. Check if legacy code after line 2337 is interfering")

if __name__ == "__main__":
    debug_sp_architect_comprehensive()