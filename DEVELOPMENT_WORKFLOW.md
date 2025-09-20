# STTI Assessment - Development Workflow

## Repository Setup

You now have a **professional two-repository setup**:

### **🔴 Production Repository (LIVE)**
- **URL**: https://github.com/nickmilo/stti-assessment
- **Purpose**: Live, stable version - users interact with this
- **Rule**: Never push untested changes here
- **Git Remote**: `origin`

### **🟡 Development Repository (TESTING)**
- **URL**: https://github.com/nickmilo/stti-assessment-dev
- **Purpose**: Testing, experimentation, new features
- **Rule**: This is your playground - break things safely here
- **Git Remote**: `dev`

## Your New Workflow

### **Daily Development Work**

```bash
# 1. Make changes locally using the safe tools
cd "/Users/nick/Dropbox/+/AI/Efforts/Active/STTI Assessment/Analysis"

# Example: Safe text replacement
python3 safe_text_replacer.py "old text" "new text" --preview
python3 safe_text_replacer.py "old text" "new text"

# Example: Safe profile implementation
python3 implement_profiles_v2.py --batch SC --log-level INFO

# 2. Commit changes locally
git add .
git commit -m "Description of changes"

# 3. Push to DEVELOPMENT repo for testing
git push dev main
```

### **Testing & Validation**

```bash
# Test the development version online at:
# https://nickmilo.github.io/stti-assessment-dev/Web-App/

# Run local validation
python3 implement_profiles_v2.py --validate-only

# Check logs for any issues
tail -f Analysis/stti_profile_implementation.log
```

### **Promoting to Production**

**Only when you're confident everything works:**

```bash
# Push tested changes to production
git push origin main

# Production site updates at:
# https://nickmilo.github.io/stti-assessment/Web-App/
```

## Repository Commands Quick Reference

```bash
# Check which remotes you have
git remote -v

# See status of both repos
git log --oneline -5  # Your local commits

# Push to development (testing)
git push dev main

# Push to production (live site)
git push origin main

# Pull latest from production (if working on multiple machines)
git pull origin main
```

## Safety Features Built In

### **Automatic Backups**
- Every change creates timestamped backup in `Analysis/backups/`
- Backups have format: `index_backup_YYYYMMDD_HHMMSS.html`

### **Rollback Capability**
```bash
# If something breaks, rollback from backup
cd Analysis
python3 -c "
from utils import STTIFileHandler
handler = STTIFileHandler()
# List backups
import os
backups = [f for f in os.listdir('backups') if f.endswith('.html')]
print('Available backups:', backups[-5:])  # Show last 5
"

# Manual rollback (replace with actual backup filename)
cp backups/index_backup_20250920_102131.html ../Web-App/index.html
```

### **Validation Checks**
- All text replacements are validated before saving
- HTML syntax checking prevents broken markup
- Content verification ensures changes were applied correctly

## Development Best Practices

### **1. Always Preview First**
```bash
# Preview mode shows what will change WITHOUT making changes
python3 safe_text_replacer.py "old" "new" --preview
```

### **2. Test in Development First**
- Never push untested changes to production
- Use the development repo URL to verify changes work

### **3. Small, Focused Commits**
```bash
# Good commit messages
git commit -m "Update terminology: Southerner → Southern"
git commit -m "Add validation for SC-Architect profile"
git commit -m "Fix HTML syntax in overwhelmed content"

# Bad commit messages
git commit -m "stuff"
git commit -m "fix"
```

### **4. Use the Logging**
```bash
# Monitor what's happening
tail -f Analysis/stti_profile_implementation.log

# Debug mode for detailed info
python3 safe_text_replacer.py "old" "new" --log-level DEBUG
```

## Emergency Procedures

### **If Development Site Breaks**
1. Check `Analysis/stti_profile_implementation.log` for errors
2. Use automatic rollback: `handler.rollback()`
3. Restore from backup in `Analysis/backups/`
4. Re-run validation: `python3 implement_profiles_v2.py --validate-only`

### **If Production Site Breaks**
1. **Don't panic** - you have backups
2. Use git to revert: `git revert HEAD`
3. Push the revert: `git push origin main`
4. Fix the issue in development first, then re-promote

## File Structure

```
STTI Assessment/
├── Analysis/                 # 🔧 Development tools (NEW!)
│   ├── safe_text_replacer.py    # Safe text replacement
│   ├── implement_profiles_v2.py # Modern profile implementation
│   ├── config.py                # Centralized configuration
│   ├── utils.py                 # Safe file operations
│   ├── backups/                 # Automatic backups
│   └── stti_profile_implementation.log
├── Web-App/                  # 🌐 The actual assessment
│   └── index.html              # Main HTML file
├── Assets/                   # 🎨 Images and fonts
├── Documentation/           # 📚 Project docs
└── x/                       # 🗄️ Archive/old files
```

## Success Metrics

✅ **You've successfully set up professional development workflow**
✅ **Development repository**: https://github.com/nickmilo/stti-assessment-dev
✅ **Production repository**: https://github.com/nickmilo/stti-assessment
✅ **Safe development tools** with automatic backup and validation
✅ **Clear promotion path** from development → production

**You can now experiment safely without fear of breaking the live site!**