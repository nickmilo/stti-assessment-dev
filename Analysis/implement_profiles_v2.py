#!/usr/bin/env python3
"""
STTI Profile Implementation v2.0
Modern, safe implementation using proper architecture

This script replaces the hardcoded, error-prone original scripts with:
- Proper configuration management
- Comprehensive error handling
- Automated backup system
- Validation and logging
- Reusable, maintainable code architecture
"""

import sys
import argparse
from pathlib import Path

# Add the Analysis directory to Python path for imports
sys.path.insert(0, str(Path(__file__).parent))

from profile_base import create_implementor, SCProfileImplementor
from utils import setup_logging
from config import validate_environment

def implement_sc_profiles():
    """Implement SC profiles using new architecture"""
    implementor = SCProfileImplementor()
    return implementor.implement_batch()

def implement_all_remaining_profiles():
    """Implement all remaining profile batches"""
    logger = setup_logging()

    try:
        # Validate environment first
        validate_environment()
        logger.info("Environment validation passed")

        # Track overall success
        overall_success = True

        # Implement SC profiles
        logger.info("Starting SC profile implementation...")
        sc_success = implement_sc_profiles()
        overall_success &= sc_success

        # TODO: Add other profile batches (SP, SI, PI) here as they are converted
        # sp_success = implement_sp_profiles()
        # si_success = implement_si_profiles()
        # pi_success = implement_pi_profiles()
        # overall_success &= sp_success & si_success & pi_success

        if overall_success:
            logger.info("🎉 ALL PROFILE IMPLEMENTATIONS COMPLETED SUCCESSFULLY")
        else:
            logger.error("❌ Some profile implementations failed")

        return overall_success

    except Exception as e:
        logger.error(f"Fatal error during implementation: {e}")
        return False

def main():
    """Main entry point with CLI support"""
    parser = argparse.ArgumentParser(
        description="STTI Profile Implementation v2.0 - Safe, modern profile implementation"
    )
    parser.add_argument(
        '--batch',
        choices=['SC', 'SP', 'SI', 'PI'],
        help="Implement specific profile batch"
    )
    parser.add_argument(
        '--profile',
        help="Implement single profile by code (e.g., SC-Architect)"
    )
    parser.add_argument(
        '--validate-only',
        action='store_true',
        help="Only validate environment, don't implement"
    )
    parser.add_argument(
        '--log-level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO',
        help="Set logging level"
    )

    args = parser.parse_args()

    # Setup logging
    logger = setup_logging(getattr(logging, args.log_level))

    try:
        # Validate environment
        validate_environment()
        logger.info("✅ Environment validation passed")

        if args.validate_only:
            logger.info("Validation-only mode - exiting")
            return True

        # Handle specific operations
        if args.profile:
            # Single profile implementation
            batch_code = args.profile.split('-')[0]
            implementor = create_implementor(batch_code)
            if implementor:
                success = implementor.implement_single_profile(args.profile)
                return success
            else:
                logger.error(f"Could not create implementor for profile: {args.profile}")
                return False

        elif args.batch:
            # Single batch implementation
            implementor = create_implementor(args.batch)
            if implementor:
                success = implementor.implement_batch()
                return success
            else:
                logger.error(f"Could not create implementor for batch: {args.batch}")
                return False

        else:
            # Default: implement all remaining profiles
            return implement_all_remaining_profiles()

    except Exception as e:
        logger.error(f"Fatal error: {e}")
        return False

if __name__ == "__main__":
    import logging
    success = main()
    sys.exit(0 if success else 1)