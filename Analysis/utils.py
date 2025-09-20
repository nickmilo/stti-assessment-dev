#!/usr/bin/env python3
"""
STTI Assessment Utilities
Shared utilities for safe file operations, error handling, and logging
"""

import os
import shutil
import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

from config import get_html_path, get_backup_path, INSERTION_MARKERS

# Configure logging
def setup_logging(log_level=logging.INFO):
    """Setup comprehensive logging for profile implementation"""
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=log_level,
        format=log_format,
        handlers=[
            logging.FileHandler('stti_profile_implementation.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

class STTIFileHandler:
    """Safe file handler for STTI HTML modifications"""

    def __init__(self):
        self.html_path = get_html_path()
        self.backup_dir = get_backup_path()
        self.content = None
        self.backup_path = None

    def create_backup(self) -> str:
        """Create a timestamped backup of the HTML file"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_filename = f"index_backup_{timestamp}.html"
            backup_path = os.path.join(self.backup_dir, backup_filename)

            shutil.copy2(self.html_path, backup_path)
            self.backup_path = backup_path
            logger.info(f"Backup created: {backup_path}")
            return backup_path

        except Exception as e:
            logger.error(f"Failed to create backup: {e}")
            raise

    def load_html(self) -> str:
        """Safely load HTML content with error handling"""
        try:
            if not os.path.exists(self.html_path):
                raise FileNotFoundError(f"HTML file not found: {self.html_path}")

            with open(self.html_path, 'r', encoding='utf-8') as f:
                self.content = f.read()

            if not self.content.strip():
                raise ValueError("HTML file is empty")

            logger.info(f"HTML loaded successfully: {len(self.content)} characters")
            return self.content

        except FileNotFoundError:
            logger.error(f"HTML file not found: {self.html_path}")
            raise
        except PermissionError:
            logger.error(f"Permission denied accessing: {self.html_path}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error loading HTML: {e}")
            raise

    def validate_insertion_point(self, search_string: str) -> int:
        """Validate and return insertion point location"""
        if not self.content:
            raise ValueError("No content loaded. Call load_html() first.")

        insertion_points = []
        start = 0
        while True:
            pos = self.content.find(search_string, start)
            if pos == -1:
                break
            insertion_points.append(pos)
            start = pos + 1

        if len(insertion_points) == 0:
            raise ValueError(f"Insertion point not found: {search_string[:50]}...")
        elif len(insertion_points) > 1:
            logger.warning(f"Multiple insertion points found ({len(insertion_points)}), using first one")

        logger.info(f"Insertion point validated at position: {insertion_points[0]}")
        return insertion_points[0]

    def insert_content(self, insertion_point: int, new_content: str) -> bool:
        """Insert content at specified point with validation"""
        try:
            if not self.content:
                raise ValueError("No content loaded")

            if insertion_point < 0 or insertion_point > len(self.content):
                raise ValueError(f"Invalid insertion point: {insertion_point}")

            # Create new content
            updated_content = (
                self.content[:insertion_point] +
                new_content +
                self.content[insertion_point:]
            )

            # Basic validation - ensure we didn't break HTML structure
            if updated_content.count('<') != updated_content.count('>'):
                logger.warning("HTML tag mismatch detected after insertion")

            self.content = updated_content
            logger.info(f"Content inserted successfully: {len(new_content)} characters")
            return True

        except Exception as e:
            logger.error(f"Failed to insert content: {e}")
            raise

    def save_html(self, validate_syntax: bool = True) -> bool:
        """Save HTML with optional syntax validation"""
        try:
            if not self.content:
                raise ValueError("No content to save")

            # Optional basic HTML validation
            if validate_syntax:
                if not self._basic_html_validation():
                    logger.warning("HTML validation failed, but proceeding with save")

            # Write to file
            with open(self.html_path, 'w', encoding='utf-8') as f:
                f.write(self.content)

            logger.info(f"HTML saved successfully: {self.html_path}")
            return True

        except PermissionError:
            logger.error(f"Permission denied writing to: {self.html_path}")
            raise
        except Exception as e:
            logger.error(f"Failed to save HTML: {e}")
            raise

    def _basic_html_validation(self) -> bool:
        """Perform basic HTML syntax validation"""
        try:
            # Check for balanced brackets
            if self.content.count('<') != self.content.count('>'):
                logger.warning("Unbalanced HTML tags detected")
                return False

            # Check for basic structure
            required_tags = ['<html', '<head', '<body']
            for tag in required_tags:
                if tag not in self.content.lower():
                    logger.warning(f"Missing required HTML tag: {tag}")
                    return False

            return True

        except Exception as e:
            logger.error(f"HTML validation error: {e}")
            return False

    def rollback(self) -> bool:
        """Rollback to the last backup"""
        try:
            if not self.backup_path or not os.path.exists(self.backup_path):
                raise ValueError("No backup available for rollback")

            shutil.copy2(self.backup_path, self.html_path)
            logger.info(f"Rollback successful from: {self.backup_path}")
            return True

        except Exception as e:
            logger.error(f"Rollback failed: {e}")
            raise

def safe_profile_implementation(profile_code: str, profile_content: str,
                              insertion_marker: str = None) -> bool:
    """
    Safely implement a profile with full error handling and backup

    Args:
        profile_code: The profile code being implemented (e.g., 'SC-Architect')
        profile_content: The JavaScript content to insert
        insertion_marker: Custom insertion point (defaults to main marker)

    Returns:
        bool: True if successful, False otherwise
    """
    handler = STTIFileHandler()

    try:
        # Create backup before any changes
        handler.create_backup()

        # Load and validate content
        handler.load_html()

        # Find insertion point
        marker = insertion_marker or INSERTION_MARKERS['main']
        insertion_point = handler.validate_insertion_point(marker)

        # Insert new content
        handler.insert_content(insertion_point, profile_content)

        # Save with validation
        handler.save_html()

        logger.info(f"✅ Successfully implemented profile: {profile_code}")
        return True

    except Exception as e:
        logger.error(f"❌ Failed to implement profile {profile_code}: {e}")

        # Attempt rollback
        try:
            handler.rollback()
            logger.info("Rollback completed successfully")
        except Exception as rollback_error:
            logger.error(f"Rollback also failed: {rollback_error}")

        return False

def validate_profile_content(content: str, profile_code: str) -> Tuple[bool, str]:
    """
    Validate profile content before insertion

    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    try:
        # Check for required elements
        if not content.strip():
            return False, "Content is empty"

        # Check for profile code presence
        if profile_code not in content:
            return False, f"Profile code '{profile_code}' not found in content"

        # Check for balanced quotes and brackets
        single_quotes = content.count("'") - content.count("\\'")
        double_quotes = content.count('"') - content.count('\\"')

        if single_quotes % 2 != 0:
            return False, "Unbalanced single quotes detected"

        if double_quotes % 2 != 0:
            return False, "Unbalanced double quotes detected"

        # Check for required JavaScript structure
        required_elements = ['if (code ===', 'return;']
        for element in required_elements:
            if element not in content:
                return False, f"Missing required element: {element}"

        return True, "Content validation passed"

    except Exception as e:
        return False, f"Validation error: {e}"