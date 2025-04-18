# Kamidots Configuration かみ

These dotfiles represent our collaborators personal work, entertainment, and daily operating setup.

## 📌 Overview

This project is an ongoing development of our .config files, designed to be optimised for performance, gaming, usability, and aesthetics.

## 🚀 Installation Script (EXPERIMENTAL)

An experimental script is available to automate the installation process. It ensures that all the necessary dependencies are installed and it applies all configurations.

Installation Command
```
sudo ./install.sh
```
> [!CAUTION]
> ⚠️ WARNING: Any personal modifications will be overwritten! Create a backup!


## 🔧 Manual Installation

If you prefer a manual setup, you can copy the required configuration files into your .config directory.
> [!CAUTION]
> ⚠️ WARNING: Any personal modifications will be overwritten! Create a backup!

Manual Installation Command
1. Copy configuration files over to system. ENSURE YOU BACKUP YOUR DATA!
```
rsync -av --progress ~/kamidots/.config/ ~/.config/
rsync -av --progress ~/kamidots/.local/ ~/.local/
rsync -av --progress ~/kamidots/usr/ /usr/
```

2. Wallpaper Setup
```
mkdir -p ~/Pictures/Wallpapers
rsync -av ~/kamidots/Wallpapers/ ~/Pictures/Wallpapers
swww-daemon
swww img ~/Pictures/Wallpapers/wallhaven-48kgk4.png
```
3. Dolphin Setup
mkdir -p ~/.local/share/dolphin
mv ~/kamidots/.local/share/dolphin ~/.local/share/dolphin
```
Refer to the manual installation guide for specific application configurations.

=======
> [!CAUTION]
> ⚠️ WARNING: Any personal modifications will be overwritten! Create a backup!


## 🎨 Themes & Colour Schemes

Customization is key! A variety of themes and colour schemes are available to match your aesthetic preferences. You can switch between themes using the theme manager.

Apply a Theme
```
WIP - Coming soon :)
```
Check out the themes documentation for more options.

## 🔄 Updating Configurations

To keep your configurations updated with the latest changes, run:
```
<<<<<<< HEAD
1. cd ~/kamidots
2. git pull origin master
3. Complete manual installation.
=======
cd /home/$USER/kamidots
git pull origin master
>>>>>>> 5c8361b6c2af18b79dd5bb0b49467bcd527ec783
```
## 💡 Contributing

Have suggestions or improvements? Feel free to contribute!

1. Fork the repository
2. Create a feature branch
```
git checkout -b feature-name
```
3. Commit your changes
```
git commit -m "Description of changes"
```
4. Push to GitHub
```
git push origin feature-name
```
5. Submit a pull request 🎉

## Known Issues // Troubleshooting
Broken 'Open with' in Dolphin after attempting to choose a specific application to open the file extension with.
Fixed by adding command to hyprland.conf

## ⚖️ License

This project is licensed under the MIT License. See LICENSE for more details.

