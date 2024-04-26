DEL /Q /S Plan.exe
pyinstaller plan.py --noconsole --onefile --noconfirm --icon=includes\calendar.ico -n=Plan --add-data=includes\base.png;includes --add-data=includes\dni.txt;includes --add-data=includes\przedmioty.txt;includes --add-data=includes\wolne.txt;includes
move /Y dist\Plan.exe %cd%
rmdir /Q /S build
DEL /Q /S Plan.Spec