#!/bin/bash
# Install all dependencies for Dattak Community Shield POC

echo "================================================"
echo "  DATTAK COMMUNITY SHIELD - Installation"
echo "================================================"
echo ""

# Check Python version
echo "Checking Python version..."
python3 --version

echo ""
echo "Installing dependencies..."
echo ""

# Central Server
echo "📦 [1/4] Installing Central Server dependencies..."
cd central_server
pip3 install -r requirements.txt
cd ..

# Site A
echo "📦 [2/4] Installing Site A dependencies..."
cd site_a
pip3 install -r requirements.txt
cd ..

# Site B
echo "📦 [3/4] Installing Site B dependencies..."
cd site_b
pip3 install -r requirements.txt
cd ..

# Attacker
echo "📦 [4/4] Installing Attack Bot dependencies..."
cd attacker
pip3 install -r requirements.txt
cd ..

echo ""
echo "================================================"
echo "✅ Installation complete!"
echo "================================================"
echo ""
echo "To start the demo:"
echo "1. Open 4 terminals"
echo "2. Terminal 1: ./start_central.sh"
echo "3. Terminal 2: ./start_site_a.sh"
echo "4. Terminal 3: ./start_site_b.sh"
echo "5. Terminal 4: ./attack_site_a.sh"
echo ""
echo "See README.md for the full demo script."
echo ""

