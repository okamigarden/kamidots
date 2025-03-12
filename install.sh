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
ICONS_DIR="/usr/share/icons"
WALL_DIR="$(pwd)/Wallpapers"

echo "Updating system..."
pacman -Syu --noconfirm

echo "Installing official packages..."
pacman -S --needed --noconfirm \
    kitty dolphin firefox polkit-kde-agent polkit-gnome wl-clipboard dbus udiskie \
    grim slurp brightnessctl pipewire playerctl kvantum powerline-fonts fish paru \
    yay waybar

# Determine which AUR helper to use: paru or yay
if command -v paru &> /dev/null; then
    AUR_HELPER="paru"
elif command -v yay &> /dev/null; then
    AUR_HELPER="yay"
else
    echo "Error: No AUR helper found! Install paru or yay first."
    exit 1
fi

echo "Using $AUR_HELPER to install AUR packages..."
# Run paru/yay as the normal user (not root)
if [[ -n "$SUDO_USER" ]]; then
    sudo -u "$SUDO_USER" $AUR_HELPER -S --needed --noconfirm \
        hypridle cliphist swww xdg-desktop-portal-hyprland \
        swappy wlogout
fi


echo "All dependencies installed successfully!"

# Ensure rsync is installed
if ! command -v rsync &> /dev/null; then
    echo "Installing rsync..."
    pacman -S --needed --noconfirm rsync
fi

# Confirmation Message (DO YOU WANT TO PROCEED)
BACKUP_DIR="$USER_HOME/.config_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"

if [[ -d "$TARGET_DIR" ]]; then
    echo "Backing up existing .config directory to $BACKUP_DIR..."
    mkdir -p "$BACKUP_DIR"
    rsync -rvP "$TARGET_DIR/" "$BACKUP_DIR"
fi

# Warn before overwriting .config files.
echo "Warning: The directory $TARGET DIR already exists."
read -r -p "Do you want to overwrite the existing files? (y/N): " CONFIRM
if [[ "$CONFIRM" != "y" && "$CONFIRM" != "Y" ]]; then
    echo "Aborting file copy. Existing files were not overwritten."
    exit 0
fi

# Copying kamidots to .config
echo "Copying kamidots files to $TARGET_DIR..."
mkdir -p "$TARGET_DIR"
rsync -rvP --delete --chown=$SUDO_USER:$SUDO_USER "$(pwd)/.config/" "$TARGET_DIR/"
rsync -rvP --delete --chown=$SUDO_USER:$SUDO_USER "$(pwd)/usr/share/icons/" "$ICONS_DIR"
sudo chown -R $SUDO_USER:$SUDO_USER "$USER_HOME/.config"


# Add aliases to Fish shell configuration
echo "Adding new aliases for Fish shell..."
FISH_CONFIG="$USER_HOME/.config/fish/config.fish"

# Ensure the config file exists
mkdir -p "$USER_HOME/.config/fish"
touch "$FISH_CONFIG"

# Append aliases only if non-existing
grep -qxF "alias hyprsettings='nano ~/.config/hypr/hyprland.conf'" "$FISH_CONFIG" || echo "alias hyprsettings='nano ~/.config/hypr/hyprland.conf'" >> "$FISH_CONFIG"
grep -qxF "alias wasd='systemctl poweroff'" "$FISH_CONFIG" || echo "alias wasd='systemctl poweroff'" >> "$FISH_CONFIG"
grep -qxF "alias hyprquit='hyprctl dispatch exit'" "$FISH_CONFIG" || echo "alias hyprquit='hyprctl dispatch exit'" >> "$FISH_CONFIG"
grep -qxF "alias p='sudo pacman'" "$FISH_CONFIG" || echo "alias p='sudo pacman'" >> "$FISH_CONFIG"
echo "Aliases added successfully to $FISH_CONFIG"


# Set wallpaper for user
echo "Setting wallpaper!"
sudo -u "$SUDO_USER" swww img "$WALL_DIR/wallhaven-48kgk4.png"

echo "All dependencies installed, configurations copied, and aliases set!"
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                 
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
████████▀   ▀██████▀     ▄████▀    ▄████████▀
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"        
                                                 

echo "Setup complete!"
