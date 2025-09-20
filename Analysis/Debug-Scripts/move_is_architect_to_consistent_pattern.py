#!/usr/bin/env python3
"""
Move IS-Architect to setCollapsibleSections pattern for consistency
Following tenet #4: One surgical change at a time
"""

def move_is_architect_to_consistent_pattern():
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
        content = f.read()
    
    print("Moving IS-Architect to setCollapsibleSections pattern...")
    
    # 1. Extract the collapsible sections content from loadISArchitectContent
    start = content.find('function loadISArchitectContent() {')
    if start == -1:
        print("❌ Could not find loadISArchitectContent function")
        return
    
    end = content.find('function ', start + 1)
    if end == -1:
        end = len(content)
    
    load_function = content[start:end]
    
    # Extract the specific content we need
    print("📋 Extracting IS-Architect collapsible sections content...")
    
    # Extract overwhelmed content
    overwhelmed_start = load_function.find("overwhelmedTitle.textContent = 'When")
    overwhelmed_end = load_function.find("';", overwhelmed_start) + 2
    overwhelmed_title = load_function[overwhelmed_start:overwhelmed_end]
    
    overwhelmed_content_start = load_function.find("overwhelmedContent.innerHTML = '", overwhelmed_end)
    overwhelmed_content_end = load_function.find("';", overwhelmed_content_start) + 2
    overwhelmed_content = load_function[overwhelmed_content_start:overwhelmed_content_end]
    
    # Extract stuck content
    stuck_start = load_function.find("stuckTitle.textContent = 'Getting")
    stuck_end = load_function.find("';", stuck_start) + 2
    stuck_title = load_function[stuck_start:stuck_end]
    
    stuck_content_start = load_function.find("stuckContent.innerHTML = 'When", stuck_end)
    stuck_content_end = load_function.find("';", stuck_content_start) + 2
    stuck_content = load_function[stuck_content_start:stuck_content_end]
    
    # Extract prompts content
    prompts_start = load_function.find("promptsTitle.textContent = 'Prompts")
    prompts_end = load_function.find("';", prompts_start) + 2
    prompts_title = load_function[prompts_start:prompts_end]
    
    prompts_content_start = load_function.find("promptsContent.innerHTML = 'How", prompts_end)
    prompts_content_end = load_function.find("';", prompts_content_start) + 2
    prompts_content = load_function[prompts_content_start:prompts_content_end]
    
    print("✅ Extracted collapsible sections content")
    
    # 2. Add IS-Architect logic to setCollapsibleSections
    setcollapsible_start = content.find('function setCollapsibleSections(code) {')
    insertion_point = content.find('// Handle specific profile codes first', setcollapsible_start)
    
    if insertion_point == -1:
        insertion_point = content.find('// Show collapsible sections for all profiles', setcollapsible_start)
    
    is_architect_logic = f'''
            if (code === 'IS-Architect') {{
                // Set overwhelmed content for IS-Architect
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {{
                    {overwhelmed_title.strip()}
                    {overwhelmed_content.strip()}
                }}
                
                // Set stuck/unstuck content for IS-Architect
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {{
                    {stuck_title.strip()}
                    {stuck_content.strip()}
                }}
                
                // Set prompts content for IS-Architect
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {{
                    {prompts_title.strip()}
                    {prompts_content.strip()}
                }}
                return; // Exit early, don't use generic logic
            }}
            
            '''
    
    # Insert at the beginning of the specific profile handling
    content = content[:insertion_point] + is_architect_logic + content[insertion_point:]
    
    print("✅ Added IS-Architect logic to setCollapsibleSections")
    
    # 3. Remove the loadISArchitectContent function call from activateProfile
    old_call = '''                    if (code === 'IS-Architect') {
                        loadISArchitectContent();
                    }'''
    
    content = content.replace(old_call, '')
    print("✅ Removed loadISArchitectContent call from activateProfile")
    
    # 4. Remove the loadISArchitectContent function entirely
    start = content.find('function loadISArchitectContent() {')
    if start != -1:
        end = content.find('function ', start + 1)
        if end == -1:
            # Last function in file
            end = content.rfind('}') + 1
        
        # Remove the function and surrounding whitespace
        content = content[:start-1] + content[end:]
        print("✅ Removed loadISArchitectContent function")
    
    # Write back
    with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'w') as f:
        f.write(content)
    
    print("✅ IS-Architect now uses consistent setCollapsibleSections pattern")
    print("📋 All 4 profiles now use the same implementation approach")

if __name__ == "__main__":
    move_is_architect_to_consistent_pattern()