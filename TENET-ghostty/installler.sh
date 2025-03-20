#!/bin/bash
# v1.0

echo "Note: This Installer Only Add the TENET theme to ghostty themes"
if [  -f /usr/share/ghostty/themes/Pixegami ]; then
    sudo rm /usr/share/ghostty/themes/TENET
    sudo cp TENET /usr/share/ghostty/themes/
    echo "TENET Theme Added"
else
    sudo cp TENET /usr/share/ghostty/themes/
    echo "TENET Theme Added"
fi


