# Implementation Guide: Secret Codes 0025 & 0026
## Quick Reference for Adding Radar Chart Test Profiles

**File:** `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/main.js`
**Changes Required:** 2 modifications in 1 file
**Time Estimate:** 15 minutes
**Risk Level:** Low (isolated changes, backward compatible)

---

## TLDR

Add two test codes to validate radar chart rendering:
- **0025**: Extreme variance (I=32 vs S=8) → IP-Architect profile
- **0026**: Balanced scores (P=33 to S=18) → PI-Architect profile

Both profiles already exist. We just need to pass custom scores through the activation flow.

---

## Change #1: Enhance activateProfile() Function

**Location:** main.js, line 328

### Step 1: Update Function Signature

**Find this line (328):**
```javascript
function activateProfile(code, name) {
```

**Replace with:**
```javascript
function activateProfile(code, name, customScores = null) {
```

### Step 2: Add Score Rendering Logic

**Find this section (lines 367-372):**
```javascript
                    // Hide sections for broken profiles
                    hideBrokenProfileSections(code);

                    // Load full content based on profile

                    console.log(`${code} activated successfully`);
```

**Replace with:**
```javascript
                    // Hide sections for broken profiles
                    hideBrokenProfileSections(code);

                    // Render score visualizations if custom scores provided (for test codes)
                    if (customScores) {
                        // Calculate archetype scores for accurate pill ordering
                        const archetypeScores = [
                            ['I', customScores.I],
                            ['S', customScores.S],
                            ['P', customScores.P],
                            ['C', customScores.C]
                        ].sort((a, b) => {
                            if (b[1] !== a[1]) return b[1] - a[1]; // Sort by score descending
                            return a[0].localeCompare(b[0]); // Alphabetical tiebreaker
                        });

                        // Re-render archetype pills with actual score ordering
                        setStaticArchetypePills(code, archetypeScores);

                        // Render radar charts and score bars
                        renderRadarChart(customScores, code);
                        renderRadarChartArchetypesOnly(customScores);
                        animateScoreBars(customScores);
                    }

                    // Load full content based on profile

                    console.log(`${code} activated successfully`);
```

**Why this works:**
- `customScores = null` default ensures backward compatibility
- Existing codes (0001-0024) pass no third parameter, so customScores stays null
- New codes (0025-0026) pass scores object, triggering visualization
- Pills are re-rendered with actual score order instead of code order

---

## Change #2: Add Secret Code Handlers

**Location:** main.js, line 244 (after code 0024 handler)

### Find this section (lines 241-247):
```javascript
                } else if (keySequence === '0024') {
                    activateProfile('CS-Gardener', 'The Translator');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence.length >= 4) {
                    keySequence = '';
                    clearTimeout(keyTimer);
                }
```

### Replace with:
```javascript
                } else if (keySequence === '0024') {
                    activateProfile('CS-Gardener', 'The Translator');
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0025') {
                    // TEST CODE: Extreme variance (I=32 vs S=8) - 24 point spread
                    const testScores = { I: 32, S: 8, P: 26, C: 15, A: 32, G: 10 };
                    activateProfile('IP-Architect', 'The Converter', testScores);
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0026') {
                    // TEST CODE: Balanced scores (P=33 to S=18) - 15 point spread
                    const testScores = { I: 24, S: 18, P: 33, C: 20, A: 20, G: 18 };
                    activateProfile('PI-Architect', 'The Converter', testScores);
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence.length >= 4) {
                    keySequence = '';
                    clearTimeout(keyTimer);
                }
```

**Why this works:**
- Follows exact pattern of existing codes
- Defines scores inline for clarity
- Calls enhanced activateProfile() with third parameter
- Comments explain test purpose

---

## Verification Steps

### Syntax Check
1. Save main.js
2. Load index.html in browser
3. Open DevTools console (F12)
4. Check for JavaScript errors
5. ✓ Should see "Profile configuration loaded" message

### Functional Test: Code 0025
1. Press keys: 0, 0, 2, 5 (not in input field)
2. ✓ Results screen appears
3. ✓ Shows "IP-Architect - The Converter"
4. ✓ Archetype pills show: Inner Guide, Producer, Creative, Synthesizer
5. ✓ Tendency pill shows: Architect
6. ✓ Radar chart renders with extreme polygon shape
7. ✓ Score bars show: I: 32, S: 8, P: 26, C: 15, A: 32, G: 10
8. ✓ Raw scores text displays correctly

### Functional Test: Code 0026
1. Refresh page
2. Press keys: 0, 0, 2, 6
3. ✓ Results screen appears
4. ✓ Shows "PI-Architect - The Converter"
5. ✓ Archetype pills show: Producer, Inner Guide, Creative, Synthesizer (P first!)
6. ✓ Tendency pill shows: Architect
7. ✓ Radar chart renders with balanced polygon shape
8. ✓ Score bars show: I: 24, S: 18, P: 33, C: 20, A: 20, G: 18

### Regression Test
1. Test code 0001 → ✓ IP-Architect without score visualization
2. Test code 0009 → ✓ PS-Architect without score visualization
3. Complete full assessment → ✓ Scores render normally
4. Test invalid code 0099 → ✓ Nothing happens (as expected)

---

## Expected Results

