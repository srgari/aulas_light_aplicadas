#!/bin/sh

echo "Checking if a virtual environment is active."

# Run python and return 1 if inside a virtual environment, else return 0
# and store the value in the INVENV variable
INVENV=$(python -c 'import sys; print(0 if sys.prefix == sys.base_prefix else 1)')

# Check if variable is equal to 1
if [ $INVENV -eq 1 ]; then
  echo "Virtual environment detected! Proceeding..."
# Check if file exists
elif [ -f 'env/bin/activate' ]; then
  echo "Trying to activating environment..."
  source env/bin/activate
  echo "Proceeding..."
else
  echo "Cannot run 'env/bin/activate'."
  echo "Please activate or create your virtual environment."
  exit 1
fi

# Now you can run your data processing scripts...
