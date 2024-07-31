#!/bin/bash

# Determine the OS platform
OS="$(uname -s)"

case "$OS" in
    Linux*)
        # Determine the Linux distribution (Debian/Ubuntu or Arch Linux)
        if [ -f /etc/debian_version ]; then
            echo "Detected Debian-based Linux"
            sudo apt update && sudo apt install ffmpeg && pip install -U openai-whisper
        elif [ -f /etc/arch-release ]; then
            echo "Detected Arch Linux"
            sudo pacman -S ffmpeg && pip install -U openai-whisper
        else
            echo "Unsupported Linux distribution"
        fi
        ;;
    Darwin*)
        echo "Detected macOS"
        # Check if Homebrew is installed
        if command -v brew >/dev/null 2>&1; then
            brew install ffmpeg && pip install -U openai-whisper
        else
            echo "Homebrew is not installed, please install it first from https://brew.sh"
        fi
        ;;
    CYGWIN*|MINGW32*|MSYS*)
        echo "Detected Windows"
        # Check for Chocolatey and Scoop, and prefer Chocolatey if both are installed
        if command -v choco >/dev/null 2>&1; then
            choco install ffmpeg && pip install -U openai-whisper
        elif command -v scoop >/dev/null 2>&1; then
            scoop install ffmpeg && pip install -U openai-whisper
        else
            echo "Neither Chocolatey nor Scoop is installed, please install one of them first."
        fi
        ;;
    *)
        echo "Unsupported OS"
        ;;
esac
