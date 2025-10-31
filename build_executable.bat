pyinstaller -y --name=dartboard dartboard/dartboard_main.py
xcopy dartboard\backend\migrations dist\dartboard\backend\migrations\ /E/H
