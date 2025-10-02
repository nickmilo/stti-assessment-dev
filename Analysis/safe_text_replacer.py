#!/usr/bin/env python3
"""
Safe Text Replacement Utility
Demonstrates the improved, safer way to make changes to the STTI assessment

Example: Replace "Southerner" with "Southern" safely
"""

import sys
import argparse
from pathlib import Path

# Add the Analysis directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from utils import STTIFileHandler, setup_logging
from config import validate_environment

class SafeTextReplacer:
    """Safe text replacement with backup, validation, and rollback"""

    def __init__(self):
        self.logger = setup_logging()
        self.handler = STTIFileHandler()

    def replace_text(self, old_text: str, new_text: str, preview_only: bool = False) -> bool:
        """
        Safely replace text in HTML file with full safety features

        Args:
            old_text: Text to find and replace
            new_text: Text to replace with
            preview_only: If True, only show what would change without making changes

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Step 1: Validate environment
            self.logger.info("🔍 Validating environment...")
            validate_environment()

            # Step 2: Create backup (only if not preview)
            if not preview_only:
                self.logger.info("💾 Creating backup...")
                backup_path = self.handler.create_backup()
                self.logger.info(f"✅ Backup created: {backup_path}")

            # Step 3: Load and analyze content
            self.logger.info("📖 Loading HTML content...")
            self.handler.load_html()

            # Step 4: Find all occurrences
            content = self.handler.content
            occurrences = content.count(old_text)

            if occurrences == 0:
                self.logger.warning(f"⚠️  No occurrences of '{old_text}' found")
                return True  # Not an error, just nothing to do

            self.logger.info(f"🔎 Found {occurrences} occurrences of '{old_text}'")

            # Step 5: Show preview of changes
            self._show_preview(content, old_text, new_text)

            if preview_only:
                self.logger.info("👁️  Preview mode - no changes made")
                return True

            # Step 6: Make the replacement
            self.logger.info("✏️  Making replacements...")
            new_content = content.replace(old_text, new_text)

            # Step 7: Validate the changes
            if not self._validate_changes(content, new_content, old_text, new_text):
                self.logger.error("❌ Change validation failed")
                return False

            # Step 8: Update content and save
            self.handler.content = new_content
            self.handler.save_html(validate_syntax=True)

            self.logger.info(f"✅ Successfully replaced {occurrences} occurrences")
            self.logger.info(f"✅ Changed '{old_text}' → '{new_text}'")

            return True

        except Exception as e:
            self.logger.error(f"❌ Text replacement failed: {e}")

            # Attempt rollback if we made changes
            if not preview_only and hasattr(self.handler, 'backup_path'):
                try:
                    self.handler.rollback()
                    self.logger.info("🔄 Rollback completed successfully")
                except Exception as rollback_error:
                    self.logger.error(f"💥 Rollback also failed: {rollback_error}")

            return False

    def _show_preview(self, content: str, old_text: str, new_text: str):
        """Show preview of what will change"""
        lines = content.split('\n')
        changes_found = 0

        self.logger.info("👀 Preview of changes:")
        self.logger.info("-" * 50)

        for i, line in enumerate(lines, 1):
            if old_text in line:
                changes_found += 1
                if changes_found <= 5:  # Show first 5 changes
                    preview_line = line.replace(old_text, f"→{new_text}←")
                    self.logger.info(f"Line {i}: {preview_line.strip()}")
                elif changes_found == 6:
                    self.logger.info("... (additional changes not shown)")

        self.logger.info("-" * 50)

    def _validate_changes(self, old_content: str, new_content: str, old_text: str, new_text: str) -> bool:
        """Validate that changes were made correctly"""
        # Check that old text is gone
        remaining_old = new_content.count(old_text)
        if remaining_old > 0:
            self.logger.error(f"❌ Still found {remaining_old} occurrences of '{old_text}'")
            return False

        # Check that new text count is correct (accounting for overlaps)
        original_new_count = old_content.count(new_text)
        final_new_count = new_content.count(new_text)
        replacements_made = old_content.count(old_text)

        # If new_text is substring of old_text, count stays same
        # If old_text is substring of new_text, count increases
        # Otherwise, count increases by replacements_made
        if new_text in old_text:
            expected_final_count = original_new_count  # Southerner->Southern case
        elif old_text in new_text:
            expected_final_count = original_new_count + replacements_made
        else:
            expected_final_count = original_new_count + replacements_made

        if final_new_count != expected_final_count:
            self.logger.error(f"❌ Expected {expected_final_count} total '{new_text}' but found {final_new_count}")
            return False

        self.logger.info(f"✅ Validation passed: {replacements_made} replacements made, {final_new_count} total '{new_text}'")

        # Check that content length changed appropriately
        expected_length_change = (len(new_text) - len(old_text)) * replacements_made
        actual_length_change = len(new_content) - len(old_content)

        if actual_length_change != expected_length_change:
            self.logger.error(f"❌ Content length change mismatch")
            return False

        return True

def main():
    """Main entry point with CLI"""
    parser = argparse.ArgumentParser(
        description="Safe Text Replacement - Replace text in STTI assessment safely"
    )
    parser.add_argument('old_text', help='Text to find and replace')
    parser.add_argument('new_text', help='Text to replace with')
    parser.add_argument('--preview', action='store_true',
                       help='Preview changes without making them')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO', help='Set logging level')

    args = parser.parse_args()

    # Create replacer and run
    replacer = SafeTextReplacer()
    success = replacer.replace_text(args.old_text, args.new_text, args.preview)

    if success:
        if args.preview:
            print("\n✅ Preview completed successfully")
        else:
            print(f"\n✅ Successfully replaced '{args.old_text}' with '{args.new_text}'")
            print("💡 Ready to commit and push changes!")
    else:
        print(f"\n❌ Failed to replace '{args.old_text}' with '{args.new_text}'")

    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()