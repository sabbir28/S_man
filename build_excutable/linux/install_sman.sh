#!/bin/bash

set -e  # Exit immediately if a command exits with a non-zero status

# Check if script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# Define variables
APP_DIR="/opt/sman"
INSTALL_DIR="$APP_DIR/sman-linux-x86_64"
DOWNLOAD_URL="https://github.com/sabbir28/S_man/raw/main/build_excutable/linux/sman-linux-x86_64.tar.gz"
TAR_FILE="sman-linux-x86_64.tar.gz"

# Ensure necessary packages are installed
apt-get update
apt-get install -y python3 python3-pip wget  # Install Python, pip, and wget

# Download the application archive
wget "$DOWNLOAD_URL" -P /tmp

# Extract the application archive
mkdir -p "$INSTALL_DIR"
tar -xzvf "/tmp/$TAR_FILE" -C "$INSTALL_DIR" --strip-components=1

# Install Python dependencies
pip3 install -r "$INSTALL_DIR/requirements.txt"

# Create a symbolic link for easy access
ln -sf "$INSTALL_DIR/sman" /usr/local/bin/sman

# Optional: Set permissions (adjust as needed)
chmod +x /usr/local/bin/sman

# Clean up downloaded archive
rm "/tmp/$TAR_FILE"

echo "sman has been successfully installed."
echo "You can now run it using 'sman' command."
