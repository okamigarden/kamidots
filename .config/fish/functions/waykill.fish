function waykill --wraps='pkill waybar && hyprctl dispatch exec waybar' --description 'alias waykill=pkill waybar && hyprctl dispatch exec waybar'
  pkill waybar && hyprctl dispatch exec waybar $argv
        
end
