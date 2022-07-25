import base64

code = base64.b64encode(b"""

import os
import shutil
import sys
import time
import logging
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Author: Michael Ly
# Date: 7/25/2022
# Moves files in the downloads folder to other folders based on the file type

downloads_path = str(Path.home() / "Downloads")
dest_dir_sfx = downloads_path + "\SFX"
if not os.path.exists(dest_dir_sfx):
    os.makedirs(dest_dir_sfx)
dest_dir_img = downloads_path + "\images"
if not os.path.exists(dest_dir_img):
    os.makedirs(dest_dir_img)
dest_dir_mus = downloads_path + "\music"
if not os.path.exists(dest_dir_mus):
    os.makedirs(dest_dir_mus)
dest_dir_exe = downloads_path + "\exe"
if not os.path.exists(dest_dir_exe):
    os.makedirs(dest_dir_exe)
dest_dir_pdf = downloads_path + "pdf"
if not os.path.exists(dest_dir_pdf):
    os.makedirs(dest_dir_pdf)
dest_dir_vid = downloads_path + "\ videos"
if not os.path.exists(dest_dir_vid):
    os.makedirs(dest_dir_vid)
dest_dir_mic = downloads_path + "\microsoft365"
if not os.path.exists(dest_dir_mic):
    os.makedirs(dest_dir_mic)
dest_dir_cmp = downloads_path + "\compressed files"
if not os.path.exists(dest_dir_cmp):
    os.makedirs(dest_dir_cmp)
dest_dir_mod = downloads_path + "\modeling"
if not os.path.exists(dest_dir_mod):
    os.makedirs(dest_dir_mod)
dest_dir_cod = downloads_path + "\code"
if not os.path.exists(dest_dir_cod):
    os.makedirs(dest_dir_cod)
dest_dir_msc = downloads_path + "\msc"
if not os.path.exists(dest_dir_msc):
    os.makedirs(dest_dir_msc)

# creates a unique name for the file if a duplicate exists
def makeUnique(path):
    path = path + "1"
    return path

# handles the actual moving of the file
def move(dest, entry, name):
    file_exists = os.path.exists(dest + "/" + name)
    if file_exists:
        unique_name = makeUnique(name)
        os.rename(entry, unique_name)
    shutil.move(entry, dest)

# handles the mapping of the file to the destination
class MoveHandler(FileSystemEventHandler):

    def on_modified(self, event):
        # scanning the downloads
        with os.scandir(downloads_path) as entries:
            # for looping through each one to find the specified file types
            for entry in entries:
                name = entry.name
                destination = downloads_path
                if name.endswith('.wave') or name.endswith('.mp3'):
                    if entry.stat().st_size < 25000000 or "SFX" in name:
                        destination = dest_dir_sfx
                    else:
                        destination = dest_dir_mus
                    move(destination, entry, name)
                elif name.endswith('.mp4') or name.endswith('.mov') or name.endswith('.mkv') or name.endswith('.gif'):
                    destination = dest_dir_vid
                    move(destination, entry, name)
                elif name.endswith('.jpg') or name.endswith('.jpeg') or name.endswith('.png') or name.endswith('.hdr') or name.endswith('.ico'):
                    destination = dest_dir_img
                    move(destination, entry, name)
                elif name.endswith('.msi') or name.endswith('.exe'):
                    destination = dest_dir_exe
                    move(destination, entry, name)
                elif name.endswith('.pdf'):
                    destination = dest_dir_pdf
                    move(destination, entry, name)
                elif name.endswith('.docx') or name.endswith('.pptx') or name.endswith('.dotx') or name.endswith('.csv'):
                    destination = dest_dir_mic
                    move(destination, entry, name)
                elif name.endswith('.zip') or name.endswith('.rar') or name.endswith('.7z') or name.endswith('.tgz'):
                    destination = dest_dir_cmp
                    move(destination, entry, name)
                elif name.endswith('.blend') or name.endswith('.obj') or name.endswith('.glb'):
                    destination = dest_dir_mod
                    move(destination, entry, name)
                elif name.endswith('.py') or name.endswith('.html') or name.endswith('.css') or name.endswith('.pug') or name.endswith('.jar') or name.endswith('.java') or name.endswith('.cpp') or name.endswith('.cs'):
                    destination = dest_dir_cod
                    move(destination, entry, name)
                else: 
                    destination = dest_dir_msc
                    move(destination, entry, name)

# watchdog setup here listens to the downloads folder and executes the move if a new file shows up
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = downloads_path
    event_handler = MoveHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

""")

exec(base64.b64decode(code))