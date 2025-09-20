#!/usr/bin/env python3
"""
STTI Assessment Configuration
Centralized configuration for all profile implementation scripts
"""

import os
from pathlib import Path

# Base paths - relative to this config file
CONFIG_DIR = Path(__file__).parent
PROJECT_ROOT = CONFIG_DIR.parent
WEB_APP_DIR = PROJECT_ROOT / "Web-App"
ANALYSIS_DIR = PROJECT_ROOT / "Analysis"

# Critical files
HTML_FILE = WEB_APP_DIR / "index.html"
BACKUP_DIR = ANALYSIS_DIR / "backups"

# Create backup directory if it doesn't exist
BACKUP_DIR.mkdir(exist_ok=True)

# Validation settings
REQUIRED_FILES = [HTML_FILE]
INSERTION_MARKERS = {
    'main': "return; // Exit early, don't use generic logic\n            }\n            \n            // Set overwhelmed content"
}

def validate_environment():
    """Validate that all required files and directories exist"""
    missing_files = []

    for file_path in REQUIRED_FILES:
        if not file_path.exists():
            missing_files.append(str(file_path))

    if missing_files:
        raise FileNotFoundError(f"Missing required files: {missing_files}")

    return True

def get_html_path():
    """Get the absolute path to the HTML file"""
    return str(HTML_FILE.resolve())

def get_backup_path():
    """Get the absolute path to the backup directory"""
    return str(BACKUP_DIR.resolve())

# Environment validation on import
if __name__ != "__main__":
    try:
        validate_environment()
    except FileNotFoundError as e:
        print(f"WARNING: Configuration validation failed: {e}")