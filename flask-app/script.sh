#!/bin/bash

# Create venv if not exists
if [ ! -d "venv" ]; then
  python3 -m venv venv
fi

# Activate venv and install Flask
source venv/bin/activate
pip install flask

# Start the Flask app
nohup venv/bin/python app.py > app.log 2>&1 &

