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
DOWNLOAD_URL="https://example.com/path/to/sman-linux-x86_64.tar.gz"  # Replace with actual download URL
TAR_FILE="sman-linux-x86_64.tar.gz"

# Ensure necessary packages are installed
apt-get update
apt-get install -y python3 python3-pip wget  # Install Python, pip, and wget

# Download the application archive
wget "$DOWNLOAD_URL" -O "$TAR_FILE"

# Extract the application archive
mkdir -p "$INSTALL_DIR"
tar -xzvf "$TAR_FILE" -C "$INSTALL_DIR" --strip-components=1

# Install Python dependencies
pip3 install -r "$INSTALL_DIR/requirements.txt"

# Create a symbolic link for easy access
ln -s "$INSTALL_DIR/sman" /usr/local/bin/sman

# Optional: Set permissions (adjust as needed)
chmod +x /usr/local/bin/sman

# Clean up downloaded archive
rm "$TAR_FILE"

echo "sman has been successfully installed."
echo "You can now run it using 'sman' command."
