// Test ProfileRenderer in browser console
// Copy-paste this into browser console after loading index.html

console.log("=== PROFILE RENDERER DIAGNOSTIC ===");

// Check if ProfileRenderer exists
console.log("1. ProfileRenderer loaded:", !!window.profileRenderer);

// Check if profiles.json is loaded
if (window.profileRenderer) {
    console.log("2. Profiles loaded:", !!window.profileRenderer.profiles);
    console.log("3. Number of profiles:", Object.keys(window.profileRenderer.profiles).length);

    // Test specific profile
    const testCode = 'IP-Architect';
    console.log(`\n4. Testing profile: ${testCode}`);
    console.log("   - Has profile:", window.profileRenderer.hasProfile(testCode));

    if (window.profileRenderer.hasProfile(testCode)) {
        const profile = window.profileRenderer.profiles[testCode];
        console.log("   - Profile data:", profile);
        console.log("   - Has archetypeDescription:", !!profile.archetypeDescription);
        console.log("   - Has orientationDescription:", !!profile.orientationDescription);
        console.log("   - Has tendencyDescription:", !!profile.tendencyDescription);
        console.log("   - Has overwhelmed:", !!profile.overwhelmed);
        console.log("   - Has stuckUnstuck:", !!profile.stuckUnstuck);
        console.log("   - Has prompts:", !!profile.prompts);

        console.log("\n5. Testing renderProfile()...");
        const success = window.profileRenderer.renderProfile(testCode);
        console.log("   - Render success:", success);
    }
} else {
    console.error("❌ ProfileRenderer not found!");
}

console.log("\n6. Checking DOM elements:");
console.log("   - archetypeDescription:", !!document.getElementById('archetypeDescription'));
console.log("   - westernerDescription:", !!document.getElementById('westernerDescription'));
console.log("   - tendencyDescription:", !!document.getElementById('tendencyDescription'));
console.log("   - overwhelmedContent:", !!document.getElementById('overwhelmedContent'));
console.log("   - stuckUnstuckContent:", !!document.getElementById('stuckUnstuckContent'));
console.log("   - promptsContent:", !!document.getElementById('promptsContent'));
