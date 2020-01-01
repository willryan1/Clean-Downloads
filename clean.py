#!/usr/bin/env python3

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import sys
from lib.mappings import get_current_mappings
from lib.mappings import get_directory

M_PATH = "mappings.json"

MAPPINGS = get_current_mappings(M_PATH)


def get_path():
    return os.path.abspath(__file__)


class NewHandler(FileSystemEventHandler):
    def __init__(self, directory):
        self.directory = directory

    def set_dir(self, directory):
        self.directory = directory

    def on_created(self, event):
        src_path = event.src_path
        if os.path.isdir(src_path):
            return
        _, file_extension = os.path.splitext(src_path)
        try:
            dest_dir = MAPPINGS[file_extension.lower()]
        except KeyError:
            print("Extension {} did not exist in MAPPINGS".format(file_extension))
            return
        base_directory = os.path.dirname(src_path)
        file_name = os.path.basename(src_path)
        new_path = base_directory + "/" + dest_dir + "/" + file_name
        new_directory = os.path.dirname(new_path)
        if not os.path.exists(new_directory):
            try:
                os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory {} failed".format(new_directory))
                return
        if not os.path.isfile(src_path):
            print("{} is not a file".format(src_path))
            return
        try:
            os.rename(src_path, new_path)
        except FileExistsError:
            print("File {} already exists.\n {} will not be moved".format(new_path, src_path))
        except OSError:
            print("{} is a non empty dictionary. Must be removed.".format(new_path))
        except Exception as err:
            print(err)


def main():
    folder_src = get_directory(M_PATH)
    if not os.path.isdir(folder_src):
        sys.exit("The directory given in the json file is not a valid directory")
    event_handler = NewHandler(folder_src)
    observer = Observer()
    observer.schedule(event_handler, folder_src, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
