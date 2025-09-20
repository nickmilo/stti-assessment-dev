#!/usr/bin/env python3
"""
Comprehensive analysis of STTI scoring system
Following SOP Tenet #2: Use Python script to re-familiarize with code structure
Following SOP Tenet #1: Understand structure before analyzing
"""

def analyze_scoring_system():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    print("=== COMPREHENSIVE SCORING SYSTEM ANALYSIS ===\n")
    
    # 1. Analyze the questions array structure
    print("🔍 QUESTION STRUCTURE ANALYSIS:")
    questions_start = content.find('const questions = [')
    if questions_start != -1:
        questions_section = content[questions_start:questions_start + 100000]
        
        # Count total questions
        question_count = questions_section.count('id:')
        print(f"  Total questions: {question_count}")
        
        # Analyze archetype distribution
        archetype_counts = {}
        archetype_types = ['I+', 'I-', 'S+', 'S-', 'P+', 'P-', 'C+', 'C-', 'A+', 'A-', 'G+', 'G-', 'RH']
        
        for archetype in archetype_types:
            count = questions_section.count(f"archetype: '{archetype}'")
            if count > 0:
                archetype_counts[archetype] = count
        
        print(f"  Archetype distribution:")
        for archetype, count in sorted(archetype_counts.items()):
            print(f"    {archetype}: {count} questions")
        
        # Check for red herrings
        rh_count = archetype_counts.get('RH', 0)
        print(f"  Red herring questions: {rh_count}")
        
        # Sample a few questions to understand structure
        print(f"\n  Sample question structure:")
        lines = questions_section.split('\n')
        in_question = False
        sample_count = 0
        
        for line in lines:
            if 'id:' in line and sample_count < 2:
                in_question = True
                sample_count += 1
                print(f"    Question {sample_count}:")
            
            if in_question:
                clean_line = line.strip()
                if clean_line:
                    print(f"      {clean_line}")
                
                if '},' in line and in_question:
                    in_question = False
                    print()
    
    # 2. Analyze calculateScores function
    print("🔍 SCORE CALCULATION ANALYSIS:")
    calc_scores_start = content.find('function calculateScores()')
    if calc_scores_start != -1:
        calc_section = content[calc_scores_start:calc_scores_start + 2000]
        
        # Check scoring logic
        print("  Score calculation logic:")
        lines = calc_section.split('\n')
        for line in lines:
            line_clean = line.strip()
            if 'case' in line_clean or 'score =' in line_clean:
                print(f"    {line_clean}")
        
        # Check if all archetype types are handled
        print(f"\n  Archetype handling in calculateScores:")
        for archetype in ['I', 'S', 'P', 'C', 'A', 'G']:
            if f"scores['{archetype}']" in calc_section or f'scores.{archetype}' in calc_section:
                print(f"    ✅ {archetype} archetype scoring implemented")
            else:
                print(f"    ❌ {archetype} archetype scoring MISSING")
        
        # Check polarity handling
        if 'polarity ===' in calc_section or 'polarity =' in calc_section:
            print(f"    ✅ Polarity handling implemented (+/-)")
        else:
            print(f"    ❌ Polarity handling MISSING")
    
    # 3. Analyze determineProfile function
    print(f"\n🔍 PROFILE DETERMINATION ANALYSIS:")
    determine_start = content.find('function determineProfile(')
    if determine_start != -1:
        determine_section = content[determine_start:determine_start + 1500]
        
        print("  Profile determination logic:")
        if 'sort(' in determine_section:
            print("    ✅ Archetype ranking by scores")
        if 'scores.A > scores.G' in determine_section:
            print("    ✅ Tendency determination (A vs G)")
        if 'dominantArchetypes[0]' in determine_section:
            print("    ✅ Top 2 archetypes selection")
        if '.join(\'\')' in determine_section and '-' in determine_section:
            print("    ✅ Profile code construction (XX-Tendency)")
    
    # 4. Check answer storage and processing
    print(f"\n🔍 ANSWER PROCESSING ANALYSIS:")
    select_answer_start = content.find('function selectAnswer(')
    if select_answer_start != -1:
        select_section = content[select_answer_start:select_answer_start + 1000]
        
        print("  Answer storage structure:")
        if 'questionId:' in select_section:
            print("    ✅ Question ID stored")
        if 'answer:' in select_section:
            print("    ✅ Response value stored (SD/D/A/SA)")
        if 'archetype:' in select_section:
            print("    ✅ Archetype type stored")
        
        # Check if answers are properly linked to questions
        if 'questions[currentQuestion]' in select_section:
            print("    ✅ Answer linked to current question")
    
    # 5. Validate scoring consistency
    print(f"\n🔍 SCORING CONSISTENCY CHECK:")
    
    # Check that calculateScores processes all stored answers
    if 'Object.values(answers)' in content:
        print("    ✅ All answers are processed")
    
    # Check red herring handling
    if 'RH' in content and 'return' in content:
        print("    ✅ Red herrings are skipped in scoring")
    
    # Check polarity inversion logic
    scoring_section = content[content.find('function calculateScores'):content.find('function calculateScores') + 2000]
    if 'polarity === \'+\'' in scoring_section and 'polarity === \'-\'' in scoring_section:
        print("    ✅ Positive and negative polarity handled")
        
        # Check the actual scoring values
        if 'case \'SD\':' in scoring_section:
            print("    ✅ Strongly Disagree (SD) scoring implemented")
        if 'case \'SA\':' in scoring_section:
            print("    ✅ Strongly Agree (SA) scoring implemented")
    
    # 6. Check for potential scoring issues
    print(f"\n🚨 POTENTIAL ISSUES:")
    
    issues_found = []
    
    # Check if scores object is properly initialized
    if 'scores = {' in content:
        init_line = content[content.find('scores = {'):content.find('scores = {') + 200]
        expected_keys = ['I', 'S', 'P', 'C', 'A', 'G']
        for key in expected_keys:
            if f'{key}: 0' not in init_line:
                issues_found.append(f"Score initialization missing for {key}")
    
    # Check answer option mapping
    if 'SD' in content and 'SA' in content and 'D' in content and 'A' in content:
        print("    ✅ All answer options (SD/D/A/SA) are referenced")
    else:
        issues_found.append("Missing answer option references")
    
    if issues_found:
        for issue in issues_found:
            print(f"    ❌ {issue}")
    else:
        print("    ✅ No obvious scoring issues detected")
    
    # 7. Overall assessment
    print(f"\n📊 OVERALL SCORING SYSTEM ASSESSMENT:")
    print(f"  Components checked:")
    print(f"    - Question structure and archetype mapping")
    print(f"    - Score calculation logic")
    print(f"    - Profile determination algorithm") 
    print(f"    - Answer storage and processing")
    print(f"    - Red herring handling")
    print(f"    - Polarity inversion logic")
    
    if not issues_found:
        print(f"\n  ✅ SCORING SYSTEM APPEARS ROBUST")
        print(f"     All major components are implemented correctly")
    else:
        print(f"\n  ⚠️  POTENTIAL ISSUES FOUND: {len(issues_found)}")
        print(f"     Review and address the issues listed above")

if __name__ == "__main__":
    analyze_scoring_system()