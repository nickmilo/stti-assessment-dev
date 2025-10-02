#!/usr/bin/env python3
"""
STTI Profile Implementation Base Classes
Shared foundation for all profile implementations with proper abstraction
"""

import logging
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

from utils import safe_profile_implementation, validate_profile_content

logger = logging.getLogger(__name__)

@dataclass
class ProfileData:
    """Data class for profile information"""
    code: str
    archetype_pair: str
    direction: str
    tendency: str
    overwhelmed_title: str
    overwhelmed_content: str
    stuck_title: str
    stuck_content: str
    prompts_title: str
    prompts_content: str

class ProfileImplementor(ABC):
    """Abstract base class for profile implementations"""

    def __init__(self, batch_name: str, description: str):
        self.batch_name = batch_name
        self.description = description
        self.logger = logging.getLogger(f"{__name__}.{self.__class__.__name__}")

    @abstractmethod
    def get_profiles(self) -> List[ProfileData]:
        """Return list of profiles to implement"""
        pass

    def generate_javascript_content(self, profile: ProfileData) -> str:
        """Generate JavaScript content for a profile"""
        template = '''
            if (code === '{code}') {{
                // Set overwhelmed content for {code}
                const overwhelmedTitle = document.querySelector('#overwhelmedSection .section-title');
                const overwhelmedContent = document.querySelector('#overwhelmedSection .section-content');
                if (overwhelmedTitle && overwhelmedContent) {{
                    overwhelmedTitle.textContent = '{overwhelmed_title}';
                    overwhelmedContent.innerHTML = '{overwhelmed_content}';
                }}

                // Set stuck/unstuck content for {code}
                const stuckTitle = document.querySelector('#stuckUnstuckSection .section-title');
                const stuckContent = document.querySelector('#stuckUnstuckSection .section-content');
                if (stuckTitle && stuckContent) {{
                    stuckTitle.textContent = '{stuck_title}';
                    stuckContent.innerHTML = '{stuck_content}';
                }}

                // Set prompts content for {code}
                const promptsTitle = document.querySelector('#promptsSection .section-title');
                const promptsContent = document.querySelector('#promptsSection .section-content');
                if (promptsTitle && promptsContent) {{
                    promptsTitle.textContent = '{prompts_title}';
                    promptsContent.innerHTML = '{prompts_content}';
                }}
                return; // Exit early, don\\'t use generic logic
            }}
            '''

        # Escape single quotes in content for JavaScript
        def escape_content(text: str) -> str:
            return text.replace("'", "\\'").replace('\n', ' ')

        return template.format(
            code=profile.code,
            overwhelmed_title=escape_content(profile.overwhelmed_title),
            overwhelmed_content=escape_content(profile.overwhelmed_content),
            stuck_title=escape_content(profile.stuck_title),
            stuck_content=escape_content(profile.stuck_content),
            prompts_title=escape_content(profile.prompts_title),
            prompts_content=escape_content(profile.prompts_content)
        )

    def implement_batch(self) -> bool:
        """Implement all profiles in this batch"""
        self.logger.info(f"=== IMPLEMENTING {self.batch_name.upper()} ===")
        self.logger.info(f"{self.description}")

        profiles = self.get_profiles()
        success_count = 0
        total_count = len(profiles)

        # Generate combined content for all profiles in batch
        combined_content = ""
        for profile in profiles:
            profile_content = self.generate_javascript_content(profile)

            # Validate content before adding
            is_valid, error_msg = validate_profile_content(profile_content, profile.code)
            if not is_valid:
                self.logger.error(f"❌ Profile {profile.code} validation failed: {error_msg}")
                continue

            combined_content += profile_content

        if not combined_content:
            self.logger.error("❌ No valid profiles to implement")
            return False

        # Implement all profiles in one operation
        success = safe_profile_implementation(
            profile_code=f"{self.batch_name}_batch",
            profile_content=combined_content
        )

        if success:
            self.logger.info(f"✅ {self.batch_name} batch implemented successfully ({total_count} profiles)")
        else:
            self.logger.error(f"❌ {self.batch_name} batch implementation failed")

        return success

    def implement_single_profile(self, profile_code: str) -> bool:
        """Implement a single profile by code"""
        profiles = self.get_profiles()
        target_profile = None

        for profile in profiles:
            if profile.code == profile_code:
                target_profile = profile
                break

        if not target_profile:
            self.logger.error(f"Profile {profile_code} not found in {self.batch_name}")
            return False

        profile_content = self.generate_javascript_content(target_profile)

        # Validate content
        is_valid, error_msg = validate_profile_content(profile_content, profile_code)
        if not is_valid:
            self.logger.error(f"Profile {profile_code} validation failed: {error_msg}")
            return False

        return safe_profile_implementation(profile_code, profile_content)

class SCProfileImplementor(ProfileImplementor):
    """Implements SC (Synthesizer + Creative = Translator) profiles"""

    def __init__(self):
        super().__init__("SC", "SC = Synthesizer + Creative = Diagonal/Translator")

    def get_profiles(self) -> List[ProfileData]:
        return [
            ProfileData(
                code="SC-Architect",
                archetype_pair="Synthesizer + Creative",
                direction="Translator",
                tendency="Architect",
                overwhelmed_title="When Translators feel overwhelmed…",
                overwhelmed_content="They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.",
                stuck_title="Getting stuck and unstuck as an SC-Architect",
                stuck_content="When you combine your Translator archetypes with an Architect tendency, it's most difficult to access your Inner Guide archetype—yet that's exactly what you most need. Since your tendency is to architect, the easiest way to bridge perspectives with meaning is by tapping into your Synthesizer archetype, which aligns with your structured approach to making sense.",
                prompts_title="Prompts to bridge perspectives with meaning as an SC-Architect",
                prompts_content="What deeper meaning connects the perspectives you're translating? How can your Synthesizer help you structure these connections systematically? Once your Synthesizer is activated, you'll likely find it becomes easier to move into your Inner Guide archetype, allowing you to access the intrinsic meaning behind your translations."
            ),
            ProfileData(
                code="SC-Gardener",
                archetype_pair="Synthesizer + Creative",
                direction="Translator",
                tendency="Gardener",
                overwhelmed_title="When Translators feel overwhelmed…",
                overwhelmed_content="They may try to bridge too many perspectives at once, when what they need is to focus on one key translation or synthesis at a time, allowing clarity to emerge before expanding.",
                stuck_title="Getting stuck and unstuck as an SC-Gardener",
                stuck_content="When you combine your Translator archetypes with a Gardener tendency, it's most difficult to access your Producer archetype—yet that's exactly what you most need. Since your tendency is to garden, the easiest way to bridge perspectives with action is by tapping into your Creative archetype, which aligns with your flexible approach to innovative expression.",
                prompts_title="Prompts to bridge perspectives with action as an SC-Gardener",
                prompts_content="What creative expressions could emerge from the perspectives you're bridging? How can your Creative help you manifest your translations in innovative ways? Once your Creative is activated, you'll likely find it becomes easier to move into your Producer archetype, allowing you to take systematic action on your synthesized insights."
            )
        ]

def create_implementor(batch_code: str) -> Optional[ProfileImplementor]:
    """Factory function to create appropriate implementor"""
    implementors = {
        'SC': SCProfileImplementor,
        # Add other implementors as needed
    }

    implementor_class = implementors.get(batch_code.upper())
    if implementor_class:
        return implementor_class()
    else:
        logger.error(f"Unknown batch code: {batch_code}")
        return None