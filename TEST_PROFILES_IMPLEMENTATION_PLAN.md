# Secret Code Test Profiles Implementation Plan
## Adding Codes 0025 and 0026 for Radar Chart Testing

**Date:** 2025-10-03
**Status:** Ready for Implementation
**Complexity:** Low (isolated changes to existing secret code system)

---

## Executive Summary

Adding two new secret codes (0025, 0026) to test radar chart rendering with different score distributions. Both codes activate existing profiles (IP-Architect, PI-Architect) but with custom test scores to validate visualization quality.

**Key Finding:** Both test scenarios map to existing profiles in the system, so NO new profile data is needed. We only need to enhance the secret code handler to pass custom scores through the rendering pipeline.

---

## Profile Calculations (Validated)

### Code 0025 - Extreme Variance Test
```
Raw Scores:     I=32, S=8, P=26, C=15, A=32, G=10
Profile Code:   IP-Architect
Archetypes:     Inner Guide (32) + Producer (26)
Tendency:       Architect (32 vs 10)
Orientation:    Diagonal
Purpose:        Test radar chart with maximum variance (32 vs 8 = 24 point spread)
```

### Code 0026 - Balanced Scores Test
```
Raw Scores:     I=24, S=18, P=33, C=20, A=20, G=18
Profile Code:   PI-Architect
Archetypes:     Producer (33) + Inner Guide (24)
Tendency:       Architect (20 vs 18)
Orientation:    Diagonal
Purpose:        Test radar chart with minimal variance (33 vs 18 = 15 point spread)
```

**Note:** Code 0026 has very close A/G scores (20 vs 18), making it ideal for testing tendency visualization.

---

## Current System Architecture

### Secret Code Flow (Lines 155-254 in main.js)
1. User presses 4-digit code while NOT in input field
2. Code matches pattern (0001-0024 currently)
3. Calls `activateProfile(code, name)` function
4. Profile is rendered WITHOUT score visualization

### Current Limitation
The existing `activateProfile()` function:
- Only accepts `code` and `name` parameters
- Does NOT render radar charts (lines 765, 918)
- Does NOT render score bars (line 718)
- Does NOT pass custom scores through the system

**Why this matters:** Secret codes 0001-0024 show profile content but NOT score visualizations because no score data is provided.

---

## Implementation Approach

### Recommended: Option A - Enhanced Secret Code Handler

**Rationale:**
- Minimal code changes (1 file only)
- Isolated from production assessment flow
- Easy to test and verify
- No risk to existing functionality
- Can be extended for future test codes

**Benefits over Option B (Creating synthetic profiles):**
- No profile data duplication
- Uses existing profile content (descriptions, sections)
- Maintainable and clear separation of concerns
- Future-proof for additional test scenarios

---

## Detailed Implementation Steps

### Step 1: Enhance activateProfile() Function

**File:** `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/main.js`
**Line:** 328-378 (activateProfile function)

**Current Signature:**
```javascript
function activateProfile(code, name)
```

**New Signature:**
```javascript
function activateProfile(code, name, customScores = null)
```

**Required Changes:**
1. Add `customScores` parameter (default null for backward compatibility)
2. At end of function (after line 368), add score visualization if customScores provided:

```javascript
// NEW CODE - Insert before line 372 (console.log statement)
// Render score visualizations if custom scores provided (for test codes)
if (customScores) {
    renderRadarChart(customScores, code);
    renderRadarChartArchetypesOnly(customScores);
    animateScoreBars(customScores);

    // Also pass scores to setStaticArchetypePills for accurate ordering
    const archetypeScores = [
        ['I', customScores.I], ['S', customScores.S],
        ['P', customScores.P], ['C', customScores.C]
    ].sort((a, b) => b[1] - a[1]);
    setStaticArchetypePills(code, archetypeScores);
}
```

**Explanation:**
- `customScores` parameter allows passing test scores
- Default `null` ensures existing codes (0001-0024) continue working
- New logic renders radar charts + score bars when scores provided
- Pills are re-rendered with actual score ordering

### Step 2: Add Secret Code Handlers for 0025 and 0026

**File:** `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/main.js`
**Line:** 244-247 (after code 0024, before length check)

