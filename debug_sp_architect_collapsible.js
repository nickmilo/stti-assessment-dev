// Debug script to test SP-Architect collapsible sections
// Following SOP Tenet #2: Use code to understand the issue completely

console.log('=== DEBUGGING SP-ARCHITECT COLLAPSIBLE SECTIONS ===');

// Test if setCollapsibleSections exists
if (typeof setCollapsibleSections === 'function') {
    console.log('✅ setCollapsibleSections function exists');
    
    // Test calling it directly with SP-Architect
    console.log('🔄 Calling setCollapsibleSections("SP-Architect")...');
    try {
        setCollapsibleSections('SP-Architect');
        console.log('✅ Function called successfully');
        
        // Check if sections are now visible
        const sections = ['overwhelmedSection', 'stuckUnstuckSection', 'promptsSection'];
        sections.forEach(sectionId => {
            const section = document.getElementById(sectionId);
            if (section) {
                const display = window.getComputedStyle(section).display;
                console.log(`📊 ${sectionId} display: ${display}`);
                
                // Check content
                const title = section.querySelector('.section-title');
                const content = section.querySelector('.section-content');
                if (title && content) {
                    console.log(`📝 ${sectionId} title: "${title.textContent}"`);
                    console.log(`📝 ${sectionId} content: "${content.innerHTML.substring(0, 100)}..."`);
                } else {
                    console.log(`❌ ${sectionId} title or content not found`);
                }
            } else {
                console.log(`❌ ${sectionId} not found in DOM`);
            }
        });
        
    } catch (error) {
        console.error('❌ Error calling setCollapsibleSections:', error);
    }
} else {
    console.log('❌ setCollapsibleSections function not found');
}

// Check if the function is being called in showResults
console.log('\n🔍 Checking showResults function...');
if (typeof showResults === 'function') {
    console.log('✅ showResults function exists');
} else {
    console.log('❌ showResults function not found');
}