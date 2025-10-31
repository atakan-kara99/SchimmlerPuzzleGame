pyinstaller ^
  --onefile ^
  --noconsole ^
  --name schimmler ^
  --icon=../assets/icon.ico ^
  --add-data "../assets/icon.ico;assets" ^
  --distpath ../dist ^
  --workpath ../build ^
  ../src/main.py

pause
