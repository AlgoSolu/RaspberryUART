#!/bin/sh
sudo apt-get install python-imaging python-imaging-tk
sudo apt-get install python3-pil python3-pil.imagetk
pip install pyinstaller
sudo rm -rf dist/
sudo rm -rf build/
sudo rm  /usr/bin/verger/verger
sudo rm ~/Desktop/verger.desktop
/home/pi/.local/bin/pyinstaller --add-data 'ressources/:./ressources' --onefile --hidden-import=tkinter -y --hidden-import=serial --hidden-import='PIL._tkinter_finder'  main.py
sudo cp ressources/icon.png /usr/share/pixmaps/verger.png
sudo mkdir /usr/bin/verger
sudo cp dist/main /usr/bin/verger/verger
cp verger.desktop ~/Desktop/verger.desktop
cp verger.desktop ~/.config/autostart/verger.desktop
