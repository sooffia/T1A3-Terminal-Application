#!/bin/bash

# Debug: Print current directory
echo "Current directory: $(pwd)"

# Navigate to the directory where the script is located
cd /src

# Debug: Print current directory after navigation
echo "Current directory after navigation: $(pwd)"

# Check if Python 3 is installed and the correct version
if [[ -x "$(command -v python3)" ]]; then
  pyv="$(python3 -V 2>&1)"
  echo "Python version: $pyv"
  if [[ $pyv == "Python 3.12"* ]]; then
    echo "The required version of Python is installed and ready to use."
  else
    echo "Please install Python version 3.12 or newer to run this application." >&2
    exit 1  # Exit with an error code
  fi
else
  echo "Python 3 is not installed on your system. Please install Python version 3.12 (or newer) to run this application." >&2
  exit 1  # Exit with an error code
fi

echo "Creating a virtual environment named .venv and activating it."
python3 -m venv .venv
source .venv/bin/activate

echo "Installing the required dependencies for the application."
pip install -r ./requirements.txt

echo "Running the application."
python3 ./main.py 

# Deactivate the virtual environment after running the script
deactivate
