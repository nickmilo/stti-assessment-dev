/**
 * ProfileRenderer - Modern, data-driven profile rendering system
 * Replaces 24+ hardcoded profile blocks with clean, maintainable code
 */
class ProfileRenderer {
    constructor() {
        this.profiles = null;
        this.domCache = new Map();
        this.isReady = false;
        this.loadProfiles();
    }

    /**
     * Load profile configuration from JSON
     */
    async loadProfiles() {
        try {
            const response = await fetch('profiles.json');
            if (!response.ok) {
                throw new Error(`Failed to load profiles: ${response.status}`);
            }
            this.profiles = await response.json();
            this.isReady = true;
            console.log('✅ Profile configuration loaded:', Object.keys(this.profiles).length, 'profiles');
        } catch (error) {
            console.error('❌ Failed to load profile configuration:', error);
            // Fallback to hardcoded profiles if JSON fails
            this.profiles = this.getFallbackProfiles();
            this.isReady = true;
        }
    }

    /**
     * Cache DOM elements for performance
     */
    getElement(selector) {
        if (!this.domCache.has(selector)) {
            this.domCache.set(selector, document.querySelector(selector));
        }
        return this.domCache.get(selector);
    }

    /**
     * Render a specific profile by code
     */
    renderProfile(profileCode) {
        if (!this.profiles || !this.profiles[profileCode]) {
            console.warn(`⚠️ Profile not found: ${profileCode}`);
            return false;
        }

        const profile = this.profiles[profileCode];

        try {
            // Render archetype description (new)
            this.renderDescriptionSection('archetypeDescription', profile.archetypeDescription);

            // Render orientation description (new)
            this.renderDescriptionSection('orientationDescription', profile.orientationDescription);

            // Render tendency description (new)
            this.renderDescriptionSection('tendencyDescription', profile.tendencyDescription);

            // Render overwhelmed section
            this.renderSection('overwhelmed', profile.overwhelmed);

            // Render stuck/unstuck section
            this.renderSection('stuckUnstuck', profile.stuckUnstuck);

            // Render prompts section
            this.renderSection('prompts', profile.prompts);

            // Render archetypes synergy section
            this.renderSection('archetypesSynergy', profile.archetypesSynergy);

            console.log(`✅ Rendered profile: ${profileCode}`);
            return true;

        } catch (error) {
            console.error(`❌ Failed to render profile ${profileCode}:`, error);
            return false;
        }
    }

    /**
     * Render description sections (archetype, orientation, tendency)
     * These sections only have content, no title
     */
    renderDescriptionSection(sectionType, sectionData) {
        if (!sectionData) return;

        let elementId;
        switch (sectionType) {
            case 'archetypeDescription':
                elementId = 'archetypeDescription';
                break;
            case 'orientationDescription':
                elementId = 'westernerDescription';  // HTML uses 'westernerDescription' ID
                break;
            case 'tendencyDescription':
                elementId = 'tendencyDescription';
                break;
            default:
                console.warn(`Unknown description section type: ${sectionType}`);
                return;
        }

        // Get cached DOM element
        const element = this.getElement(`#${elementId}`);

        if (element) {
            element.innerHTML = sectionData.content;
        } else {
            console.warn(`Missing DOM element for: ${elementId}`);
        }
    }

    /**
     * Render collapsible sections (overwhelmed, stuckUnstuck, prompts, archetypesSynergy)
     * These sections have both title and content
     */
    renderSection(sectionType, sectionData) {
        if (!sectionData) return;

        let sectionId;
        switch (sectionType) {
            case 'overwhelmed':
                sectionId = 'overwhelmedSection';
                break;
            case 'stuckUnstuck':
                sectionId = 'stuckUnstuckSection';
                break;
            case 'prompts':
                sectionId = 'promptsSection';
                break;
            case 'archetypesSynergy':
                sectionId = 'archetypesSynergySection';
                break;
            default:
                console.warn(`Unknown section type: ${sectionType}`);
                return;
        }

        // Get cached DOM elements
        const titleElement = this.getElement(`#${sectionId} .section-title`);
        const contentElement = this.getElement(`#${sectionId} .section-content`);

        if (titleElement && contentElement) {
            titleElement.textContent = sectionData.title;
            contentElement.innerHTML = sectionData.content;
        } else {
            console.warn(`Missing DOM elements for section: ${sectionId}`);
        }
    }

    /**
     * Check if profile exists
     */
    hasProfile(profileCode) {
        return this.profiles && this.profiles[profileCode];
    }

    /**
     * Get all available profile codes
     */
    getAvailableProfiles() {
        return this.profiles ? Object.keys(this.profiles) : [];
    }

    /**
     * Fallback profiles in case JSON loading fails
     */
    getFallbackProfiles() {
        return {
            "IS-Architect": {
                "overwhelmed": {
                    "title": "When Westerners feel overwhelmed…",
                    "content": "They usually double-down on their strengths to analyze, when what they likely need more is to move from reflection to expression."
                },
                "stuckUnstuck": {
                    "title": "Getting stuck and unstuck as an IS-Architect",
                    "content": "When you combine your Westerner archetypes with an Architect tendency, it's most difficult to access your Creative archetype—yet that's exactly what you most need."
                },
                "prompts": {
                    "title": "Prompts to go from West to East as an IS-Architect",
                    "content": "How can you tie your current activity or problem to a concrete outcome or goal?"
                }
            }
            // Additional fallback profiles would go here
        };
    }
}

// Global instance for backward compatibility
window.profileRenderer = new ProfileRenderer();