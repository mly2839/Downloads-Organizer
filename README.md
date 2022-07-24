
# Project Details

- Start Date: 7/24/2022
- Author: Michael Ly

## Description

Organizes your downloads folder to separate subfolders based on the type of file it is.

## Start

- Copy code using http, ssh, etc
- Run 'pip install watchdog' or 'pip3 install watchdog' if on python 3.x
- Edit the downloads folder path and the destination paths properly
- Adjust/Add/Remove any file extensions you want
- Run by typing 'python organizer.py' or 'python3 organizer.py' if on python 3.x

This process will run continuously on the editor that you start it on until you kill it using CTRL + C

## Start Background

Runs this script in the background

- Copy code using http, ssh, etc
- Run 'python -m pip install watchdog' or 'python3 -m pip3 install watchdog' if on python 3.x
- Run 'python -m pip install pythonw' or 'python3 -m pip3 install pythonw' if on python 3.x
- Edit the downloads folder path and the destination paths properly
- Adjust/Add/Remove any file extensions you want
- Run by typing 'pythonw organizer.pyw'
- End task by running 'TASKKILL /F /IM pythonw.exe' on an elevated command line
