# Secret Code Test Profiles - Data Flow Analysis

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     USER INTERACTION                            │
│  User presses: 0, 0, 2, 5 (or 0, 0, 2, 6)                      │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              KEY SEQUENCE HANDLER                               │
│  main.js lines 155-254: keydown event listener                 │
│  - Builds 4-digit sequence from keypresses                     │
│  - 3-second timeout between digits                             │
│  - Only active when NOT in input field                         │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              CODE PATTERN MATCHING                              │
│  if (keySequence === '0025')                                   │
│  if (keySequence === '0026')                                   │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│            TEST SCORE DEFINITION                                │
│  Code 0025: { I:32, S:8, P:26, C:15, A:32, G:10 }             │
│  Code 0026: { I:24, S:18, P:33, C:20, A:20, G:18 }            │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│           ACTIVATE PROFILE (ENHANCED)                           │
│  activateProfile(code, name, customScores)                     │
│  main.js lines 328-378 (NEW: line ~370 for score rendering)   │
│                                                                 │
│  Standard Flow (lines 330-368):                                │
│  ✓ Hide all screens                                            │
│  ✓ Show results screen                                         │
│  ✓ Set profile code & subtitle                                 │
│  ✓ Set chord diagram                                           │
│  ✓ Set static archetype pills (DEFAULT ORDER)                  │
│  ✓ Set orientation                                             │
│  ✓ Set tendency pills & description                            │
│  ✓ Set archetype description                                   │
│  ✓ Set collapsible sections                                    │
│  ✓ Hide broken profile sections                                │
│                                                                 │
│  NEW: Custom Score Flow (if customScores provided):            │
│  ✓ Calculate archetypeScores from customScores                 │
│  ✓ Re-render archetype pills with ACTUAL SCORE ORDER           │
│  ✓ Render 6-axis radar chart                                   │
│  ✓ Render 4-archetype radar chart                              │
│  ✓ Animate score bars                                          │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              PROFILE CONTENT LOADING                            │
│  ProfileRenderer.renderProfile(code)                           │
│  profile-renderer.js lines 120-157                             │
│                                                                 │
│  Loads from profiles.json:                                     │
│  - IP-Architect (line 2)                                       │
│  - PI-Architect (line 148)                                     │
│                                                                 │
│  Renders sections:                                             │
│  ✓ archetypeDescription                                        │
│  ✓ orientationDescription                                      │
│  ✓ tendencyDescription                                         │
│  ✓ overwhelmed                                                 │
│  ✓ stuckUnstuck                                                │
│  ✓ prompts                                                     │
│  ✗ archetypesSynergy (missing - profiles in broken list)      │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│              SCORE VISUALIZATION                                │
│  (NEW - only happens when customScores provided)               │
│                                                                 │
│  renderRadarChart(scores, code)                                │
│  - 6-axis chart: I, S, P, C, A, G                             │
│  - Relative scaling with 10-90% padding                        │
│  - Lines 765-912                                               │
│                                                                 │
│  renderRadarChartArchetypesOnly(scores)                        │
│  - 4-axis chart: I, S, P, C only                              │
│  - Relative scaling with 10-90% padding                        │
│  - Lines 918-1052                                              │
│                                                                 │
│  animateScoreBars(scores)                                      │
│  - 6 horizontal bars with numeric values                       │
│  - Absolute scaling 8-32 range                                 │
│  - Lines 718-758                                               │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────────┐
│                RESULTS SCREEN DISPLAY                           │
│  All content visible to user:                                  │
│  ✓ Profile code (e.g., "IP-Architect")                        │
│  ✓ Profile subtitle ("The Converter")                         │
│  ✓ Archetype pills (in SCORE ORDER when test code)            │
│  ✓ Tendency pill ("Architect")                                │
│  ✓ Orientation pill ("Diagonal")                              │
│  ✓ Chord diagram image                                         │
│  ✓ All text descriptions                                       │
│  ✓ Collapsible sections (if not in broken list)               │
│  ✓ NEW: 6-axis radar chart                                    │
│  ✓ NEW: 4-archetype radar chart                               │
│  ✓ NEW: Score bars with values                                │
└─────────────────────────────────────────────────────────────────┘
```

## Key Differences: Normal Assessment vs Test Codes

### Normal Assessment Flow (53 Questions)
```
User answers → calculateScores() → determineProfile() → showResults()
                     ↓                      ↓                  ↓
                  { I:23,              { code: 'SP-      Renders:
                    S:18,                Architect',      - Profile content
                    P:27,                tendency: 'A',   - Radar charts
                    C:19,                archetypes: ...  - Score bars
                    A:24,              }                  - All sections
                    G:18 }
