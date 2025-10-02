# Content Sync System - Architecture & Implementation

**Version**: 2.0 (Revised after Quality Review)
**Date**: 2025-10-01
**Status**: Implementation Ready
**Branch**: md-analysis-test

---

## Overview

This document describes the automated system for syncing content from the human-editable Markdown file (`STTI Master Profiles.md`) to the code that powers the web application.

**Goal**: Edit Markdown → Run one command → Everything updates automatically

---

## Architecture (Simplified)

```
STTI Master Profiles.md
    ↓
[Parser + Validator]
    ↓
profiles.json (ALL 24 profiles, ALL 7 sections)
    ↓
ProfileRenderer.js (renders from JSON)
    ↓
main.js (calls ProfileRenderer)
    ↓
User sees updated content
```

**Key Principle**: Single source of truth (Markdown) → Single data file (JSON) → Single renderer (ProfileRenderer.js)

---

## Content Sections (7 per profile)

Each of the 24 profiles has these sections:

1. **Archetype Description** - Explains the dominant/secondary archetype combination
2. **Orientation Description** - Profile-specific orientation (Westerner, Easterner, etc.)
3. **Tendency Description** - Architect vs Gardener approach
4. **Overwhelmed** - How this orientation handles overwhelm
5. **Stuck/Unstuck** - Guidance for getting unstuck
6. **Prompts** - Specific questions to activate archetypes
7. **Archetype Synergy** - How the two dominant archetypes work together

---

## Implementation Phases

### Phase 1: Expand ProfileRenderer.js ✅
**Status**: Ready to implement

**What**: Add support for 3 missing sections:
- archetypeDescription
- orientationDescription
- tendencyDescription

**Why**: Currently only handles 4 sections (overwhelmed, stuckUnstuck, prompts, archetypesSynergy)

**Files Modified**:
- `Web-App/profile-renderer.js`

---

### Phase 2: Build Validation Script ✅
**Status**: Ready to implement

**What**: Create `validate-profiles.py` to check JSON correctness

**Validation Checks**:
1. Valid JSON syntax
2. All 24 profiles present
3. Each profile has all required sections
4. No empty content fields
5. Proper structure (title + content format)

**Files Created**:
- `Analysis/validate-profiles.py`

---

### Phase 3: Build Parser Script ✅
**Status**: Ready to implement

**What**: Create `sync-profiles.py` to parse Markdown and generate JSON

**Features**:
- Parses all 24 profiles from Master Content
- Extracts all 7 sections per profile
- Validates before writing
- Dry-run mode (preview changes)
- Clear success/failure messages

**Files Created**:
- `Analysis/sync-profiles.py`

---

### Phase 4: Expand profiles.json Schema ✅
**Status**: Ready to implement

**Current** (only 2 profiles, 4 sections):
```json
{
  "IS-Architect": {
    "overwhelmed": { "title": "...", "content": "..." },
    "stuckUnstuck": { "title": "...", "content": "..." },
    "prompts": { "title": "...", "content": "..." },
    "archetypesSynergy": { "title": "...", "content": "..." }
  }
}
```

**New** (all 24 profiles, 7 sections):
```json
{
  "IS-Architect": {
    "archetypeDescription": { "content": "..." },
    "orientationDescription": { "content": "..." },
    "tendencyDescription": { "content": "..." },
    "overwhelmed": { "title": "...", "content": "..." },
    "stuckUnstuck": { "title": "...", "content": "..." },
    "prompts": { "title": "...", "content": "..." },
    "archetypesSynergy": { "title": "...", "content": "..." }
  },
  "IS-Gardener": { ... },
  ... (22 more profiles)
}
```

**Files Modified**:
- `Web-App/profiles.json`

---

### Phase 5: Update main.js ✅
**Status**: Ready to implement

**What**:
- Delete hardcoded profile content blocks
- Call ProfileRenderer.js for all dynamic content
- Keep only the orchestration logic

**Files Modified**:
- `Web-App/main.js`

---

## User Workflow (After Implementation)

```bash
# 1. Edit the master content file
# Update line 21 or any other content in:
# "STTI Master Profiles.md"

# 2. Run sync (with automatic validation)
python Analysis/sync-profiles.py

# 3. Output shows results:
# ✅ Parsed 24 profiles
# ✅ All sections validated
# ✅ profiles.json updated
# ⚠️  Review changes before committing

# 4. Test locally
# Open index.html and test secret codes (0001, 0002, etc.)

# 5. Commit changes
git add Web-App/profiles.json
git commit -m "Update profile content"
git push
```

---

## Safety Features

### 1. Validation Before Writing
Parser validates structure before updating files. If validation fails, no files are changed.

