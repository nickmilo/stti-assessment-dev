#!/bin/bash
# Start local development server for STTI Assessment
# This mimics how GitHub Pages will serve the site

echo "🚀 Starting STTI Assessment local server..."
echo ""
echo "Server will start at: http://localhost:8000/"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

cd "$(dirname "$0")"
python3 -m http.server 8000
