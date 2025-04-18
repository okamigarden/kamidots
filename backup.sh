#!/bin/bash
# Timestamped backup directory
backup_dir=~/kamidots-backup-$(date +%Y%m%d_%H%M%S)
mkdir -p "$backup_dir"

# Backup .config
if [ -d ~/.config ]; then
  rsync -av --progress ~/.config "$backup_dir/.config"
fi

# Backup Dolphin config
if [ -d ~/.local/share/dolphin ]; then
  mkdir -p "$backup_dir/.local/share"
  rsync -av --progress ~/.local/share/dolphin "$backup_dir/.local/share/dolphin"
fi

# Backup shell configs
if [ -d ~/.bashrc ]; then
  mkdir -p "$backup_dir/"
  rsync -av --progress ~/.local/share/dolphin "$backup_dir/"
fi

echo "✅ Backup complete. Stored at: $backup_dir"