### Code 0025 Visual Characteristics
- **Radar Chart Shape:** Extremely narrow at Synthesizer (8), very wide at Inner Guide (32)
- **Polygon:** High variance, irregular hexagon
- **Score Bars:** I and A bars near 100%, S bar near 0%
- **Pill Order:** Inner Guide (32) > Producer (26) > Creative (15) > Synthesizer (8)

### Code 0026 Visual Characteristics
- **Radar Chart Shape:** More balanced, closer to regular hexagon
- **Polygon:** Lower variance, smoother shape
- **Score Bars:** All bars in middle range (18-33)
- **Pill Order:** Producer (33) > Inner Guide (24) > Creative (20) > Synthesizer (18)

---

## Troubleshooting

### Issue: Syntax error after editing
**Solution:** Check for missing braces, commas, or parentheses. Use code editor with syntax highlighting.

### Issue: Code 0025 or 0026 doesn't activate
**Solution:**
- Verify you're NOT in an input field (click on page background first)
- Check console for errors
- Try refreshing page and testing again

### Issue: Radar charts don't render
**Solution:**
- Check console for errors in renderRadarChart()
- Verify SVG elements exist in HTML (#radarChart, #radarChartArchetypes)
- Confirm customScores object has all 6 properties (I, S, P, C, A, G)

### Issue: Pills show wrong order
**Solution:**
- Verify archetypeScores calculation in activateProfile()
- Check that setStaticArchetypePills() is called AFTER archetypeScores calculated
- Confirm sort logic matches: higher scores first, alphabetical tiebreaker

### Issue: Existing codes (0001-0024) break
**Solution:**
- Verify function signature has `customScores = null` default
- Check that `if (customScores)` block only runs when scores provided
- Test a few existing codes to confirm they still work

---

## Code Explanation

### Why Re-render Archetype Pills?

**Problem:** setStaticArchetypePills(code) renders pills in CODE order:
```javascript
// Code: IP-Architect
// Pills: I, P, C, S (alphabetical for remaining)
// But actual scores: I=32, P=26, C=15, S=8 (already in correct order by chance)

// Code: PI-Architect
// Pills: P, I, C, S (alphabetical for remaining)
// But actual scores: P=33, I=24, C=20, S=18 (matches!)
```

**Solution:** Calculate archetypeScores from actual scores, then re-render:
```javascript
// Actual scores determine order
archetypeScores = [['P',33], ['I',24], ['C',20], ['S',18]]
setStaticArchetypePills(code, archetypeScores)
// Pills now show: P (highest) → I → C → S (lowest)
```

### Why Use Default Parameter?

**Backward Compatibility:**
```javascript
// Existing calls (codes 0001-0024):
activateProfile('PS-Architect', 'The Builder')
// customScores = null (default), score rendering skipped

// New calls (codes 0025-0026):
activateProfile('IP-Architect', 'The Converter', { I:32, S:8, ... })
// customScores = {...}, score rendering executes
```

**Alternative approaches rejected:**
- Create new function (duplicates code)
- Use global variable (messy state management)
- Check profile code (couples test codes to implementation)

---

## What NOT to Change

**DO NOT modify these functions:**
- calculateScores() - used by production assessment
- determineProfile() - used by production assessment
- showResults() - different code path from activateProfile()
- renderRadarChart() - works correctly as-is
- ProfileRenderer.renderProfile() - handles profile content

**DO NOT modify these files:**
- profiles.json - profiles already exist
- profile-renderer.js - no changes needed
- index.html - DOM structure is correct
- styles.css - styling is correct

**DO NOT add:**
- New profile entries for 0025/0026 (use existing profiles)
- Test mode flags or indicators (keep implementation minimal)
- Logging beyond what exists (console.log already present)

---

## Future Enhancements (Out of Scope)

### Additional Test Codes
- **0027**: All equal (I=20, S=20, P=20, C=20, A=20, G=20) - test perfect balance
- **0028**: All minimum (I=8, S=8, P=8, C=8, A=8, G=8) - test edge case
- **0029**: All maximum (I=32, S=32, P=32, C=32, A=32, G=32) - test edge case
- **0030**: Gardener extreme (reverse of 0025 with G=32, A=10)

### System Improvements
- Add "TEST MODE" badge when test code activated
- Log test scores to console automatically
- Add URL parameter support (e.g., ?test=0025)
- Create admin panel for custom score input
- Add keyboard shortcut to cycle through all test codes

---

## Git Commit Message Template

```
Add secret test codes 0025 and 0026 for radar chart testing

- Enhanced activateProfile() to accept optional customScores parameter
- Added test code 0025: Extreme variance (I=32 vs S=8) → IP-Architect
- Added test code 0026: Balanced scores (P=33 to S=18) → PI-Architect
- Test codes render radar charts and score bars with custom data
- Backward compatible: Existing codes 0001-0024 unchanged

Purpose: Validate radar chart rendering with edge cases
Testing: Both codes activate successfully with correct visualizations
```

---

## Summary

This implementation:
- ✓ Adds powerful testing capability with minimal code
- ✓ Maintains backward compatibility with existing codes
- ✓ Reuses existing profile infrastructure
- ✓ Provides clear visual validation of chart rendering
- ✓ Follows existing code patterns and conventions
- ✓ Low risk, high value addition

**Total Changes:**
- 1 function signature update
- 1 conditional block (15 lines)
- 2 secret code handlers (12 lines)
- **Total: ~30 lines of code**

**Testing Time:** 5-10 minutes
**Implementation Time:** 10-15 minutes
**Total Time:** 15-25 minutes

Ready to implement!
