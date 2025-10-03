# Comprehensive Implementation Plan for CSS Wizard Fixes

## Project Location
`/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev`

## Key Files
- **main.js** - Radar chart rendering, donut chart function (lines 817-1451)
- **styles.css** - Radar chart styling, spacing (lines 1596-1780)
- **index.html** - Score breakdown section (lines 186-300)
- **profiles.json** - Profile data with orientation descriptions
- **Web-App/profiles-data.js** - Inline profile data (duplicate of profiles.json)

---

# ISSUE CATEGORY 1: Radar Chart Visual Refinements

## 1.1 Delete Empty Space (Top and Bottom)

**Problem:** Excessive white space above "Top-down" label and below "Bottom-up" label

**File:** `styles.css`

**Current Code (lines 1600-1608):**
```css
.radar-chart-section {
    background: linear-gradient(135deg, #f8f9ff 0%, #fff5f0 100%);
    border-radius: var(--radius-md);
    border-left: 4px solid var(--lyt-purple);
    padding: var(--space-2xl);  /* Currently 2rem = 32px */
    margin-bottom: var(--space-2xl);
    text-align: center;
}
```

**Fix:**
```css
.radar-chart-section {
    background: linear-gradient(135deg, #f8f9ff 0%, #fff5f0 100%);
    border-radius: var(--radius-md);
    border-left: 4px solid var(--lyt-purple);
    padding: var(--space-lg) var(--space-2xl);  /* Change to: 1rem top/bottom, 2rem left/right */
    margin-bottom: var(--space-2xl);
    text-align: center;
}
```

**Alternative Fix (if more reduction needed):**
Also adjust the label positions in `main.js` (lines 920-923):
```javascript
// Current:
addLabelWithBackground(centerX, centerY - maxRadius - 8, 'Top-down', 'middle', 75, 20);
addLabelWithBackground(centerX, centerY + maxRadius + 18, 'Bottom-up', 'middle', 80, 20);

// Change to (reduce offsets):
addLabelWithBackground(centerX, centerY - maxRadius - 4, 'Top-down', 'middle', 75, 20);
addLabelWithBackground(centerX, centerY + maxRadius + 12, 'Bottom-up', 'middle', 80, 20);
```

---

## 1.2 Make Circles 75% of Current Size

**Problem:** Concentric grid circles are too large

**File:** `main.js`

**Current Code (line 825):**
```javascript
MAX_RADIUS: 180,
```

**Fix:**
```javascript
MAX_RADIUS: 135,  // 180 * 0.75 = 135
```

**Impact:** This will affect:
- Grid circle sizes (line 868-869)
- Axis spoke lengths (line 877-883)
- Cartesian grid lines (line 889-901)
- Quadrant gradient sizes (line 961-966)
- Y-axis label positions (line 991-992)
- All polygon/dot positions (line 1212-1214)

**Note:** Since all calculations are relative to MAX_RADIUS, changing this one constant scales everything proportionally.

---

## 1.3 Make Y-Axis Numbers Slightly Darker

**Problem:** Y-axis score labels (8, 18, 23, 28, 32) in light gray are too faint

**File:** `main.js`

**Current Code (lines 997-1001):**
```javascript
const label = createText(labelX, labelY, value.toString(), {
    'text-anchor': 'start',
    'fill': '#D1D5DB',  // Light gray - TOO FAINT
    'font-size': '12',
    'font-weight': '600'
});
```

**Fix:**
```javascript
const label = createText(labelX, labelY, value.toString(), {
    'text-anchor': 'start',
    'fill': '#9CA3AF',  // Darker gray (was #D1D5DB)
    'font-size': '12',
    'font-weight': '600'
});
```

**Color Reference:**
- Current: `#D1D5DB` (Tailwind gray-300 - very light)
- New: `#9CA3AF` (Tailwind gray-400 - medium)
- Alternative: `#6B7280` (Tailwind gray-500 - darker) if more contrast needed

---

