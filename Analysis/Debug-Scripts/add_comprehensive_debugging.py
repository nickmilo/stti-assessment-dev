#!/usr/bin/env python3
"""
Add comprehensive debugging to track where the secret code fails
"""

# Read the current file
with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index.html', 'r') as f:
    content = f.read()

# Add debugging at the very beginning of the script
debug_init = """
        // === COMPREHENSIVE DEBUG MODE ===
        window.DEBUG_MODE = true;
        console.log('🟢 DEBUG MODE ACTIVE - Script starting');
        
        // Override console.log to also show alerts in debug mode
        const originalLog = console.log;
        window.debugLog = function(...args) {
            originalLog('🔍', ...args);
            if (window.DEBUG_MODE) {
                // Also track in a debug array
                if (!window.debugMessages) window.debugMessages = [];
                window.debugMessages.push(args.join(' '));
            }
        };
"""

# Find where to insert (right after the script tag)
script_start = content.find('<script>') + len('<script>')
content = content[:script_start] + debug_init + content[script_start:]

# Replace specific console.log calls with debugLog
replacements = [
    ("console.log('Z key pressed - showing IS-Architect results');", 
     "debugLog('Z key pressed - showing IS-Architect results');"),
    ("console.log('showSpecificProfile called with:', profile);",
     "debugLog('showSpecificProfile called with:', profile);")
]

for old, new in replacements:
    content = content.replace(old, new)

# Add more debugging to showTestResults
content = content.replace(
    "function showTestResults(targetProfile) {",
    """function showTestResults(targetProfile) {
            debugLog('🎯 showTestResults called with:', targetProfile);
            try {"""
)

# Add catch block
content = content.replace(
    "// Directly show the specific profile\n            showSpecificProfile(mockProfile);",
    """// Directly show the specific profile
            debugLog('📊 About to call showSpecificProfile with:', mockProfile);
            showSpecificProfile(mockProfile);
            } catch (error) {
                debugLog('❌ ERROR in showTestResults:', error.message);
                console.error('Full error:', error);
                alert('Error: ' + error.message);
            }"""
)

# Add debug button
debug_button = """
    <div style="position: fixed; bottom: 10px; right: 10px; z-index: 9999; background: #333; color: white; padding: 10px; border-radius: 5px;">
        <button onclick="window.DEBUG_MODE = !window.DEBUG_MODE; this.textContent = window.DEBUG_MODE ? 'Debug ON' : 'Debug OFF'">Debug ON</button>
        <button onclick="if(window.debugMessages) alert(window.debugMessages.join('\\n')); else alert('No debug messages');">Show Log</button>
        <button onclick="showTestResults('IS-Architect')">Test IS-Arch</button>
    </div>
"""

# Insert debug button before </body>
body_end = content.rfind('</body>')
content = content[:body_end] + debug_button + content[body_end:]

# Save as a new debug file
with open('/Users/nick/Dropbox/+/AI/STTI Assessment/index-debug.html', 'w') as f:
    f.write(content)

print("Created index-debug.html with comprehensive debugging")
print("\nKey additions:")
print("- Debug mode toggle button (bottom right)")
print("- 'Show Log' button to see all debug messages")
print("- 'Test IS-Arch' button to directly trigger the secret code")
print("- Extensive logging throughout the secret code path")
print("\nOpen index-debug.html in your browser to test!")