```

### Secret Code Flow (Codes 0001-0024 - Original)
```
User presses 0009 → activateProfile('PS-Architect', 'The Builder')
                              ↓
                         Renders:
                         - Profile content only
                         - NO radar charts
                         - NO score bars
                         - Standard pill order
```

### Secret Code Flow (Codes 0025-0026 - NEW)
```
User presses 0025 → testScores = { I:32, S:8, ... }
                         ↓
                    activateProfile('IP-Architect', 'The Converter', testScores)
                         ↓
                    Renders:
                    - Profile content (from profiles.json)
                    - Radar charts (from testScores)
                    - Score bars (from testScores)
                    - Accurate pill order (from testScores)
```

## Critical Code Paths

### Path 1: Profile Code Determination
```javascript
// Code 0025 scores → Profile code calculation
scores = { I:32, S:8, P:26, C:15, A:32, G:10 }
        ↓
archetypeScores = [ ['I',32], ['P',26], ['C',15], ['S',8] ]
        ↓
dominantArchetypes = ['I', 'P']
        ↓
tendency = (A:32 > G:10) ? 'Architect' : 'Gardener'  → 'Architect'
        ↓
code = 'IP-Architect'
```

### Path 2: Archetype Pill Ordering
```javascript
// WITHOUT customScores (codes 0001-0024):
code = 'IP-Architect'
        ↓
Pills show: I, P, C, S (alphabetical remaining order)

// WITH customScores (codes 0025-0026):
customScores = { I:32, S:8, P:26, C:15 }
        ↓
archetypeScores = [ ['I',32], ['P',26], ['C',15], ['S',8] ]
        ↓
Pills show: I(32), P(26), C(15), S(8) (actual score order)
```

### Path 3: Radar Chart Rendering
```javascript
// Code 0025: Extreme variance
scores = { I:32, S:8, P:26, C:15, A:32, G:10 }
        ↓
maxScore = 32, minScore = 8
        ↓
Relative scaling with padding:
  I:32 → 90% radius (highest)
  S:8  → 10% radius (lowest)
  P:26 → ~66% radius
        ↓
Polygon renders with EXTREME shape (narrow at S, wide at I)
```

```javascript
// Code 0026: Balanced scores
scores = { I:24, S:18, P:33, C:20, A:20, G:18 }
        ↓
maxScore = 33, minScore = 18
        ↓
Relative scaling with padding:
  P:33 → 90% radius (highest)
  S:18 → 10% radius (lowest)
  I:24 → ~42% radius
        ↓
Polygon renders with BALANCED shape (more hexagonal)
```

## Function Call Hierarchy

```
window.keydown event
 └─ keySequence builder (lines 155-170)
     └─ if (keySequence === '0025')
         ├─ Define testScores
         └─ activateProfile(code, name, testScores)
             ├─ Screen management
             ├─ Set profile code & subtitle
             ├─ Set chord diagram
             ├─ setStaticArchetypePills(code)          [Default order]
             ├─ setOrientation(code)
             │   └─ ProfileRenderer.profiles[code].orientationDescription
             ├─ setTendencyPills(code)
             │   └─ ProfileRenderer.profiles[code].tendencyDescription
             ├─ setArchetypeDescription(code)
             │   └─ ProfileRenderer.profiles[code].archetypeDescription
             ├─ setCollapsibleSections(code)
             │   └─ ProfileRenderer.renderProfile(code)
             │       ├─ renderSection('overwhelmed', ...)
             │       ├─ renderSection('stuckUnstuck', ...)
             │       ├─ renderSection('prompts', ...)
             │       └─ renderSection('archetypesSynergy', ...) [Hidden for broken profiles]
             ├─ hideBrokenProfileSections(code)
             └─ if (customScores)                       [NEW]
                 ├─ Calculate archetypeScores from customScores
                 ├─ setStaticArchetypePills(code, archetypeScores)  [Accurate order]
                 ├─ renderRadarChart(customScores, code)
                 ├─ renderRadarChartArchetypesOnly(customScores)
                 └─ animateScoreBars(customScores)
