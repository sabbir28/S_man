#!/bin/bash

set -euo pipefail  # Exit immediately if a command fails, and handle errors in pipelines
IFS=$'\n\t'  # Improve handling of word splitting and special characters

# Check if script is run with root privileges
if [ "$(id -u)" -ne 0 ]; then
    echo "Please run this script as root or using sudo."
    exit 1
fi

# Define variables
APP_DIR="/opt/sman"
INSTALL_DIR="$APP_DIR/sman-linux-x86_64"
DOWNLOAD_URL="https://github.com/sabbir28/S_man/raw/main/build_excutable/linux/sman-linux-x86_64.tar.gz"
REQUIREMENTS_URL="https://github.com/sabbir28/S_man/raw/main/requirements.txt"
TAR_FILE="sman-linux-x86_64.tar.gz"
TMP_DIR=$(mktemp -d)  # Create a temporary directory

# Function to handle cleanup on script exit or error
cleanup() {
    local exit_status=$?
    rm -rf "$TMP_DIR"  # Clean up temporary directory
    exit $exit_status
}
trap cleanup EXIT  # Ensure cleanup function is called on script exit

# Function to handle errors
handle_error() {
    local error_message="$1"
    echo "Error: $error_message"
    cleanup
    exit 1
}

# Ensure necessary packages are installed
apt-get update || handle_error "Failed to update package lists."
apt-get install -y python3 python3-pip wget || handle_error "Failed to install packages."

# Download the application archive
wget -q "$DOWNLOAD_URL" -P "$TMP_DIR" || handle_error "Failed to download application archive."

# Extract the application archive
mkdir -p "$INSTALL_DIR" || handle_error "Failed to create installation directory."
tar -xzf "$TMP_DIR/$TAR_FILE" -C "$INSTALL_DIR" --strip-components=1 || handle_error "Failed to extract application archive."

# Download requirements.txt separately
wget -q "$REQUIREMENTS_URL" -O "$INSTALL_DIR/requirements.txt" || handle_error "Failed to download requirements file."

# Install Python dependencies
pip3 install -r "$INSTALL_DIR/requirements.txt" || handle_error "Failed to install Python dependencies."

# Remove existing symbolic link if it exists
if [ -L "/usr/local/bin/sman" ]; then
    rm -f /usr/local/bin/sman || handle_error "Failed to remove existing symbolic link."
fi

# Create a symbolic link for easy access
ln -sf "$INSTALL_DIR/sman" /usr/local/bin/sman || handle_error "Failed to create symbolic link."

# Optional: Set permissions (adjust as needed)
chmod +x /usr/local/bin/sman || handle_error "Failed to set execute permissions."

# Clean up temporary files
cleanup

echo "sman has been successfully installed."
echo "You can now run it using 'sman' command."