## 1.4 Fix Gradient Center Opacity (Lightest Part Too Hot/Light)

**Problem:** Center of radial gradients (color2 with 0.1 opacity) is too bright/washed out, especially in Inner Guide (yellow) quadrant

**File:** `main.js`

**Current Code (lines 936-943):**
```javascript
const gradients = [
    { id: 'synthesizerGradient', color1: '#5dbcd2', color2: 'rgba(93, 188, 210, 0.1)' },   // Teal
    { id: 'producerGradient', color1: '#d669bc', color2: 'rgba(214, 105, 188, 0.1)' },     // Pink
    { id: 'creativeGradient', color1: '#b9adff', color2: 'rgba(185, 173, 255, 0.1)' },    // Purple
    { id: 'innerGuideGradient', color1: '#fcf601', color2: 'rgba(252, 246, 1, 0.1)' }     // Yellow - MOST PROBLEMATIC
];
```

**Fix (increase color2 opacity from 0.1 to 0.25):**
```javascript
const gradients = [
    { id: 'synthesizerGradient', color1: '#5dbcd2', color2: 'rgba(93, 188, 210, 0.25)' },
    { id: 'producerGradient', color1: '#d669bc', color2: 'rgba(214, 105, 188, 0.25)' },
    { id: 'creativeGradient', color1: '#b9adff', color2: 'rgba(185, 173, 255, 0.25)' },
    { id: 'innerGuideGradient', color1: '#fcf601', color2: 'rgba(252, 246, 1, 0.25)' }  // Yellow improved
];
```

**Reasoning:**
- 0.1 opacity = too transparent, washes out at center
- 0.25 opacity = 2.5x stronger, reduces "hot spot" effect
- Alternative: 0.3 if 0.25 still too light

---

# ISSUE CATEGORY 2: Missing Donut Chart

## 2.1 Diagnosis Checklist

**File:** `main.js`

**Function Definition:** Lines 1043-1161 (`renderArchitectGardenerDonut`)

**Function Calls:**
1. Line 1451: `renderArchitectGardenerDonut(profile.scores);` - Called in `showResults()`
2. Line 406: Also called in `activateProfile()` for secret codes

**Debug Steps:**

### Step 1: Verify SVG Element Exists
**HTML File:** `index.html` (lines 186-194)
```html
<!-- Architect vs Gardener Donut Chart -->
<div class="donut-chart-section section-box section-box--cyan">
    <div class="donut-chart-title">Architect vs Gardener Balance</div>
    <div class="donut-chart-container">
        <svg id="architectGardenerDonut" viewBox="0 0 300 300" class="donut-chart-svg">
            <title>Architect vs Gardener Tendency Balance</title>
        </svg>
    </div>
</div>
```

**Check:** Element exists ✓

### Step 2: Check Console for Debug Messages
**Current Debug Logs (lines 1044-1050):**
```javascript
console.log('🍩 Rendering donut chart with scores:', scores);
const svg = document.getElementById('architectGardenerDonut');
if (!svg) {
    console.error('❌ Donut SVG element #architectGardenerDonut not found in DOM!');
    return;
}
console.log('✓ Donut SVG element found');
```

**User needs to check browser console for:**
- "🍩 Rendering donut chart with scores: ..." (function called)
- "❌ Donut SVG element not found" (element missing)
- "✓ Donut SVG element found" (element exists)

### Step 3: Verify Scores Object Structure
**Function expects:** `scores.A` and `scores.G` (lines 1058-1060)
```javascript
const total = scores.A + scores.G;
const architectPercent = (scores.A / total) * 100;
const gardenerPercent = (scores.G / total) * 100;
```

**Potential Issue:** If `scores.A` or `scores.G` undefined, calculation fails silently

