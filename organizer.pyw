import os
import shutil
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# Author: Michael Ly
# Date: 7/24/2022
# Moves files in the downloads folder to other folders based on the file type

downloads_path = r"C:\Users\micha\Downloads"
dest_dir_sfx = r"C:\Users\micha\Desktop\Dws\SFX"
dest_dir_img = r"C:\Users\micha\Desktop\Dws\img"
dest_dir_mus = r"C:\Users\micha\Desktop\Dws\music"
dest_dir_exe = r"C:\Users\micha\Desktop\Dws\exe"
dest_dir_pdf = r"C:\Users\micha\Desktop\Dws\pdf"
dest_dir_vid = r"C:\Users\micha\Desktop\Dws\video"
dest_dir_mic = r"C:\Users\micha\Desktop\Dws\outlook"
dest_dir_cmp = r"C:\Users\micha\Desktop\Dws\compressed"
dest_dir_mod = r"C:\Users\micha\Desktop\Dws\modeling"
dest_dir_cod = r"C:\Users\micha\Desktop\Dws\code"

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
                elif name.endswith('.pdf') or name.endswith('.txt') or name.endswith('.pem'):
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