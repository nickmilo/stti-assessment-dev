#!/usr/bin/env python3
"""
Create a minimal test HTML to verify basic functionality
"""

minimal_html = """<!DOCTYPE html>
<html>
<head>
    <title>STTI Secret Code Test</title>
</head>
<body>
    <h1>STTI Assessment - Secret Code Test</h1>
    <p>Press Z to test if secret codes work</p>
    <div id="result"></div>
    
    <script>
    console.log('Test page loaded');
    
    // Simple Z key test
    document.addEventListener('keydown', function(e) {
        console.log('Key pressed:', e.key);
        if (e.key === 'z' || e.key === 'Z') {
            document.getElementById('result').innerHTML = '<h2>Z key works! Secret code triggered.</h2>';
            console.log('Z key detected successfully');
        }
    });
    </script>
</body>
</html>
"""

with open('/Users/nick/Dropbox/+/AI/stti-assessment/test-secret-codes.html', 'w') as f:
    f.write(minimal_html)

print("Created test-secret-codes.html")
print("\nNow let's extract the actual showTestResults function to see what might be wrong...")

# Extract the showTestResults function
with open('/Users/nick/Dropbox/+/AI/stti-assessment/index.html', 'r') as f:
    lines = f.readlines()

in_function = False
func_lines = []
brace_count = 0

for i, line in enumerate(lines):
    if 'function showTestResults' in line:
        in_function = True
        
    if in_function:
        func_lines.append(f"{i+1}: {line.rstrip()}")
        if '{' in line:
            brace_count += line.count('{')
        if '}' in line:
            brace_count -= line.count('}')
        
        if brace_count == 0 and len(func_lines) > 1:
            break

print("\n=== showTestResults Function ===")
for line in func_lines[:20]:  # First 20 lines
    print(line)
    
print(f"\n... ({len(func_lines)} total lines in function)")