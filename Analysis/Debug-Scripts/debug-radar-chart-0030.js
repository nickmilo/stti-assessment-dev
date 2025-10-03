// Debug script for radar chart 0030 issue
// Profile 0030: I:15 S:26 P:8 C:32 A:10 G:32

const scores = { I: 15, S: 26, P: 8, C: 32, A: 10, G: 32 };

// Config from main.js
const CENTER_X = 250;
const CENTER_Y = 250;
const MAX_RADIUS = 180;
const GRID_LEVELS = 5;
const SCALE_MIN_PERCENT = 0.4;
const SCALE_MAX_PERCENT = 1.0;

// Calculate grid circle radii
console.log("=== GRID CIRCLES ===");
for (let i = 1; i <= GRID_LEVELS; i++) {
    const radius = (i / GRID_LEVELS) * MAX_RADIUS;
    console.log(`Circle ${i}: radius = ${radius}px (at ${(i/GRID_LEVELS)*100}% of max)`);
}

// 6-axis configuration
const axes6 = [
    { key: 'A', label: 'Architect', angle: -90 },
    { key: 'P', label: 'Producer', angle: -30 },
    { key: 'C', label: 'Creative', angle: 30 },
    { key: 'G', label: 'Gardener', angle: 90 },
    { key: 'I', label: 'Inner Guide', angle: 150 },
    { key: 'S', label: 'Synthesizer', angle: 210 }
];

// Calculate polygon points for 6-axis chart
const allScores6 = axes6.map(axis => scores[axis.key]);
const maxScore6 = Math.max(...allScores6);
const minScore6 = Math.min(...allScores6);

console.log("\n=== 6-AXIS CHART SCORES ===");
console.log(`Min score: ${minScore6} (${axes6.find(a => scores[a.key] === minScore6).key})`);
console.log(`Max score: ${maxScore6} (${axes6.find(a => scores[a.key] === maxScore6).key})`);

console.log("\n=== 6-AXIS POINT CALCULATIONS ===");
axes6.forEach(axis => {
    const score = scores[axis.key];
    const normalizedScore = (score - minScore6) / (maxScore6 - minScore6);
    const paddedScore = normalizedScore * (SCALE_MAX_PERCENT - SCALE_MIN_PERCENT) + SCALE_MIN_PERCENT;
    const radius = paddedScore * MAX_RADIUS;
    const angleRad = (axis.angle * Math.PI) / 180;
    const x = CENTER_X + radius * Math.cos(angleRad);
    const y = CENTER_Y + radius * Math.sin(angleRad);

    console.log(`${axis.key} (${axis.label}): score=${score}, norm=${normalizedScore.toFixed(3)}, padded=${paddedScore.toFixed(3)}, radius=${radius.toFixed(1)}px`);
    console.log(`  → Position: (${x.toFixed(1)}, ${y.toFixed(1)})`);
    console.log(`  → Should be on circle: ${Math.round((paddedScore * GRID_LEVELS))}`);
});

// 4-axis configuration
const axes4 = [
    { key: 'S', label: 'Synthesizer', angle: -135 },
    { key: 'P', label: 'Producer', angle: -45 },
    { key: 'C', label: 'Creative', angle: 45 },
    { key: 'I', label: 'Inner Guide', angle: 135 }
];

// Calculate polygon points for 4-axis chart
const allScores4 = axes4.map(axis => scores[axis.key]);
const maxScore4 = Math.max(...allScores4);
const minScore4 = Math.min(...allScores4);

console.log("\n=== 4-AXIS CHART SCORES ===");
console.log(`Min score: ${minScore4} (${axes4.find(a => scores[a.key] === minScore4).key})`);
console.log(`Max score: ${maxScore4} (${axes4.find(a => scores[a.key] === maxScore4).key})`);

console.log("\n=== 4-AXIS POINT CALCULATIONS ===");
axes4.forEach(axis => {
    const score = scores[axis.key];
    const normalizedScore = (score - minScore4) / (maxScore4 - minScore4);
    const paddedScore = normalizedScore * (SCALE_MAX_PERCENT - SCALE_MIN_PERCENT) + SCALE_MIN_PERCENT;
    const radius = paddedScore * MAX_RADIUS;
    const angleRad = (axis.angle * Math.PI) / 180;
    const x = CENTER_X + radius * Math.cos(angleRad);
    const y = CENTER_Y + radius * Math.sin(angleRad);

    console.log(`${axis.key} (${axis.label}): score=${score}, norm=${normalizedScore.toFixed(3)}, padded=${paddedScore.toFixed(3)}, radius=${radius.toFixed(1)}px`);
    console.log(`  → Position: (${x.toFixed(1)}, ${y.toFixed(1)})`);
    console.log(`  → Should be on circle: ${Math.round((paddedScore * GRID_LEVELS))}`);
});

console.log("\n=== LABEL POSITIONS (4-axis chart only) ===");
console.log(`Reflection label: x=15 (15px from left edge, viewBox is 0-500)`);
console.log(`Expression label: x=485 (15px from right edge, viewBox is 0-500)`);
console.log(`Top-down label: y=${CENTER_Y - MAX_RADIUS - 15} (${MAX_RADIUS + 15}px above center)`);
console.log(`Bottom-up label: y=${CENTER_Y + MAX_RADIUS + 25} (${MAX_RADIUS + 25}px below center)`);