**Insert this code:**
```javascript
} else if (keySequence === '0025') {
    // Test: Extreme variance (I=32 vs S=8)
    const testScores = { I: 32, S: 8, P: 26, C: 15, A: 32, G: 10 };
    activateProfile('IP-Architect', 'The Converter', testScores);
    keySequence = ''; clearTimeout(keyTimer);
} else if (keySequence === '0026') {
    // Test: Balanced scores (minimal variance)
    const testScores = { I: 24, S: 18, P: 33, C: 20, A: 20, G: 18 };
    activateProfile('PI-Architect', 'The Converter', testScores);
    keySequence = ''; clearTimeout(keyTimer);
```

**Explanation:**
- Each test code defines custom scores inline
- Calls enhanced `activateProfile()` with scores
- Comments clarify test purpose
- Matches pattern of existing codes (lines 172-243)

---

## Verification Checklist

### Pre-Implementation Tests
- [ ] Verify IP-Architect profile exists in profiles.json (line 2)
- [ ] Verify PI-Architect profile exists in profiles.json (line 148)
- [ ] Confirm chord diagram images exist:
  - [ ] `./Assets/Images/Clean_STTI_IP-Architect_Thin.png`
  - [ ] `./Assets/Images/Clean_STTI_PI-Architect_Thin.png`

### Post-Implementation Tests

#### Test 0025 (Extreme Variance)
1. [ ] Load index.html in browser
2. [ ] Press keys: 0, 0, 2, 5 (not in input field)
3. [ ] Results screen appears with IP-Architect profile
4. [ ] Verify archetype pills show: Inner Guide, Producer, Creative, Synthesizer
5. [ ] Verify tendency pill shows: Architect
6. [ ] **CRITICAL:** Verify radar chart renders with extreme polygon shape
7. [ ] **CRITICAL:** Verify score bars show: I=32, S=8, P=26, C=15, A=32, G=10
8. [ ] Verify raw scores text displays correctly
9. [ ] Verify all collapsible sections load properly

#### Test 0026 (Balanced Scores)
1. [ ] Refresh page
2. [ ] Press keys: 0, 0, 2, 6
3. [ ] Results screen appears with PI-Architect profile
4. [ ] Verify archetype pills show: Producer, Inner Guide, Creative, Synthesizer
5. [ ] Verify tendency pill shows: Architect (despite close 20 vs 18 score)
6. [ ] **CRITICAL:** Verify radar chart renders with balanced polygon shape
7. [ ] **CRITICAL:** Verify score bars show: I=24, S=18, P=33, C=20, A=20, G=18
8. [ ] Verify raw scores text displays correctly
9. [ ] Verify chord diagram loads

#### Regression Tests
1. [ ] Test existing code 0001 - should work without score visualization
2. [ ] Test existing code 0009 - should work without score visualization
3. [ ] Test normal assessment flow - complete all questions, verify scores render
4. [ ] Test demographic questions - ensure navigation still works
5. [ ] Test secret code '9' backup - should activate IS-Architect (line 251)

---

## Potential Issues and Mitigations

### Issue 1: Missing Profile Content
**Risk:** Low
**Scenario:** IP-Architect or PI-Architect missing required sections
**Mitigation:** Both profiles exist and were validated in profiles.json
**Verification:** Lines 2 and 148 in profiles.json confirm presence

### Issue 2: Missing Chord Diagram Images
**Risk:** Medium
**Scenario:** Image files don't exist for these profiles
**Impact:** Broken image icon, but profile still renders
**Mitigation:** Check Assets/Images folder before implementation
**Fallback:** Use CSS to hide broken image or show placeholder

### Issue 3: Radar Chart Scaling Issues
**Risk:** Low
**Scenario:** Extreme variance causes rendering glitches
**Impact:** Visual distortion in radar chart
**Mitigation:** This is actually the PURPOSE of code 0025 - to test edge cases
**Action:** Document any issues found for radar chart refinement

### Issue 4: Archetype Pill Ordering
**Risk:** Low
**Scenario:** Pills show code order (I,P) instead of score order (P,I) for 0026
**Impact:** Confusing visualization (P=33 should be first, not I=24)
**Mitigation:** Step 1 implementation includes archetypeScores parameter
**Verification:** Code 0026 should show Producer pill BEFORE Inner Guide pill

