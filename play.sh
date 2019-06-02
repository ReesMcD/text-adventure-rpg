#!/bin/bash
echo "Welcome to Text Adventure"
echo ""

source venv/bin/activate
python play.py build
python play.py play