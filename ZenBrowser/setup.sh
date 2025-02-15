curl https://updates.zen-browser.app/appimage.sh > appimage.sh
sudo chmod +x appimage.sh
./appimage.sh
echo "/home/tenet/.local/share/AppImage/ZenBrowser.AppImage" > zen
sudo chmod +x zen
sudo cp zen /usr/bin/