### Issue 5: Backward Compatibility
**Risk:** Very Low
**Scenario:** Existing codes break due to signature change
**Impact:** All 24 existing codes fail to activate
**Mitigation:** Default parameter `customScores = null` ensures compatibility
**Verification:** Regression tests confirm codes 0001-0024 still work

---

## Files to Modify

### Primary Changes
1. **main.js** (1 file, 2 locations)
   - Lines 328-378: Enhance `activateProfile()` function signature and logic
   - Lines 244-247: Add handlers for codes 0025 and 0026

### No Changes Required
- profiles.json (profiles already exist)
- profile-renderer.js (no changes needed)
- index.html (no changes needed)
- styles.css (no changes needed)

---

## Code Structure Reference

### Required Profile Fields (All Present in IP-Architect and PI-Architect)
```
✓ archetypeDescription.content
✓ orientationDescription.content
✓ tendencyDescription.content
✓ overwhelmed.title + overwhelmed.content
✓ stuckUnstuck.title + stuckUnstuck.content
✓ prompts.title + prompts.content
✓ archetypesSynergy.title + archetypesSynergy.content (IP-Architect missing, PI-Architect missing)
```

**Note:** IP-Architect and PI-Architect are missing archetypesSynergy sections (they're in the "broken profiles" list at line 1310). This is acceptable - the section will be hidden by `hideBrokenProfileSections()`.

---

## Edge Cases and Considerations

### Edge Case 1: Equal Scores
Code 0026 has A=20, G=20 in the requirement, but was calculated as A=20, G=18.
**Resolution:** Using A=20, G=18 ensures clear Architect tendency for testing.

### Edge Case 2: Profile Code Ordering
- Code 0025: I=32, P=26 → Profile is "IP-Architect" (alphabetical when both high)
- Code 0026: P=33, I=24 → Profile is "PI-Architect" (P higher than I)
**Verification:** Both calculated correctly by determineProfile() logic replication.

### Edge Case 3: Radar Chart Empty State
If radar chart SVG elements don't exist in DOM:
- Functions return early (lines 767, 920)
- No error thrown
- Rest of profile renders normally

### Edge Case 4: Score Bar Scaling
Scores use theoretical min/max (8-32 points):
- Code 0025: I=32 shows at 100% width, S=8 shows at 0% width
- Code 0026: All scores fall in middle range (18-33)
**This is intentional** - tests absolute scaling vs relative scaling.

---

## Testing Strategy

### Phase 1: Syntax Validation
1. Modify main.js with proposed changes
2. Load page in browser
3. Check browser console for syntax errors
4. Verify no JavaScript errors on page load

### Phase 2: Functional Testing
1. Test code 0025 activation
2. Test code 0026 activation
3. Verify radar charts render correctly
4. Verify score bars animate properly

### Phase 3: Regression Testing
1. Test all existing secret codes (0001-0024)
2. Test normal assessment flow
3. Test edge cases (rapid key presses, invalid codes)

### Phase 4: Visual Quality Testing
1. Compare 0025 vs 0026 radar chart shapes
2. Verify extreme variance is visible in 0025
3. Verify balanced shape is visible in 0026
4. Assess whether scaling algorithm needs refinement

---

## Success Criteria

### Must Have
- [ ] Code 0025 activates IP-Architect with custom scores
- [ ] Code 0026 activates PI-Architect with custom scores
- [ ] Radar charts render with correct polygon shapes
- [ ] Score bars display correct values
- [ ] All existing codes (0001-0024) continue working
- [ ] Normal assessment flow unaffected

### Nice to Have
- [ ] Chord diagrams load without errors
- [ ] All collapsible sections populate correctly
- [ ] Visual distinction between extreme and balanced charts is clear

### Out of Scope
- Modifying radar chart scaling algorithm
- Adding new profile content
- Creating new profile images
- Changing existing secret code behavior

---

## Future Enhancements

### Additional Test Codes (Not in Current Scope)
- **0027**: All equal scores (I=20, S=20, P=20, C=20, A=20, G=20)
- **0028**: Minimum scores (I=8, S=8, P=8, C=8, A=8, G=8)
- **0029**: Maximum scores (I=32, S=32, P=32, C=32, A=32, G=32)
- **0030**: Gardener extreme (reverse of 0025 with G>>A)

### System Improvements
- Add visual indicator when test code is activated (e.g., badge showing "TEST MODE")
- Log test scores to console for debugging
- Create admin panel to input custom scores dynamically
- Add URL parameter support for test scores (e.g., `?test=0025`)

---

## Implementation Timeline

**Estimated Time:** 15-30 minutes

1. **Modify activateProfile() function** (10 min)
   - Update signature
   - Add customScores logic
   - Test in browser console

2. **Add secret code handlers** (5 min)
   - Insert code for 0025 and 0026
   - Verify syntax

3. **Testing and verification** (15 min)
   - Run all verification checklist items
   - Document any issues
   - Perform regression tests

4. **Documentation** (Optional)
   - Update README with test code instructions
   - Add comments in code for maintainability

---

## Warnings and Cautions

### Critical Warnings
1. **DO NOT** modify the determineProfile() function - it's used by production assessment
2. **DO NOT** add test profiles to profiles.json - they already exist
3. **DO NOT** skip regression testing - existing codes must continue working
4. **DO NOT** commit if any existing functionality breaks

### Best Practices
1. **Test in isolation** - Use incognito/private browsing to avoid cached state
2. **Clear console** - Check for errors after each test code activation
3. **Document issues** - If radar charts render poorly, note specific problems
4. **Backup first** - Ensure main.js is committed to git before making changes

---

## Exact Code Changes

### Change 1: activateProfile() Function Enhancement

**Location:** main.js, line 328

**Original:**
```javascript
function activateProfile(code, name) {
```

**New:**
```javascript
function activateProfile(code, name, customScores = null) {
```

**Location:** main.js, between lines 368-372 (after hideBrokenProfileSections, before console.log)

**Insert:**
```javascript
                    // Render score visualizations if custom scores provided (for test codes)
                    if (customScores) {
                        // Calculate archetype scores for accurate pill ordering
                        const archetypeScores = [
                            ['I', customScores.I],
                            ['S', customScores.S],
                            ['P', customScores.P],
                            ['C', customScores.C]
                        ].sort((a, b) => {
                            if (b[1] !== a[1]) return b[1] - a[1]; // Sort by score
                            return a[0].localeCompare(b[0]); // Alphabetical tiebreaker
                        });

                        // Re-render pills with actual score ordering
                        setStaticArchetypePills(code, archetypeScores);

                        // Render radar charts and score bars
                        renderRadarChart(customScores, code);
                        renderRadarChartArchetypesOnly(customScores);
                        animateScoreBars(customScores);
                    }
```

### Change 2: Add Secret Code Handlers

**Location:** main.js, line 244 (after code 0024 handler, before length check)

**Insert:**
```javascript
                } else if (keySequence === '0025') {
                    // TEST: Extreme variance - I=32 vs S=8 (24 point spread)
                    const testScores = { I: 32, S: 8, P: 26, C: 15, A: 32, G: 10 };
                    activateProfile('IP-Architect', 'The Converter', testScores);
                    keySequence = ''; clearTimeout(keyTimer);
                } else if (keySequence === '0026') {
                    // TEST: Balanced scores - minimal variance (15 point spread)
                    const testScores = { I: 24, S: 18, P: 33, C: 20, A: 20, G: 18 };
                    activateProfile('PI-Architect', 'The Converter', testScores);
                    keySequence = ''; clearTimeout(keyTimer);
```

---

## Conclusion

This implementation adds powerful testing capabilities with minimal risk and effort. The approach is clean, maintainable, and extensible for future test scenarios. Both test codes use existing profile infrastructure while providing the score visualization data needed to validate radar chart quality.

**Next Steps:**
1. Review this plan for completeness
2. Execute implementation (15-30 minutes)
3. Run verification checklist
4. Document any radar chart rendering issues discovered
5. Consider creating follow-up ticket for chart refinements if needed

**Implementation Status:** Ready to proceed with high confidence.