**Fix: Add Defensive Check (lines 1043-1051):**
```javascript
function renderArchitectGardenerDonut(scores) {
    console.log('🍩 Rendering donut chart with scores:', scores);

    // Defensive check for A and G scores
    if (!scores || typeof scores.A === 'undefined' || typeof scores.G === 'undefined') {
        console.error('❌ Donut chart: Invalid scores object. Expected A and G properties.', scores);
        return;
    }

    const svg = document.getElementById('architectGardenerDonut');
    if (!svg) {
        console.error('❌ Donut SVG element #architectGardenerDonut not found in DOM!');
        return;
    }
    console.log('✓ Donut SVG element found');
    console.log('✓ A:', scores.A, 'G:', scores.G);
    // ... rest of function
}
```

### Step 4: Check CSS Display/Visibility
**File:** `styles.css` (lines 1757-1779)

**Current Styles:**
```css
.donut-chart-section {
    margin-bottom: var(--space-2xl);
    text-align: center;
}

.donut-chart-svg {
    width: 100%;
    height: auto;
    filter: drop-shadow(0 4px 12px rgba(93, 188, 210, 0.15));
}
```

**Check:** No `display: none` or `visibility: hidden` ✓

### Step 5: Test with Secret Code
**Quick Test:** Press `0026` to activate test profile:
```javascript
// Line 250-255: Test profile with known scores
activateProfile('PI-Architect', 'The Converter', {
    I: 24, S: 18, P: 33, C: 20, A: 20, G: 18
});
```

This should render the donut chart with A=20, G=18.

---

## 2.2 Most Likely Causes (Ranked by Probability)

### Cause #1: Function Not Being Called (Check Console)
**Symptom:** No "🍩 Rendering donut chart" log
**Solution:** Verify `showResults()` is executing line 1451

### Cause #2: Scores Object Missing A/G Properties
**Symptom:** Console shows "🍩 Rendering" but no chart appears
**Solution:** Add defensive check (see Step 3 above)

### Cause #3: SVG Rendering Issue (Invisible SVG)
**Symptom:** Console shows "✓ Donut SVG element found" but no visual
**Solution:** Inspect element in browser DevTools to see if SVG has child elements

### Cause #4: CSS Z-Index or Overflow Issue
**Symptom:** Chart renders but is hidden behind other elements
**Solution:** Add `position: relative; z-index: 10;` to `.donut-chart-section`

---

# ISSUE CATEGORY 3: Remove Tendencies from Score Breakdown

## 3.1 Identify Section to Remove

**File:** `index.html`

**Lines to DELETE (258-286):**
```html
<!-- Tendencies Scores -->
<div class="score-category">
    <div class="score-category-label">Tendencies</div>

    <div class="score-bar-wrapper">
        <div class="score-label">
            <span class="score-name">Architect</span>
            <span class="score-value" id="score-architect">0</span>
        </div>
        <div class="score-track">
            <div class="score-baseline"></div>
            <div class="score-bar score-bar-cyan-alt" data-score="0" style="width: 0%;">
                <div class="score-marker"></div>
            </div>
        </div>
    </div>

    <div class="score-bar-wrapper">
        <div class="score-label">
            <span class="score-name">Gardener</span>
            <span class="score-value" id="score-gardener">0</span>
        </div>
        <div class="score-track">
            <div class="score-baseline"></div>
            <div class="score-bar score-bar-green" data-score="0" style="width: 0%;">
                <div class="score-marker"></div>
            </div>
        </div>
    </div>
</div>
```

**Lines to KEEP:**
- Lines 202-256: Archetypes section ✓
- Lines 289-298: Range hint and raw scores ✓

---

## 3.2 Update JavaScript (No Changes Needed)

**File:** `main.js`

**Function:** `animateScoreBars()` (lines 775-795)

**Current Code Still Valid:**
```javascript
// Lines 786-788: These lines still needed for donut chart
animateBar('score-architect', scores.A, THEORETICAL_MIN, THEORETICAL_MAX);
animateBar('score-gardener', scores.G, THEORETICAL_MIN, THEORETICAL_MAX);
```

**Important:** Even though we're removing the visual bars from HTML, the JavaScript calls are harmless (they'll just fail silently because element IDs don't exist). The scores are still used for the donut chart.

