# STTI Assessment Project - Standard Operating Procedures

**Version**: 1.1  
**Date**: 2025-09-11  
**Author**: Claude Code  
**Project Status**: 12/24 profiles complete (50%)  

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [The Four Sacred Tenets](#the-four-sacred-tenets)
3. [Architecture & Code Structure](#architecture--code-structure)
4. [Profile Implementation System](#profile-implementation-system)
5. [Tendency Logic Patterns](#tendency-logic-patterns)
6. [Working Process & Methodology](#working-process--methodology)
7. [Common Pitfalls & Landmines](#common-pitfalls--landmines)
8. [Technical Implementation Details](#technical-implementation-details)
9. [Testing & Validation](#testing--validation)
10. [Git Workflow & Deployment](#git-workflow--deployment)
11. [Completed Profiles Reference](#completed-profiles-reference)
12. [Future Work & Scaling](#future-work--scaling)

---

## Project Overview

### What is STTI Assessment?
The **Sensemaking Type and Tendencies Inventory (STTI)** is a personality assessment tool that determines a user's cognitive profile based on:
- **4 Archetypes**: Inner Guide (I), Synthesizer (S), Producer (P), Creative (C)
- **2 Tendencies**: Architect (structured) vs Gardener (flexible)
- **6 Orientations**: Westerner, Easterner, Northerner, Southerner, Diagonal (2 types)

### The 24 Profiles
Each profile is coded as `XX-Tendency`:
- `IS-Architect`, `IS-Gardener` (Westerner/Philosopher)
- `IP-Architect`, `IP-Gardener` (Diagonal Converter)
- `CP-Architect`, `CP-Gardener` (Easterner/Maker)
- `CS-Architect`, `CS-Gardener` (Diagonal Translator)
- `PS-Architect`, `PS-Gardener` (Northerner/Builder)
- `CI-Architect`, `CI-Gardener` (Southerner/Explorer)
- Plus all other 2-letter archetype combinations...

### Assessment Flow
1. User answers 48 questions
2. JavaScript calculates archetype scores (I, S, P, C) and tendency (A, G)
3. System determines dominant archetype pair and tendency
4. Profile-specific content loads (orientation, archetypes, tendency, collapsible sections)
5. User gets personalized results with actionable insights

### Secret Codes System
- Codes `0001-0024` allow direct preview of any profile
- Used for testing and development
- Activated by typing 4-digit codes when focused on page
- Critical for rapid testing during development

#### Complete Secret Code Mapping
| Code | Profile | Code | Profile | Code | Profile | Code | Profile |
|------|---------|------|---------|------|---------|------|---------|
| 0001 | IP-Architect | 0007 | PI-Architect | 0013 | SI-Architect | 0019 | CI-Architect |
| 0002 | IP-Gardener | 0008 | PI-Gardener | 0014 | SI-Gardener | 0020 | CI-Gardener |
| 0003 | IS-Architect | 0009 | PS-Architect | 0015 | SP-Architect | 0021 | CP-Architect |
| 0004 | IS-Gardener | 0010 | PS-Gardener | 0016 | SP-Gardener | 0022 | CP-Gardener |
| 0005 | IC-Architect | 0011 | PC-Architect | 0017 | SC-Architect | 0023 | CS-Architect |
| 0006 | IC-Gardener | 0012 | PC-Gardener | 0018 | SC-Gardener | 0024 | CS-Gardener |

**Quick Reference:**
- **PS-Architect = 0009** (Northerner/Builder)
- **PS-Gardener = 0010** (Northerner/Builder)
- **CI-Architect = 0019** (Southerner/Explorer)  
- **CI-Gardener = 0020** (Southerner/Explorer)

---

## The Four Sacred Tenets

**These tenets exist because I repeatedly made careless mistakes that broke working code. FOLLOW THEM RELIGIOUSLY.**

### Tenet #1: Do not carelessly modify code without properly understanding the existing structure
**Why this matters**: I repeatedly broke working functionality by making blind string replacements without understanding the surrounding context. The try/catch syntax error that broke secret codes was a direct result of violating this tenet.

**How to follow**:
- Always read the surrounding 20-30 lines of any code you're modifying
- Understand the function's purpose and how it fits into the larger system
- Check for dependencies and side effects before making changes

### Tenet #2: Before adding to the HTML file, use a reusable Python script to re-familiarize yourself with the entirety of the code
**Why this matters**: The HTML file is 3000+ lines. You cannot see the full structure using standard tools, leading to incomplete understanding and errors.

**How to follow**:
- Create Python scripts that analyze the full file structure
- Map out function locations, profile implementations, and patterns
- Identify existing code before adding new code
- Use scripts like `analyze_code_structure.py` as templates

### Tenet #3: Always validate JavaScript syntax after every modification - never commit without testing that the basic functionality still works
**Why this matters**: Syntax errors break the entire JavaScript execution, causing secret codes and core functionality to fail silently.

**How to follow**:
- Run `test_syntax_validation.py` after every change
- Check for balanced braces, parentheses, and try/catch blocks
- Test secret codes (0001, 0002, etc.) to ensure basic functionality works
- If syntax validation fails, fix immediately before proceeding

### Tenet #4: Make one surgical change at a time and verify it works before making the next change - never batch multiple modifications without testing each individually
**Why this matters**: When multiple changes are batched together, it becomes impossible to isolate which change caused a problem, leading to debugging hell.

**How to follow**:
- Make one logical change per commit
- Test the change immediately after implementation
- Only proceed to the next change after confirming the current one works
- Use git commits to create restore points

### Tenet #5: You have permission to download any Python library or script that will make your job more accurate, efficient, or faster. Note to my future self: Please also complete this tenet number five with additional descriptive details and its own "How to follow" subsection. 

---

## Architecture & Code Structure

### File Structure
```
/Users/nick/Dropbox/+/AI/stti-assessment/
├── index.html                 # Main application (3000+ lines)
├── STTI_PROJECT_SOP.md       # This documentation
├── Clean_STTI_*.png          # Profile chord diagrams
├── *.py                      # Python analysis/modification scripts
└── font files                # Canela Deck fonts
```

### HTML File Organization
The `index.html` file contains everything:
- **Lines 1-500**: HTML structure, CSS styles
- **Lines 500-1500**: Assessment questions and form structure  
- **Lines 1500-2000**: Core JavaScript functions
- **Lines 2000-3000**: Results display and sharing functionality

### Key JavaScript Functions (in order of definition)
1. `setTendencyPills(code)` - Sets tendency pills and descriptions
2. `setArchetypeDescription(code)` - Sets archetype combination descriptions
3. `setCollapsibleSections(code)` - **THE MAIN PROFILE CONTENT FUNCTION**
4. `activateProfile(code, name)` - Orchestrates all profile loading
5. `setStaticArchetypePills(code)` - Sets archetype pill order
6. `setOrientation(code)` - Sets orientation pills and descriptions
7. `showTestResults(targetProfile)` - Handles secret codes
8. `showSpecificProfile(profile)` - Legacy function (mostly unused)

### The Consistent Pattern: setCollapsibleSections
**This is the heart of profile-specific content.** All profiles should use this pattern:

```javascript
function setCollapsibleSections(code) {
    // Handle specific profile codes first
    if (code === 'SPECIFIC-PROFILE') {
        // Set overwhelmed content
        const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
        const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
        if (overwhelmedTitle && overwhelmedContent) {
            overwhelmedTitle.textContent = 'When [Orientation]s feel overwhelmed…';
            overwhelmedContent.innerHTML = '[Specific content]';
        }
        
        // Set stuck/unstuck content
        const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
        const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
        if (stuckTitle && stuckContent) {
            stuckTitle.textContent = 'Getting stuck and unstuck as a [PROFILE]';
            stuckContent.innerHTML = '[Tendency-specific logic]';
        }
        
        // Set prompts content
        const promptsTitle = document.querySelector('#promptsSection .section-title');
        const promptsContent = document.querySelector('#promptsSection .section-content');
        if (promptsTitle && promptsContent) {
            promptsTitle.textContent = 'Prompts for [PROFILE]';
            promptsContent.innerHTML = '[Pathway-specific prompts]';
        }
        return; // Exit early, don't use generic logic
    }
    
    // Generic logic for unimplemented profiles...
}
```

---

## Profile Implementation System

### Archetype Combinations & Orientations
| Combination | Orientation | Description |
|-------------|-------------|-------------|
| IS | Westerner | Philosopher (reflection-focused) |
| CP | Easterner | Maker (action-focused) |
| PS | Northerner | Builder (systematic progress) |
| CI | Southerner | Explorer (creative discovery) |
| CS | Diagonal | Translator (bridge perspectives) |
| IP | Diagonal | Converter (transform insights to action) |

### The Three Collapsible Sections

#### 1. When [Orientation]s feel overwhelmed…
**Purpose**: Describes the orientation's typical overwhelm pattern and solution
**Pattern**: Each orientation has consistent overwhelm behavior:
- **Westerners**: Double-down on analysis → need expression
- **Easterners**: Increase activity → need reflection  
- **Northerners**: Over-plan → need decisive action
- **Southerners**: Get lost in exploration → need structure
- **Translators**: Bridge too many perspectives → focus on one
- **Converters**: Oscillate between reflection/action → find rhythm

#### 2. Getting stuck and unstuck as a [PROFILE]
**Purpose**: Explains which archetype is most difficult to access and the pathway to reach it
**Critical Pattern**: This follows the **Tendency Logic** (see next section)

#### 3. Prompts for [PROFILE] / Prompts to go from [Direction] as [PROFILE]
**Purpose**: Provides specific questions/prompts to activate the pathway archetype
**Pattern**: Guides from accessible archetype → difficult archetype

---

## Tendency Logic Patterns

**THIS IS THE MOST CRITICAL AND ERROR-PRONE PART OF THE SYSTEM**

### The Core Pattern
- **Architect Tendency**: Struggles with flexible/intuitive archetypes (Creative, Inner Guide)
- **Gardener Tendency**: Struggles with structured/systematic archetypes (Producer, Synthesizer)

### Archetype Classifications
- **Structured Archetypes**: Producer (systematic action), Synthesizer (systematic analysis)
- **Flexible Archetypes**: Creative (innovative expression), Inner Guide (intuitive meaning)

### Tendency-Specific Difficulties
For any archetype combination `XY`:

**If Architect Tendency**:
- Difficult archetype = the flexible one not in XY
- Pathway archetype = the structured one in XY

**If Gardener Tendency**:
- Difficult archetype = the structured one not in XY  
- Pathway archetype = the flexible one in XY

### Example Applications
- **IS-Architect**: Has I+S, struggles with Creative (flexible), uses Synthesizer (structured) pathway
- **IS-Gardener**: Has I+S, struggles with Producer (structured), uses Inner Guide (flexible) pathway
- **CP-Architect**: Has C+P, struggles with Inner Guide (flexible), uses Producer (structured) pathway
- **CP-Gardener**: Has C+P, struggles with Synthesizer (structured), uses Creative (flexible) pathway

### Template for Stuck/Unstuck Content
```
When you combine your [Orientation] archetypes with an [Tendency] tendency, 
it's most difficult to access your [Difficult Archetype] archetype—yet that's 
exactly what you most need. Since your tendency is to [tendency verb], the 
easiest way to [movement description] is by tapping into your [Pathway Archetype] 
archetype, which aligns with your [tendency description] approach.
```

---

## Working Process & Methodology

### Before Starting Any Work
1. **Read this SOP completely**
2. **Run analysis Python script** to understand current state
3. **Plan the work** - which profiles, what order, what content
4. **Set up validation tools** ready for testing

### Profile Implementation Workflow
1. **Analyze current state** with Python script
2. **Plan specific profiles** (usually 2-4 at a time)
3. **Implement one profile** with surgical precision
4. **Validate syntax** immediately
5. **Test secret codes** to ensure functionality
6. **Commit changes** with descriptive message
7. **Repeat for next profile**

### Python Script Templates
Always create Python scripts for:
- **Analysis**: Understanding current code structure
- **Implementation**: Adding new profile content
- **Validation**: Checking syntax and completeness
- **Fixing**: Correcting errors systematically

### Communication with User
- **Be concise**: User prefers direct, short responses
- **Focus on actions**: What you're doing, not explaining why
- **Admit mistakes**: When you screw up, own it and fix it quickly
- **Ask for clarification**: Better to ask than assume incorrectly

---

## Common Pitfalls & Landmines

### 🚨 CRITICAL ERRORS TO AVOID

#### 1. Tendency Logic Backwards (Happened multiple times)
**The Error**: Incorrectly identifying which archetype is difficult for each tendency
**Example**: Saying CP-Architect struggles with Producer instead of Inner Guide
**Prevention**: Always double-check against working examples (IS-Architect, IS-Gardener)
**Fix Process**: Create analysis script, fix one profile at a time, validate each fix

#### 2. CSS Class Naming Errors
**The Error**: Using `garden-pill` instead of `gardener-pill`
**Root Cause**: Template literals that don't match existing CSS classes
**Prevention**: Always check existing CSS classes before implementing JavaScript assignments
**Fix Process**: Use exact class names, not programmatic variations

#### 3. Function Definition Order Errors
**The Error**: Calling functions before they're defined in JavaScript
**Example**: `setTendencyPills()` called on line 1656 but defined on line 1778
**Prevention**: Always define functions before calling them, or use function hoisting pattern
**Fix Process**: Move function definitions above their first usage

#### 4. Syntax Errors from Careless Editing
**The Error**: Missing closing braces, mismatched quotes, broken try/catch blocks
**Root Cause**: Making changes without understanding surrounding syntax
**Prevention**: Follow Tenet #1 - understand structure before modifying
**Fix Process**: Run syntax validation after every change

#### 5. Inconsistent Implementation Patterns
**The Error**: Using different patterns for different profiles (loadXXXContent vs setCollapsibleSections)
**Root Cause**: Not following established architectural patterns
**Prevention**: Always use the same pattern established for other profiles
**Fix Process**: Refactor inconsistent profiles to match the standard pattern

### 🔍 Debugging Techniques

#### When Secret Codes Don't Work
1. **Check browser console** for JavaScript errors
2. **Verify syntax validation** passes all checks
3. **Test with single profile first** (0001 for IS-Architect)
4. **Check function call chain**: showTestResults → activateProfile → profile functions

#### When Styling Doesn't Appear
1. **Verify CSS class names** match exactly
2. **Check JavaScript assignments** use correct class strings
3. **Confirm HTML structure** exists for the styling target
4. **Test with working profile** to compare

#### When Content Doesn't Update
1. **Verify profile code exists** in setCollapsibleSections
2. **Check early return logic** prevents generic content
3. **Confirm DOM selectors** target correct elements
4. **Test innerHTML assignments** with console.log

---

## Technical Implementation Details

### Profile Code Format
- **Format**: `AB-Tendency` where A and B are archetype letters
- **Examples**: `IS-Architect`, `CP-Gardener`, `PS-Architect`
- **Validation**: Must split on `-` to extract archetypes and tendency

### Secret Code System
- **Codes**: 0001-0024 map to specific profiles
- **Activation**: Keydown event listener builds sequence, triggers on 4-digit match
- **Function Flow**: keydown → showTestResults → activateProfile → profile functions
- **Testing**: Use 0001 (IS-Architect) as baseline test

### Dynamic Content Loading
The profile loading system calls these functions in order:
1. `setStaticArchetypePills(code)` - Archetype pill positioning
2. `setOrientation(code)` - Orientation pill and description
3. `setTendencyPills(code)` - Tendency pills and description
4. `setArchetypeDescription(code)` - Archetype combination description
5. `setCollapsibleSections(code)` - Profile-specific collapsible content

### CSS Class Patterns
- **Archetype Pills**: `archetype-pill`, `inner-guide-pill`, `synthesizer-pill`, etc.
- **Tendency Pills**: `tendency-pill`, `architect-pill`, `gardener-pill`
- **Orientation Pills**: Uses text content, no specific classes
- **Responsive**: Designed for mobile-first approach

### HTML Structure Dependencies
```html
<!-- Archetype Pills -->
<div id="primaryArchetypePill">Inner Guide</div>
<div id="secondaryArchetypePill">Synthesizer</div>

<!-- Tendency Pills -->
<div id="tendencyPill">Architect</div>
<div id="secondaryTendencyPill">Gardener</div>

<!-- Orientation -->
<div id="orientationPill">Westerner</div>

<!-- Collapsible Sections -->
<div id="overwhelmedSection">
    <div class="section-title">Title</div>
    <div class="section-content">Content</div>
</div>
```

---

## Testing & Validation

### Syntax Validation Script Template
```python
def test_syntax_validation():
    with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
        content = f.read()
    
    # Check brace balance
    open_braces = content.count('{')
    close_braces = content.count('}')
    
    # Check parentheses balance  
    open_parens = content.count('(')
    close_parens = content.count(')')
    
    # Check try/catch balance
    try_count = content.count('try {')
    catch_count = content.count('} catch (')
    
    # Report results
    print(f"Braces: {open_braces - close_braces} (should be 0)")
    print(f"Parens: {open_parens - close_parens} (should be 0)")
    print(f"Try/Catch: {try_count - catch_count} (should be 0)")
```

### Manual Testing Checklist
- [ ] Secret code 0001 loads IS-Architect correctly
- [ ] All 3 collapsible sections have content
- [ ] Tendency pills show correct colors
- [ ] Orientation pill shows correct text
- [ ] Archetype pills show correct order
- [ ] No JavaScript console errors

### Browser Console Monitoring
- Watch for syntax errors (red text)
- Check for failed resource loads (favicon, fonts)
- Monitor for Permissions-Policy warnings (cosmetic)
- Verify function calls execute successfully

---

## Git Workflow & Deployment

### Commit Message Pattern
```
[Action]: [Specific change] 

[Detailed description of what was changed and why]
[Any context needed for future reference]

🤖 Generated with [Claude Code](https://claude.ai/code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

### Deployment Flow
1. **Local changes** in `/Users/nick/Dropbox/+/AI/stti-assessment/index.html`
2. **Git commit** with descriptive message
3. **Git push** to GitHub repository
4. **GitHub Pages** automatically deploys to live site
5. **Test live site** to confirm changes work in production

### Repository Structure
- **Main branch**: Production code, auto-deploys to GitHub Pages
- **Direct commits**: No PR process, commits go straight to main
- **Live URL**: https://nickmilo.github.io/stti-assessment/

### When Things Break in Production
1. **Check browser console** on live site for errors
2. **Test secret codes** to isolate functionality issues
3. **Compare local vs live** to identify deployment issues
4. **Fix locally** and redeploy immediately

---

## Completed Profiles Reference

### Profile Implementation Status (12/24 Complete - 50%)

#### ✅ IS Profiles (Westerner/Philosopher)
- **IS-Architect** (0003): Creative difficult → Synthesizer pathway
- **IS-Gardener** (0004): Producer difficult → Creative pathway

#### ✅ IP Profiles (Diagonal Converter)  
- **IP-Architect** (0001): Creative difficult → Synthesizer pathway
- **IP-Gardener** (0002): Synthesizer difficult → Creative pathway

#### ✅ CP Profiles (Easterner/Maker)
- **CP-Architect** (0021): Inner Guide difficult → Creative pathway  
- **CP-Gardener** (0022): Synthesizer difficult → Producer pathway

#### ✅ CS Profiles (Diagonal Translator)
- **CS-Architect** (0023): Creative difficult → Producer pathway
- **CS-Gardener** (0024): Producer difficult → Creative pathway

#### ✅ PS Profiles (Northerner/Builder)
- **PS-Architect** (0009): Creative difficult → Inner Guide pathway
- **PS-Gardener** (0010): Inner Guide difficult → Creative pathway

#### ✅ CI Profiles (Southerner/Explorer)
- **CI-Architect** (0019): Synthesizer difficult → Producer pathway
- **CI-Gardener** (0020): Producer difficult → Synthesizer pathway

### Content Templates (Copy these patterns)

#### Overwhelmed Section Template
```
When [Orientation]s feel overwhelmed…
[Orientation-specific behavior] when what they [actually need].
```

#### Stuck/Unstuck Section Template  
```
Getting stuck and unstuck as a [PROFILE]
When you combine your [Orientation] archetypes with a [Tendency] tendency, 
it's most difficult to access your [Difficult Archetype] archetype—yet that's 
exactly what you most need. Since your tendency is to [tendency verb], the 
easiest way to [direction] is by tapping into your [Pathway Archetype] archetype, 
which aligns with your [tendency approach].
```

#### Prompts Section Template
```
Prompts to [action description] as a [PROFILE]
[Specific questions/prompts that activate the pathway archetype]? 
Once your [Pathway Archetype] is activated, you'll likely find it becomes 
easier to move into your [Difficult Archetype] archetype, allowing you to 
[desired outcome].
```

---

## Future Work & Scaling

### Remaining Profiles (16/24)
Next logical batch priorities:
1. **PS Profiles** (Northerner/Builder): PS-Architect, PS-Gardener
2. **CI Profiles** (Southerner/Explorer): CI-Architect, CI-Gardener  
3. **Reverse combinations**: IC, PC, SC, SP, SI, PI (12 profiles)

### Archetype Combination Mappings Needed
| Combo | Orientation | Archetype 1 | Archetype 2 |
|-------|-------------|-------------|-------------|
| PS | Northerner | Producer | Synthesizer |
| CI | Southerner | Creative | Inner Guide |
| IC | Southerner | Inner Guide | Creative |
| PC | Easterner | Producer | Creative |
| SC | Diagonal | Synthesizer | Creative |
| SP | Northerner | Synthesizer | Producer |
| SI | Westerner | Synthesizer | Inner Guide |
| PI | Diagonal | Producer | Inner Guide |

### Scaling Considerations
- **File size**: May need to split JavaScript into modules at some point
- **Performance**: 24 profiles shouldn't impact load time significantly  
- **Maintainability**: Current pattern scales well for remaining profiles
- **Testing**: Consider automated testing for secret codes

### Content Authoring Process
For each new profile batch:
1. **Map orientations** for archetype combinations
2. **Determine tendency difficulties** using established pattern
3. **Write overwhelmed content** based on orientation  
4. **Write stuck/unstuck content** based on tendency logic
5. **Write prompts content** based on pathway activation
6. **Implement systematically** following the four tenets

### Long-term Vision
- All 24 profiles implemented with consistent, high-quality content
- Robust testing system that prevents regressions  
- Clean, maintainable codebase that can be extended
- Comprehensive documentation for future maintainers

---

## Emergency Procedures

### If You Break Everything
1. **Don't panic** - Git history can restore working state
2. **Check git log** to identify last working commit
3. **Revert to working state**: `git reset --hard [commit-hash]`
4. **Restart from known good state**
5. **Follow tenets more carefully** the second time

### If Secret Codes Stop Working
1. **Check browser console** for JavaScript errors first
2. **Run syntax validation** to identify structural issues
3. **Test with single profile** (0001) to isolate problem
4. **Check function call chain** from keydown to profile display
5. **Verify no duplicate event listeners** are interfering

### If User Gets Frustrated
1. **Acknowledge the mistake** clearly and directly
2. **Focus on fixing** rather than explaining
3. **Follow tenets religiously** to prevent repeat errors
4. **Communicate progress** concisely
5. **Test thoroughly** before claiming something is fixed

### Communication Crisis Protocol
- **Be direct**: No preamble, no explanation unless asked
- **Own mistakes**: "I got the tendency logic backwards" not "there seems to be an issue"
- **Focus on action**: What you're doing to fix it
- **Keep responses short**: User prefers concise communication

---

## Final Reminders for Future Self

### The Most Important Things to Remember
1. **THE FOUR TENETS ARE NOT SUGGESTIONS** - They prevent hours of debugging hell
2. **Tendency logic is tricky** - Always verify against working examples  
3. **Test immediately after every change** - Don't batch changes without testing
4. **The user values directness** - No fluff, just results
5. **When in doubt, use Python scripts** - They reveal the full picture

### Before You Start Working
- [ ] Read this SOP completely
- [ ] Understand the four tenets deeply  
- [ ] Create analysis scripts first
- [ ] Plan your approach systematically
- [ ] Set up validation tools

### Success Metrics
- ✅ Secret codes work for all implemented profiles
- ✅ No JavaScript console errors
- ✅ Consistent content quality across profiles
- ✅ Clean, maintainable code structure
- ✅ Happy user feedback

### Remember: Excellence is Built on Process
This project's success depends not on cleverness, but on disciplined adherence to proven processes. The four tenets exist because they prevent the specific mistakes that have derailed progress multiple times. Follow them religiously, and you'll deliver consistent, high-quality results.

**Good luck, future self. You've got this.**

---

*Last updated: 2025-09-11*  
*Next update: After completing PS and CI profiles*