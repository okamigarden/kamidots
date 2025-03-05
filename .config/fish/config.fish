if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Handy change dir shortcuts
abbr .1 'cd ..'
abbr .2 'cd ../..'
abbr .3 'cd ../../..'
abbr .4 'cd ../../../..'
abbr .5 'cd ../../../../..'


# Always mkdir a path (this doesn't inhibit functionality to make a single dir)
abbr mkdir 'mkdir -p'
abbr ls 'ls -al'

fish_add_path /home/fabian/.spicetify
