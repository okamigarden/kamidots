# Kamidots Configuration かみ

These dotfiles represent our collaborators personal work, entertainment, and daily operating setup.

## 📌 Overview

This project is an ongoing development of our configuration files, designed to be optimised for performance, gaming, usability, and aesthetics.

## 🚀 Installation Script (EXPERIMENTAL)
> [!CAUTION]
> ⚠️ WARNING: Any personal modifications will be overwritten! Create a backup!

An experimental script is available to automate the installation process. It ensures that all the necessary dependencies are installed and it applies all configurations.

Installation Command
```
sudo ./install.sh
```

## 🔧 Manual Installation
> [!CAUTION]
> ⚠️ WARNING: Any personal modifications will be overwritten! Create aa backup.

Manual Installation Command
1. Copy configuration files over to system.
```
./backup.sh
rsync -av --progress ~/kamidots/.config/ ~/.config/
rsync -av --progress ~/kamidots/.local/ ~/.local/
sudo rsync -av --progress ~/kamidots/usr/ /usr/
```

2. Wallpaper Setup
```
mkdir -p ~/Pictures/Wallpapers
rsync -av ~/kamidots/Wallpapers/ ~/Pictures/Wallpapers
swww-daemon
swww img ~/Pictures/Wallpapers/wallhaven-48kgk4.png
```
If you have a second monitor:
```
Example (Replace HDMI-A-1 with second monitor):
swww img -o "HDMI-A-1" --transition-type random ~/Pictures/Wallpapers/wallhaven-48kgk4.png
```

3. Dolphin Setup
```
mkdir -p ~/.local/share/dolphin
mv ~/kamidots/.local/share/dolphin ~/.local/share/dolphin
```

4. Additional Information
```
less READ_AFTER_INSTALLATION.txt
```
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
1. cd ~/kamidots
2. git fetch origin master
3. git pull origin master
4. Complete manual installation again.

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

