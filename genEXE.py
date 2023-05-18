from PyInstaller.__main__ import run

run([
    "plan.py",
    "--noconsole",
    "--onefile",
    "--noconfirm",
    #"--log-level WARN",
    "--icon=includes\calendar.ico",
    "-n=Plan",
    "--add-data=includes\\*;includes"
])