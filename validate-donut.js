/**
 * Validation script to test donut chart rendering with secret codes
 * Run this in browser console after loading index.html
 */

console.log('=== DONUT CHART VALIDATION ===');

// Test secret code 0025 (Extreme Architect: A:32 G:10)
console.log('\n1. Testing secret code 0025 (Extreme Architect)...');
console.log('Expected: A=32, G=10 → 76.2% Architect, 23.8% Gardener');

// Test secret code 0030 (Extreme Gardener: A:10 G:32)
console.log('\n2. Testing secret code 0030 (Extreme Gardener)...');
console.log('Expected: A=10, G=32 → 23.8% Architect, 76.2% Gardener');

// Test secret code 0027 (Perfect balance: A:20 G:20)
console.log('\n3. Testing secret code 0027 (Perfect Balance)...');
console.log('Expected: A=20, G=20 → 50.0% Architect, 50.0% Gardener');

console.log('\n=== VALIDATION STEPS ===');
console.log('1. Load index.html');
console.log('2. Type secret code (e.g., 0025)');
console.log('3. Check if donut chart appears in "Architect vs Gardener Balance" section');
console.log('4. Verify:');
console.log('   - Top half is BLUE (Architect)');
console.log('   - Bottom half is GREEN (Gardener)');
console.log('   - White circle in center (donut hole)');
console.log('   - Percentages displayed correctly');
console.log('\n=== DEBUG FUNCTION ===');
console.log('Run: testDonutDirectly({ A: 32, G: 10 })');

// Direct test function
window.testDonutDirectly = function(scores) {
    console.log('🧪 Direct donut test with scores:', scores);

    const svg = document.getElementById('architectGardenerDonut');
    if (!svg) {
        console.error('❌ SVG element not found!');
        return;
    }

    console.log('✓ SVG element found');

    // Call the render function directly if it exists
    if (typeof renderArchitectGardenerDonut === 'function') {
        renderArchitectGardenerDonut(scores);
        console.log('✓ Render function called');
    } else {
        console.error('❌ renderArchitectGardenerDonut function not found!');
        console.log('Available functions:', Object.keys(window).filter(k => k.includes('render')));
    }
};

console.log('\nValidation script loaded. Use testDonutDirectly({ A: 32, G: 10 }) to test.');
