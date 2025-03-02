function seagate --wraps='sudo systemctl status smb nmb' --description 'alias seagate=sudo systemctl status smb nmb'
  sudo systemctl status smb nmb $argv
        
end
