#!/bin/bash

# Install necessary dependencies
sudo apt-get update
sudo apt-get install -y python3-pip git

# Clone your Flask app repository
git clone https://github.com/houngnib/Azure-labs.git
# Navigate to the Flask app directory
cd Azure-labs

# Install Python dependencies
pip3 install -r requirements.txt

# Run the Flask app
nohup python3 microS.py > flask_app.log 2>&1 &
