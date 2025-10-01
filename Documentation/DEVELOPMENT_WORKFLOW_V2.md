# STTI Assessment - Development Workflow v2.0

## Repository Setup - Separate Folders for Maximum Safety

You now have a **professional two-repository setup with completely separate folders**:

### **🔴 Production Repository & Folder (LIVE)**
- **Folder**: `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment/`
- **Repository**: https://github.com/nickmilo/stti-assessment
- **Live Site**: https://nickmilo.github.io/stti-assessment/Web-App/
- **Purpose**: Live, stable version - users interact with this
- **Rule**: ⚠️ **NEVER** edit files here - this is production!
- **Git Remote**: `origin` and `dev` (dual setup)

### **🟡 Development Repository & Folder (TESTING)**
- **Folder**: `/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/`
- **Repository**: https://github.com/nickmilo/stti-assessment-dev
- **Live Dev Site**: https://nickmilo.github.io/stti-assessment-dev/
- **Purpose**: Testing, experimentation, new features
- **Rule**: 🎯 **DO ALL YOUR WORK HERE** - this is your playground!
- **Git Remote**: `origin` (points to dev repo)

## Your New Improved Workflow

### **Daily Development Work (ALWAYS in Dev Folder)**

```bash
# 1. Navigate to DEVELOPMENT folder (not production!)
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/Analysis"

# 2. Make changes using the safe tools
# Example: Safe text replacement
python3 safe_text_replacer.py "old text" "new text" --preview
python3 safe_text_replacer.py "old text" "new text"

# Example: Safe profile implementation
python3 implement_profiles_v2.py --batch SC --log-level INFO

# 3. Commit changes locally
git add .
git commit -m "Description of changes"

# 4. Push to DEVELOPMENT repo and see changes live instantly
git push origin main
```

### **Testing & Validation**

```bash
# Test the development version online at:
# 🌐 https://nickmilo.github.io/stti-assessment-dev/

# Run local validation
python3 implement_profiles_v2.py --validate-only

# Check logs for any issues
tail -f Analysis/stti_profile_implementation.log
```

### **Promoting to Production (Only When Confident)**

```bash
# 1. Navigate to PRODUCTION folder
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment/"

# 2. Pull latest changes from development
git pull dev main

# 3. Push to production (only tested changes!)
git push origin main

# Production site updates at:
# 🌐 https://nickmilo.github.io/stti-assessment/Web-App/
```

## Live Sites You Can Access

### **🟡 Development Site (Make Changes Here)**
**URL**: https://nickmilo.github.io/stti-assessment-dev/

- Updates **automatically** when you push to dev repo
- Perfect for testing changes before going live
- Safe to break - doesn't affect users

### **🔴 Production Site (Live for Users)**
**URL**: https://nickmilo.github.io/stti-assessment/Web-App/

- Only update this when confident changes work
- This is what users see
- Keep this stable and working

## Repository Commands Quick Reference

### **Development Work Commands**
```bash
# Always work in the DEV folder
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/"

# Check git status
git status

# Make changes, then commit and push
git add .
git commit -m "Clear description of changes"
git push origin main

# See changes live at: https://nickmilo.github.io/stti-assessment-dev/
```

### **Production Promotion Commands**
```bash
# Switch to production folder
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment/"

# Pull tested changes from development
git pull dev main

# Push to production
git push origin main

# Live site updates at: https://nickmilo.github.io/stti-assessment/Web-App/
```

## Safety Features Built In

### **Complete Folder Separation**
- **Development folder**: `/STTI Assessment Dev/` - Your playground
- **Production folder**: `/STTI Assessment/` - Protected, stable version
- **Impossible to accidentally push dev changes to production**

### **Automatic Backups**
- Every change creates timestamped backup in `Analysis/backups/`
- Backups have format: `index_backup_YYYYMMDD_HHMMSS.html`

### **Live Testing**
- See every change immediately at https://nickmilo.github.io/stti-assessment-dev/
- Test thoroughly before promoting to production

### **Rollback Capability**
```bash
# If something breaks in development
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/Analysis"
python3 -c "
from utils import STTIFileHandler
handler = STTIFileHandler()
handler.rollback()  # Uses most recent backup
"
```

## Development Best Practices

### **1. Always Work in Development Folder**
```bash
# ✅ CORRECT - Work here
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/"

# ❌ WRONG - Don't edit production files
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment/"
```

### **2. Always Preview First**
```bash
# Preview mode shows what will change WITHOUT making changes
python3 safe_text_replacer.py "old" "new" --preview
```

### **3. Test Live Before Promoting**
- Make changes in development folder
- Push to see live at https://nickmilo.github.io/stti-assessment-dev/
- Only promote to production when everything works

### **4. Small, Focused Commits**
```bash
# Good commit messages
git commit -m "Update terminology: Southerner → Southern"
git commit -m "Add validation for SC-Architect profile"
git commit -m "Fix HTML syntax in overwhelmed content"
```

## Emergency Procedures

### **If Development Site Breaks**
1. **Don't worry** - production is safe
2. Check `Analysis/stti_profile_implementation.log` for errors
3. Use automatic rollback: `handler.rollback()`
4. Restore from backup in `Analysis/backups/`

### **If Production Site Breaks**
1. **Don't panic** - you have backups and development copy
2. Use git to revert: `git revert HEAD`
3. Push the revert: `git push origin main`
4. Fix the issue in development first, then re-promote

## File Structure

```
/Users/nick/Dropbox/+/AI/Efforts/Active/
├── STTI Assessment/                    # 🔴 PRODUCTION (Don't edit here!)
│   ├── Web-App/index.html                 # Live production file
│   └── [other production files]
│
└── STTI Assessment Dev/                # 🟡 DEVELOPMENT (Work here!)
    ├── Analysis/                          # 🔧 Development tools
    │   ├── safe_text_replacer.py             # Safe text replacement
    │   ├── implement_profiles_v2.py          # Modern profile implementation
    │   ├── config.py                         # Centralized configuration
    │   ├── utils.py                          # Safe file operations
    │   ├── backups/                          # Automatic backups
    │   └── stti_profile_implementation.log
    ├── Web-App/                           # 🌐 The actual assessment
    │   └── index.html                        # Development HTML file
    └── [other development files]
```

## Quick Start Guide

### **Making Your First Change**

1. **Open development folder**
   ```bash
   cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment Dev/Analysis"
   ```

2. **Make a safe change**
   ```bash
   python3 safe_text_replacer.py "test" "TEST" --preview
   python3 safe_text_replacer.py "test" "TEST"
   ```

3. **Commit and push**
   ```bash
   git add . && git commit -m "Test change" && git push origin main
   ```

4. **See it live**
   - Visit: https://nickmilo.github.io/stti-assessment-dev/
   - Check that your change worked

5. **Promote to production when ready**
   ```bash
   cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment/"
   git pull dev main && git push origin main
   ```

## Success Metrics

✅ **Separate folder setup complete** - Maximum safety guaranteed
✅ **Development repository**: https://github.com/nickmilo/stti-assessment-dev
✅ **Production repository**: https://github.com/nickmilo/stti-assessment
✅ **Live development site**: https://nickmilo.github.io/stti-assessment-dev/
✅ **Live production site**: https://nickmilo.github.io/stti-assessment/Web-App/
✅ **Safe development tools** with automatic backup and validation
✅ **Impossible to accidentally break production**

**You now have a bulletproof development workflow!**