**Optional Cleanup (lines 786-788):** Comment out or delete these lines:
```javascript
// Removed: Tendency bars no longer displayed in Score Breakdown
// animateBar('score-architect', scores.A, THEORETICAL_MIN, THEORETICAL_MAX);
// animateBar('score-gardener', scores.G, THEORETICAL_MIN, THEORETICAL_MAX);
```

---

## 3.3 Keep Raw Scores Display

**File:** `index.html` (lines 295-298)

**KEEP THIS (shows A and G in raw text):**
```html
<!-- Raw scores display -->
<div class="raw-scores">
    <span class="raw-scores-label">Raw Scores:</span>
    <span id="raw-scores-text">I: 0, S: 0, C: 0, P: 0 | A: 0, G: 0</span>
</div>
```

**Reasoning:** User only wants to remove the visual BARS, not the numerical A/G data.

---

# ISSUE CATEGORY 4: Change Directional Terms to Adjective Forms

## 4.1 Global Text Replacements Needed

**Pattern:**
- `Easterner` → `Eastern` (noun → adjective)
- `Easterners` → `Eastern profiles` OR `Eastern` (context-dependent)
- `Westerner` → `Western`
- `Westerners` → `Western profiles` OR `Western`
- `Northerner` → `Northern`
- `Northerners` → `Northern profiles` OR `Northern`
- `Southerner` → `Southern`

---

## 4.2 File: main.js (3 instances)

**Lines 499-504:**
```javascript
// BEFORE:
if (sortedArchetypes === 'IS') {
    orientation = 'Westerner';
} else if (sortedArchetypes === 'CP') {
    orientation = 'Easterner';
} else if (sortedArchetypes === 'PS') {
    orientation = 'Northerner';
}

// AFTER:
if (sortedArchetypes === 'IS') {
    orientation = 'Western';
} else if (sortedArchetypes === 'CP') {
    orientation = 'Eastern';
} else if (sortedArchetypes === 'PS') {
    orientation = 'Northern';
}
```

---

## 4.3 File: index.html (3 instances)

**Line 166:**
```html
<!-- BEFORE: -->
<div class="orientation-pill" id="orientationPill">Westerner</div>

<!-- AFTER: -->
<div class="orientation-pill" id="orientationPill">Western</div>
```

**Line 327:**
```html
<!-- BEFORE: -->
<div class="section-title space-grotesk-font collapsed" onclick="toggleSection('overwhelmedContent', this)">When Westerners feel overwhelmed…</div>

<!-- AFTER: -->
<div class="section-title space-grotesk-font collapsed" onclick="toggleSection('overwhelmedContent', this)">When Western profiles feel overwhelmed…</div>
```

**Line 337:**
```html
<!-- BEFORE: -->
When you combine your Westerner archetypes of Inner Guide and Synthesizer with an Architect tendency, we now can understand...

<!-- AFTER: -->
When you combine your Western archetypes of Inner Guide and Synthesizer with an Architect tendency, we now can understand...
```

---

## 4.4 Files: profiles.json and Web-App/profiles-data.js (Extensive Changes)

**Total Replacements Needed:** ~80 instances across both files

### Replacement Strategy (Use Find & Replace in Editor)

**Find & Replace Pairs (in order):**

1. **Find:** `As an <strong>IS-Architect</strong>, you have a <strong>Westerner</strong> profile`
   **Replace:** `As an <strong>IS-Architect</strong>, you have a <strong>Western</strong> profile`

2. **Find:** `As an <strong>IS-Gardener</strong>, you have a <strong>Westerner</strong> profile`
   **Replace:** `As an <strong>IS-Gardener</strong>, you have a <strong>Western</strong> profile`

3. **Find:** `As a <strong>PC-Architect</strong>, you have an <strong>Easterner</strong> profile`
   **Replace:** `As a <strong>PC-Architect</strong>, you have an <strong>Eastern</strong> profile`

