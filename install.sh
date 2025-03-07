#!/bin/bash

# Script to install required packages for Hyprland setup
# Works on Arch Linux and Arch-based distros

# Ensure the script runs as root
if [[ $EUID -ne 0 ]]; then
    echo "Please run this script as root using sudo."
    exit 1
fi


#Variable locations
TARGET_DIR="$HOME/.config"


echo "Updating system..."
pacman -Syu --no-confirm

echo "Installing official packages..."
pacman -S --needed --noconfirm \
    kitty dolphin firefox polkit-kde-agent polkit-gnome wl-clipboard dbus udiskie \
    swaylock grim slurp brightnessctl pipewire playerctl kvantum \
    nm-applet powerline-fonts fish
    

# Determine which AUR helper to use: paru or yay
if command -v paru &> /dev/null; then
    AUR_HELPER="paru"
elif command -v yay &> /dev/null; then
    AUR_HELPER="yay"
else
    echo "Neither paru nor yay found. Installing paru..."
    pacman -S --needed --noconfirm git base-devel
    git clone https://aur.archlinux.org/paru.git /tmp/paru
    cd /tmp/paru || exit
    makepkg -si --noconfirm
    cd - || exit
    AUR_HELPER="paru"
fi

echo "Using $AUR_HELPER to install AUR packages..."
$AUR_HELPER -S --needed --noconfirm \
    hypridle cliphist swww vesktop-bin xdg-desktop-portal-hyprland \
    swappy wlogout
echo "All dependencies installed successfully!"

# Rsync command
if ! command -v rsync &> /dev/null; then
    echo "Installing sync..."
    pacman -S --needed --no-confirm rsync
fi

#Prompt before overwriting .config files.
if [[ -d "$TARGET_DIR" ]]; then
    echo "Warning: The directory $TARGET_DIR already exists."
    read -rp "Do you want to overwrite the existing files? (y/N): " CONFIRM
    if [[ "$CONFIRM" != "y" && "$CONFIRM" != "Y" ]]; then
        echo "Aborting file copy. Existing files were not changed."
        exit 0
    fi
fi

#New Aliases in fish
echo "Creating new aliases for fish..."
alias -s hyprsettings='nano ~/.config/hypr/hyprland.conf'
alias -s weather='curl wttr.in'
alias -s wasd='systemctl poweroff'
alias -s hyprquit='hyprctl dispatch exit'
alias -s p='sudo pacman'



echo "Copying configuration files to $TARGET_DIR..."
mkdir -p "$TARGET_DIR"
rsync -avP "$(pwd)/" "$TARGET_DIR/"

echo "All dependencies installed and files copied successfully!"
echo "
                                                   
    ▄█   ▄█▄    ▄████████   ▄▄▄▄███▄▄▄▄    ▄█      
   ███ ▄███▀   ███    ███ ▄██▀▀▀███▀▀▀██▄ ███      
   ███▐██▀     ███    ███ ███   ███   ███ ███▌     
  ▄█████▀      ███    ███ ███   ███   ███ ███▌     
 ▀▀█████▄    ▀███████████ ███   ███   ███ ███▌     
   ███▐██▄     ███    ███ ███   ███   ███ ███      
   ███ ▀███▄   ███    ███ ███   ███   ███ ███      
   ███   ▀█▀   ███    █▀   ▀█   ███   █▀  █▀       
   ▀                                               
 ████████▄   ▄██████▄      ███        ▄████████    
 ███   ▀███ ███    ███ ▀█████████▄   ███    ███    
 ███    ███ ███    ███    ▀███▀▀██   ███    █▀     
 ███    ███ ███    ███     ███   ▀   ███           
 ███    ███ ███    ███     ███     ▀███████████    
 ███    ███ ███    ███     ███              ███    
 ███   ▄███ ███    ███     ███        ▄█    ███    
 ████████▀   ▀██████▀     ▄████▀    ▄████████▀"
