#!/bin/bash
# v1.0

echo "Note: This Installer Only Add the Pixegami theme to ghostty themes"
if [  -f /usr/share/ghostty/themes/Pixegami ]; then
    sudo rm /usr/share/ghostty/themes/Pixegami
    sudo cp Pixegami /usr/share/ghostty/themes/
    echo "Pixegami Theme Added"
else
    sudo cp Pixegami /usr/share/ghostty/themes/
    echo "Pixegami Theme Added"
fi


