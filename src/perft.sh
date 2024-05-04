#!/bin/sh

# Move to the directory where the Python script is located
# cd "$(dirname "$0")/chess"

python3 "./src/perft.py" "$1" "$2"