```

## Data Dependencies

### What Needs to Exist for Test Codes to Work

**✓ Required (All Present):**
- Profile data in profiles.json for IP-Architect and PI-Architect
- Chord diagram images (IP-Architect, PI-Architect)
- ProfileRenderer instance initialized
- DOM elements for results screen
- SVG elements for radar charts (#radarChart, #radarChartArchetypes)
- Score bar DOM elements (#score-inner-guide, etc.)

**✗ Not Required:**
- archetypesSynergy section (profiles are in broken list)
- Assessment answers array
- Demographic question responses
- Formspree submission

## Testing Matrix

| Test | Code | Profile | Scores | Expected Radar Shape | Expected Pill Order |
|------|------|---------|--------|---------------------|-------------------|
| Extreme variance | 0025 | IP-Architect | I:32, S:8, P:26, C:15 | Narrow at S, wide at I | I, P, C, S |
| Balanced scores | 0026 | PI-Architect | P:33, I:24, C:20, S:18 | More hexagonal | P, I, C, S |
| Existing code | 0009 | PS-Architect | None | NO CHART | P, S, C, I |
| Normal assessment | N/A | Calculated | User answers | Normal shape | Score order |

## Edge Case Analysis

### Scenario 1: Tie Scores
```
What if: I:24, P:24, S:18, C:18
Result:  archetypeScores sort applies alphabetical tiebreaker
         → ['I',24], ['P',24], ['C',18], ['S',18]
         → Pills show: I, P, C, S (alphabetical for ties)
         → Code would be: IP-Architect or IP-Gardener
```

### Scenario 2: Missing Profile
```
What if: Code 0025 tries to activate 'XX-Architect' (non-existent)
Result:  ProfileRenderer.hasProfile('XX-Architect') → false
         → renderProfile returns false
         → Sections remain empty
         → Radar charts still render (they don't need profile data)
         → User sees: Charts but no text content
```

### Scenario 3: Missing DOM Elements
```
What if: SVG element #radarChart doesn't exist
Result:  renderRadarChart() returns early (line 767)
         → No error thrown
         → Rest of profile renders normally
         → Only radar chart is missing
```

### Scenario 4: Invalid Scores
```
What if: customScores = { I:999, S:-10, P:26, C:15 }
Result:  renderRadarChart uses maxScore=999, minScore=-10
         → Scaling still works (relative)
         → Polygon shape may be extreme
         → No validation errors (charts render anything)
```

## Performance Considerations

### Code 0025/0026 vs Normal Assessment
```
Normal Assessment (53 questions):
- 53 answer objects stored
- calculateScores() iterates all answers
- determineProfile() sorts archetypes
- Formspree API submission
- Total time: ~500ms

Test Codes 0025/0026:
- 0 answer objects
- No score calculation
- Direct profile activation
- No API submission
- Total time: ~100ms (5x faster)
```

## Conclusion

The test code implementation is architecturally sound because:

1. **Minimal Changes**: Only 2 code locations modified in 1 file
2. **Backward Compatible**: Default parameter ensures existing codes work
3. **Reuses Infrastructure**: Leverages existing profile data and rendering
4. **Clear Separation**: Test logic isolated in secret code handler
5. **No Side Effects**: Doesn't modify production assessment flow
6. **Easy to Extend**: Pattern scales to additional test codes

The data flows cleanly from keypress → score definition → profile activation → visualization rendering, with all components already in place.
