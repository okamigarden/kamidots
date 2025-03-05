function wasd --wraps='systemctl poweroff' --description 'alias wasd=systemctl poweroff'
  systemctl poweroff $argv
        
end
