bash
#!/bin/bash

set -e

echo "****************************************"
echo " Setting up Capstone Environment"
echo "****************************************"

echo "Installing Python 3.14 and Virtual Environment"

sudo apt-get update

sudo DEBIAN_FRONTEND=noninteractive apt-get install -y \
    python3.14 \
    python3.14-venv \
    python3-pip

echo "Checking the Python version..."
python3.14 --version

echo "Creating a Python virtual environment"
python3.14 -m venv ~/venv

echo "Configuring the developer environment..."

touch ~/.bashrc

echo "# DevOps Capstone Project additions" >> ~/.bashrc
echo "export GITHUB_ACCOUNT=$GITHUB_ACCOUNT" >> ~/.bashrc

echo 'export PS1="\[\e]0;\u:\W\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ "' >> ~/.bashrc

echo "source ~/venv/bin/activate" >> ~/.bashrc

echo "Installing Python dependencies..."

source ~/venv/bin/activate

python -m pip install --upgrade pip wheel

pip install -r requirements.txt

pip install pytest requests

echo "Starting the Postgres Docker container..."

make db

echo "Checking the Postgres Docker container..."

docker ps

echo "****************************************"
echo " Capstone Environment Setup Complete"
echo "****************************************"

echo ""
echo "Use 'exit' to close this terminal and open a new one to initialize the environment"
echo ""
