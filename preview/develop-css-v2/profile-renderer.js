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
     * Load profile configuration from inline data or fallback to fetch
     */
    async loadProfiles() {
        try {
            // Check if inline data is available (loaded from profiles-data.js)
            if (window.STTI_PROFILES && typeof window.STTI_PROFILES === 'object') {
                this.profiles = window.STTI_PROFILES;
                this.isReady = true;
                console.log('✅ Profile configuration loaded from inline data:', Object.keys(this.profiles).length, 'profiles');
                return;
            }

            // Fallback to fetch if inline data is not available (backward compatibility)
            console.log('⚠️ Inline profile data not found, attempting to fetch profiles.json...');
            const response = await fetch('profiles.json');
            if (!response.ok) {
                throw new Error(`Failed to load profiles: ${response.status}`);
            }
            this.profiles = await response.json();
            this.isReady = true;
            console.log('✅ Profile configuration loaded from fetch:', Object.keys(this.profiles).length, 'profiles');
        } catch (error) {
            console.error('❌ CRITICAL ERROR: Failed to load profile configuration:', error);
            this.isReady = false;
            // DON'T show error on page load - wait until results are needed
            // Error will be shown in waitForProfiles() if still failing
        }
    }

    /**
     * Wait for profiles to load with retry logic
     * Used by showResults() to ensure profiles are ready before rendering
     */
    async waitForProfiles(maxRetries = 3, timeoutMs = 5000) {
        const startTime = Date.now();
        let attempts = 0;

        while (!this.isReady && attempts < maxRetries) {
            attempts++;

            if (attempts > 1) {
                console.log(`🔄 Retrying profile load (attempt ${attempts}/${maxRetries})...`);
            }

            await this.loadProfiles();

            // Poll with exponential backoff
            let pollInterval = 100;
            while (!this.isReady && (Date.now() - startTime) < timeoutMs) {
                await new Promise(resolve => setTimeout(resolve, pollInterval));
                pollInterval = Math.min(pollInterval * 1.5, 1000);
            }

            if (this.isReady) {
                return true;
            }
        }

        if (!this.isReady) {
            throw new Error(`Failed to load profiles after ${attempts} attempts`);
        }

        return this.isReady;
    }

    /**
     * Show critical error to user when profiles fail to load
     */
    showCriticalError(error) {
        const errorHTML = `
            <div style="padding: 40px; text-align: center; color: #e53e3e; max-width: 600px; margin: 0 auto;">
                <h2 style="color: #c53030;">⚠️ Configuration Error</h2>
                <p style="font-size: 18px; margin: 20px 0;">The assessment profiles failed to load. Please refresh the page to try again.</p>
                <p style="font-size: 14px; color: #666; margin-top: 20px;">
                    Technical error: ${error.message}
                </p>
                <button onclick="window.location.reload()"
                        style="margin-top: 30px; padding: 12px 24px; font-size: 16px;
                               background: #3182ce; color: white; border: none;
                               border-radius: 6px; cursor: pointer;">
                    Refresh Page
                </button>
            </div>
        `;

        // Show error in results screen
        const resultsScreen = document.getElementById('resultsScreen');
        if (resultsScreen) {
            resultsScreen.innerHTML = errorHTML;
            resultsScreen.classList.add('active');
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

}

// Global instance for backward compatibility
window.profileRenderer = new ProfileRenderer();