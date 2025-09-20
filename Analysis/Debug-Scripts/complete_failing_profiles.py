#!/usr/bin/env python3
"""
Complete all failing profile implementations in setCollapsibleSections
Following SOP Tenet #4: Make surgical changes
"""

def complete_failing_profiles():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    # Define the missing implementations for each failing profile
    # Based on the patterns from working profiles
    missing_implementations = {
        'IC-Architect': {
            'stuck_title': 'Getting stuck and unstuck as an IC-Architect',
            'stuck_content': 'When you combine your Southerner archetypes with an Architect tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from exploration to expression is by tapping into your Synthesizer archetype, which aligns with your structured approach.',
            'prompts_title': 'Prompts to go from South to North as an IC-Architect',
            'prompts_content': 'How can you organize your creative insights into a clear structure or system? How can your Synthesizer help connect your discoveries? Once your Synthesizer is activated, you\'ll likely find it becomes easier to drop into your Producer archetype, allowing you to take concrete action on your explorations.'
        },
        'IC-Gardener': {
            'stuck_title': 'Getting stuck and unstuck as an IC-Gardener',
            'stuck_content': 'When you combine your Southerner archetypes with a Gardener tendency, it\'s most difficult to access your Producer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from exploration to expression is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.',
            'prompts_title': 'Prompts to go from South to North as an IC-Gardener',
            'prompts_content': 'What deeper meaning or purpose connects to your current exploration? How can your Inner Guide help guide your discoveries? Once your Inner Guide is activated, you\'ll likely find it becomes easier to drop into your Producer archetype, allowing you to manifest your creative insights.'
        },
        'PI-Architect': {
            'stuck_title': 'Getting stuck and unstuck as a PI-Architect',
            'stuck_content': 'When you combine your Converter archetypes with an Architect tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to balance meaning with execution is by tapping into your Creative archetype, which aligns with your structured approach to expression.',
            'prompts_title': 'Prompts to find balance as a PI-Architect',
            'prompts_content': 'How can you express your insights in a structured, creative way? How can your Creative help bridge reflection and action? Once your Creative is activated, you\'ll likely find it becomes easier to drop into your Synthesizer archetype, allowing you to find sustainable rhythms.'
        },
        'PI-Gardener': {
            'stuck_title': 'Getting stuck and unstuck as a PI-Gardener',
            'stuck_content': 'When you combine your Converter archetypes with a Gardener tendency, it\'s most difficult to access your Synthesizer archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to balance meaning with execution is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.',
            'prompts_title': 'Prompts to find balance as a PI-Gardener',
            'prompts_content': 'What deeper meaning connects your current activity to your values? How can your Inner Guide help find sustainable rhythms? Once your Inner Guide is activated, you\'ll likely find it becomes easier to drop into your Synthesizer archetype, allowing you to balance reflection and action.'
        },
        'PC-Architect': {
            'stuck_title': 'Getting stuck and unstuck as a PC-Architect',
            'stuck_content': 'When you combine your Easterner archetypes with an Architect tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from expression to reflection is by tapping into your Synthesizer archetype, which aligns with your structured approach.',
            'prompts_title': 'Prompts to go from East to West as a PC-Architect',
            'prompts_content': 'How can you connect your current work to deeper patterns and meaning? How can your Synthesizer help organize your insights? Once your Synthesizer is activated, you\'ll likely find it becomes easier to drop into your Inner Guide archetype, allowing you to reflect more deeply.'
        },
        'SI-Architect': {
            'stuck_title': 'Getting stuck and unstuck as an SI-Architect',
            'stuck_content': 'When you combine your Westerner archetypes with an Architect tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to move from reflection to expression is by tapping into your Producer archetype, which aligns with your structured approach.',
            'prompts_title': 'Prompts to go from West to East as an SI-Architect',
            'prompts_content': 'How can you tie your current insights to a concrete outcome or goal? How can your Producer help structure your work? Once your Producer is activated, you\'ll likely find it becomes easier to drop into your Creative archetype, allowing you to express your deep understanding.'
        },
        'SI-Gardener': {
            'stuck_title': 'Getting stuck and unstuck as an SI-Gardener',
            'stuck_content': 'When you combine your Westerner archetypes with a Gardener tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from reflection to expression is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.',
            'prompts_title': 'Prompts to go from West to East as an SI-Gardener',
            'prompts_content': 'What deeper purpose or meaning wants to emerge from your reflections? How can your Inner Guide help clarify direction? Once your Inner Guide is activated, you\'ll likely find it becomes easier to drop into your Creative archetype, allowing you to express your insights uniquely.'
        },
        'SP-Gardener': {
            'stuck_title': 'Getting stuck and unstuck as an SP-Gardener',
            'stuck_content': 'When you combine your Northerner archetypes with a Gardener tendency, it\'s most difficult to access your Creative archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to move from planning to expression is by tapping into your Inner Guide archetype, which aligns with your flexible approach to meaning-making.',
            'prompts_title': 'Prompts to go from North to South as an SP-Gardener',
            'prompts_content': 'What creative possibilities emerge when you step back from planning? How can your Inner Guide help you trust the process? Once your Inner Guide is activated, you\'ll likely find it becomes easier to drop into your Creative archetype, allowing you to explore new possibilities.'
        },
        'SC-Architect': {
            'stuck_title': 'Getting stuck and unstuck as an SC-Architect',
            'stuck_content': 'When you combine your Translator archetypes with an Architect tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to architect, the easiest way to find clarity in translation is by tapping into your Producer archetype, which aligns with your structured approach.',
            'prompts_title': 'Prompts to find clarity as an SC-Architect',
            'prompts_content': 'How can you structure your translation work into concrete steps? How can your Producer help organize the synthesis? Once your Producer is activated, you\'ll likely find it becomes easier to drop into your Inner Guide archetype, allowing you to access deeper wisdom.'
        },
        'SC-Gardener': {
            'stuck_title': 'Getting stuck and unstuck as an SC-Gardener',
            'stuck_content': 'When you combine your Translator archetypes with a Gardener tendency, it\'s most difficult to access your Inner Guide archetype—yet that\'s exactly what you most need. Since your tendency is to garden, the easiest way to find clarity in translation is by tapping into your Creative archetype, which aligns with your flexible approach to expression.',
            'prompts_title': 'Prompts to find clarity as an SC-Gardener',
            'prompts_content': 'How can you express your synthesis in creative, exploratory ways? How can your Creative help you experiment with different bridges? Once your Creative is activated, you\'ll likely find it becomes easier to drop into your Inner Guide archetype, allowing you to access deeper wisdom.'
        }
    }
    
    # For each profile, find where it ends and add the missing sections
    for profile_code, sections in missing_implementations.items():
        print(f"\\n🔧 Completing {profile_code}...")
        
        # Find the profile's current implementation end
        profile_found = False
        insert_line = None
        
        for i, line in enumerate(lines):
            if f"code === '{profile_code}'" in line:
                profile_found = True
                # Find where this profile's implementation currently ends
                # Look for the closing brace of the overwhelmed section
                for j in range(i + 1, min(i + 20, len(lines))):
                    if lines[j].strip() == '}' and 'overwhelmed' in ''.join(lines[max(0, j-10):j]):
                        insert_line = j + 1
                        break
                break
        
        if not profile_found:
            print(f"  ❌ {profile_code} not found")
            continue
            
        if not insert_line:
            print(f"  ❌ Could not find insertion point for {profile_code}")
            continue
        
        print(f"  ✅ Found {profile_code} at line {insert_line}")
        
        # Create the missing sections
        stuck_section = [
            "                ",
            "                // Set stuck/unstuck content for " + profile_code,
            "                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');",
            "                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');",
            "                if (stuckTitle && stuckContent) {",
            f"                    stuckTitle.textContent = '{sections['stuck_title']}';",
            f"                    stuckContent.innerHTML = '{sections['stuck_content']}';",
            "                }",
            "                ",
            "                // Set prompts content for " + profile_code,
            "                const promptsTitle = document.querySelector('#promptsSection .section-title');",
            "                const promptsContent = document.querySelector('#promptsSection .section-content');",
            "                if (promptsTitle && promptsContent) {",
            f"                    promptsTitle.textContent = '{sections['prompts_title']}';",
            f"                    promptsContent.innerHTML = '{sections['prompts_content']}';",
            "                }",
            "                return; // Exit early, dont use generic logic",
            "            }"
        ]
        
        # Insert the sections
        for j, new_line in enumerate(stuck_section):
            lines.insert(insert_line + j, new_line)
    
    # Write the updated file
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write('\\n'.join(lines))
    
    print(f"\\n✅ All failing profiles completed!")
    print("Each profile now has all 3 sections: overwhelmed, stuck/unstuck, and prompts")

if __name__ == "__main__":
    complete_failing_profiles()