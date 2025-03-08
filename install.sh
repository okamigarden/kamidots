#!/bin/bash

# Script to install required packages for Hyprland setup
# Works on Arch Linux and Arch-based distros

# Ensure the script runs as root
if [[ $EUID -ne 0 ]]; then
    echo "Please run this script as root using sudo."
    exit 1
fi

# Get the real home directory of the user running the script
USER_HOME=$(eval echo ~${SUDO_USER:-$USER})
TARGET_DIR="$USER_HOME/.config"

echo "Updating system..."
pacman -Syu --noconfirm

echo "Installing official packages..."
pacman -S --needed --noconfirm \
    kitty dolphin firefox polkit-kde-agent polkit-gnome wl-clipboard dbus udiskie \
    swaylock grim slurp brightnessctl pipewire playerctl kvantum \
    nm-applet powerline-fonts fish kservice5 kservice6

# Determine which AUR helper to use: paru or yay
if command -v paru &> /dev/null; then
    AUR_HELPER="paru"
elif command -v yay &> /dev/null; then
    AUR_HELPER="yay"
else
    echo "Neither paru nor yay found."
    pacman -S --needed --noconfirm git base-devel
    read -rp "Do you want to install yay or paru? [(Y)ay/(P)aru] " CONFIRM
    if [[ "$CONFIRM" == "y" ]]; then
        echo "Installing yay..."
        git clone https://aur.archlinux.org/yay.git
        cd yay || exit
        makepkg -si --noconfirm
        cd ..
        rm -rf yay
        AUR_HELPER="yay"
    elif [[ "$CONFIRM" == "p" ]]; then
        echo "Installing paru..."
        git clone https://aur.archlinux.org/paru.git
        cd paru || exit
        makepkg -si --noconfirm
        cd ..
        rm -rf paru
        AUR_HELPER="paru"
    else
        echo "Invalid choice. Exiting..."
        exit 1
    fi
fi

echo "Using $AUR_HELPER to install AUR packages..."
$AUR_HELPER -S --needed --noconfirm \
    hypridle cliphist swww vesktop-bin xdg-desktop-portal-hyprland \
    swappy wlogout

echo "All dependencies installed successfully!"

# Ensure rsync is installed
if ! command -v rsync &> /dev/null; then
    echo "Installing rsync..."
    pacman -S --needed --noconfirm rsync
fi

# Prompt before overwriting .config files.
if [[ -d "$TARGET_DIR" ]]; then
    echo "Warning: The directory $TARGET_DIR already exists."
    read -rp "Do you want to overwrite the existing files? (y/N): " CONFIRM
    if [[ "$CONFIRM" != "y" && "$CONFIRM" != "Y" ]]; then
        echo "Aborting file copy. Existing files were not changed."
        exit 0
    fi
fi

# Copy configuration files using rsync
echo "Copying configuration files to $TARGET_DIR..."
mkdir -p "$TARGET_DIR"
rsync -avP "$(pwd)/" "$TARGET_DIR/"

# Add aliases to Fish shell configuration
echo "Adding new aliases for Fish shell..."
FISH_CONFIG="$USER_HOME/.config/fish/config.fish"

# Ensure the config file exists
mkdir -p "$USER_HOME/.config/fish"
touch "$FISH_CONFIG"

{
    echo "alias hyprsettings='nano ~/.config/hypr/hyprland.conf'"
    echo "alias weather='curl wttr.in'"
    echo "alias wasd='systemctl poweroff'"
    echo "alias hyprquit='hyprctl dispatch exit'"
    echo "alias p='sudo pacman'"
} >> "$FISH_CONFIG"

echo "Aliases added successfully to $FISH_CONFIG"

echo "All dependencies installed, configurations copied, and aliases set!"
echo "Setup complete!"
