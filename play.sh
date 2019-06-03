#!/bin/bash
echo "Welcome to Text Adventure"
echo ""

source venv/bin/activate
pip install -r requirements.txt
python play.py build
python play.py play