### 2. Dry-Run Mode
```bash
python Analysis/sync-profiles.py --dry-run
```
Shows what would change without actually changing anything.

### 3. Git-Based Rollback
```bash
git checkout Web-App/profiles.json  # Undo changes
```

### 4. Loud Failure (Not Silent)
Parser stops immediately on errors and shows clear error messages:
- Missing profile sections
- Malformed Markdown headers
- Invalid JSON encoding

---

## Quality Review Notes

### Issues Fixed from Original Design

❌ **Original**: Update both profiles.json AND main.js
✅ **Fixed**: Only update profiles.json, delete hardcoded content

❌ **Original**: No validation layer
✅ **Fixed**: Built-in validation with clear error messages

❌ **Original**: Silent failures possible
✅ **Fixed**: Loud failures with helpful error messages

❌ **Original**: No dry-run mode
✅ **Fixed**: Preview changes before applying

❌ **Original**: All 24 profiles updated at once
✅ **Fixed**: Validation ensures all-or-nothing (prevents partial corruption)

---

## Technical Implementation Details

### Markdown Parsing Strategy

**Profile Boundary Detection**:
```markdown
## IS-Architect (Inner Guide + Synthesizer, Architect Tendency)
```
Regex: `^## ([A-Z]{2}-(Architect|Gardener))`

**Section Detection**:
```markdown
### Archetype Description
### Orientation Description
### Tendency Description
### Overwhelmed
### Stuck/Unstuck
### Prompts
### Archetype Synergy
```
Regex: `^### (Archetype Description|Orientation Description|...)`

**Content Extraction**:
- Read from section header to next `###` or `---` or end of profile
- Preserve Markdown formatting (bold, emphasis)
- Extract title/content structure where applicable

### Error Handling

**Missing Sections**:
```python
if profile missing required section:
    raise ValidationError(f"Profile {code} missing {section}")
```

**Malformed Headers**:
```python
if section header not matched:
    raise ParseError(f"Invalid header format at line {line_num}")
```

**Empty Content**:
```python
if content.strip() == "":
    raise ValidationError(f"Empty content in {profile}/{section}")
```

---

## Testing Plan

### Phase 1: Single Profile Test
1. Parse only IS-Architect from Master Content
2. Validate structure
3. Compare to existing profiles.json content
4. Verify match

### Phase 2: Two Profile Test
1. Parse IS-Architect and IS-Gardener
2. Validate structure
3. Test with ProfileRenderer.js
4. Verify secret codes 0003, 0004 work

### Phase 3: All 24 Profiles Test
1. Parse all profiles from Master Content
2. Validate complete structure
3. Test all secret codes (0001-0024)
4. Verify no console errors

### Phase 4: User Workflow Test
1. Make small edit to Master Content
2. Run sync script
3. Verify only changed content updated
4. Test affected profile loads correctly

---

## Success Criteria

✅ User can edit Master Content Markdown file
✅ User runs one command: `python sync-profiles.py`
✅ All 24 profiles update automatically
✅ Validation prevents corruption
✅ Clear error messages on failure
✅ All secret codes (0001-0024) work
✅ No console errors in browser
✅ Content matches Master Content exactly

---

## Files Modified/Created

**Created**:
- `Analysis/sync-profiles.py` - Parser + sync script
- `Analysis/validate-profiles.py` - Validation script
- `Documentation/Content-Sync-System.md` - This document

**Modified**:
- `Web-App/profiles.json` - Expanded to all 24 profiles, all 7 sections
- `Web-App/profile-renderer.js` - Added support for 3 new sections
- `Web-App/main.js` - Removed hardcoded content, calls ProfileRenderer
- `Documentation/STTI_PROJECT_SOP.md` - Added sync workflow documentation

**Deleted**:
- Hardcoded profile content blocks in main.js (replaced by ProfileRenderer)

---

## Maintenance Notes

### Updating Content (Future)
1. Edit `STTI Master Profiles.md`
2. Run `python Analysis/sync-profiles.py`
3. Test locally
4. Commit and push

### Adding New Profiles (Future)
1. Add profile section to Master Content
2. Run sync script
3. New profile automatically added to profiles.json

### Fixing Errors
- If sync fails: Read error message, fix Master Content, re-run
- If validation fails: Check Master Content structure
- If content wrong: Edit Master Content (not JSON directly)

---

## Next Steps

1. ✅ Expand ProfileRenderer.js
2. ✅ Build validation script
3. ✅ Build parser script
4. ✅ Test with one profile
5. ✅ Test with all profiles
6. ✅ Update documentation
7. ✅ Merge to main branch

---

**This is the correct, quality-reviewed architecture.**
Ready for implementation on `md-analysis-test` branch.
