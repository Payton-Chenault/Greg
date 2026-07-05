@echo off

call .venv\Scripts\activate.bat
echo activating venv

echo compiling to exe
pyinstaller --noconsole --onefile --add-data "assets;assets" --name "VolumeMonitor" MainApp.py

echo cleaning up
if exist build rmdir /s /q build
if exist VolumeMonitor.spec del /q VolumeMonitor.spec

echo deactivating venv
deactivate