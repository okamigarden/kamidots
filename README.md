# Kamidots Configuration かみ

These dotfiles represent my personal work, entertainment, and daily operating setup.

## 📌 Overview

This project is an ongoing development of my .config files, designed to be optimised for performance, gaming, usability, and aesthetics.

## 🚀 Installation Script

A script is available to automate the installation process. It ensures that all the necessary dependencies are installed and it applies all configurations seamlessly.

Installation Command
```
./install.sh
```
⚠️ WARNING: Any personal modifications may be overwritten!


## 🔧 Manual Installation

If you prefer a manual setup, you can copy the required configuration files into your .config directory.

Manual Installation Command
```
rsync -avf ~/kamidots/.config ~/.config
```
Refer to the manual installation guide for specific application configurations.

⚠️ WARNING: Any personal modifications may be overwritten!


## 🎨 Themes & Colour Schemes

Customization is key! A variety of themes and colour schemes are available to match your aesthetic preferences. You can switch between themes using the theme manager.

Apply a Theme
```
./theme_manager.sh apply theme-name
```
Check out the themes documentation for more options.

## 🔄 Updating Configurations

To keep your configurations updated with the latest changes, run:
```
cd ~/kamidots
git pull origin master
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

   

## ⚖️ License

This project is licensed under the MIT License. See LICENSE for more details.