4. **Find:** `As a <strong>PC-Gardener</strong>, you have an <strong>Easterner</strong> profile`
   **Replace:** `As a <strong>PC-Gardener</strong>, you have an <strong>Eastern</strong> profile`

5. **Find:** `Westerners are known as "philosophers."`
   **Replace:** `Western profiles are known as "philosophers."`

6. **Find:** `Easterners are known as "makers."`
   **Replace:** `Eastern profiles are known as "makers."`

7. **Find:** `Northerners are known as "builders."`
   **Replace:** `Northern profiles are known as "builders."`

8. **Find:** `When Westerners feel overwhelmed`
   **Replace:** `When Western profiles feel overwhelmed`

9. **Find:** `When Easterners feel overwhelmed`
   **Replace:** `When Eastern profiles feel overwhelmed`

10. **Find:** `When Northerners feel overwhelmed`
    **Replace:** `When Northern profiles feel overwhelmed`

11. **Find:** `your Westerner archetypes`
    **Replace:** `your Western archetypes`

12. **Find:** `your Easterner archetypes`
    **Replace:** `your Eastern archetypes`

13. **Find:** `your Northerner archetypes`
    **Replace:** `your Northern archetypes`

14. **Find:** `when Easterners feel`
    **Replace:** `when Eastern profiles feel`

15. **Find:** `when Northerners benefit`
    **Replace:** `when Northern profiles benefit`

**IMPORTANT:** Perform replacements in BOTH files:
- `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/profiles.json`
- `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/Web-App/profiles-data.js`

---

# Summary Checklist

## Radar Chart Refinements
- [ ] Reduce `.radar-chart-section` padding (styles.css line 1605)
- [ ] Optional: Adjust label offsets (main.js lines 920-921)
- [ ] Change `MAX_RADIUS` from 180 to 135 (main.js line 825)
- [ ] Change Y-axis label color from `#D1D5DB` to `#9CA3AF` (main.js line 999)
- [ ] Change gradient color2 opacity from 0.1 to 0.25 (main.js lines 938-941)

## Donut Chart Debug
- [ ] Check browser console for debug messages
- [ ] Add defensive check for scores.A and scores.G (main.js line 1046)
- [ ] Test with secret code `0026`
- [ ] Inspect element in DevTools to verify SVG contents

## Remove Tendencies Section
- [ ] Delete lines 258-286 from index.html
- [ ] Optional: Comment out lines 786-788 in main.js

## Directional Term Replacements
- [ ] Update main.js lines 499-504 (3 instances)
- [ ] Update index.html lines 166, 327, 337 (3 instances)
- [ ] Perform 15 find & replace operations in profiles.json
- [ ] Perform 15 find & replace operations in Web-App/profiles-data.js

---

# Testing Plan

1. **Test Radar Chart:**
   - Use secret code `0026` (balanced scores)
   - Verify circles are 75% smaller
   - Verify no excess padding top/bottom
   - Verify Y-axis numbers are darker
   - Verify gradients have less bright center

2. **Test Donut Chart:**
   - Use secret code `0026` (A:20, G:18)
   - Verify donut renders with correct percentages
   - Check console for debug messages

3. **Test Score Breakdown:**
   - Verify only 4 archetype bars show
   - Verify no Architect/Gardener bars
   - Verify raw scores still display

4. **Test Directional Terms:**
   - Test each of the 24 profiles (codes 0001-0024)
   - Verify "Western", "Eastern", "Northern", "Southern" appear
   - Verify no "Westerner", "Easterner", "Northerner" remain

---

# Files to Modify (Summary)

1. **styles.css** - 1 change (padding reduction)
2. **main.js** - 4 changes (MAX_RADIUS, color, opacity, orientation terms)
3. **index.html** - 4 changes (delete tendencies section, 3 term replacements)
4. **profiles.json** - ~40 find & replace operations
5. **Web-App/profiles-data.js** - ~40 find & replace operations (identical to profiles.json)

**Total Estimated Changes:** ~90 modifications across 5 files
