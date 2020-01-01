import subprocess
import os
import stat
import argparse
import sys
from clean import get_path
from lib.mappings import get_directory
from lib.organize import organize
from lib.downloads_stats import display_download_stats

M_PATH = "mappings.json"

PATH = get_path()


def run():
    st = os.stat('sh_files/run.sh')
    os.chmod("sh_files/run.sh", st.st_mode | stat.S_IEXEC)
    rc = subprocess.check_call(["./sh_files/run.sh", '{}'.format(PATH)])


def stop():
    st = os.stat('sh_files/stop.sh')
    os.chmod("sh_files/stop.sh", st.st_mode | stat.S_IEXEC)
    rc = subprocess.check_call(["./sh_files/stop.sh", "{}".format(PATH)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Start or stop a script to automatically organize "
                                                 "the downloads folder")
    # parser.add_argument("directory", help="Directory to clean")
    parser.add_argument("action", help="Either start or stop to run or stop the process")
    args = parser.parse_args()
    # if not os.path.isdir(args.directory):
    #    sys.exit("The directory given is not a valid directory")
    if args.action == "start":
        d = get_directory(M_PATH)
        if not os.path.isdir(d):
            y_n = input("WARNING: The current directory in mappings.json is not a valid directory. Would you like to"
                        " proceed (y,n): ")
            y_n = y_n.lower()
            if y_n == "y" or y_n == "yes":
                print("Continuing, check output.log for any possible error messages")
            else:
                sys.exit("Stopping...")
        empty = True
        try:
            empty = os.stat("pid.txt").st_size == 0
        except FileNotFoundError:
            pass
        except Exception as err:
            print(err)
        if not empty:
            print("The process is already running.")
        else:
            run()
            print("Process started!")
    elif args.action == "stop":
        try:
            stop()
            print("Process Ended")
        except subprocess.CalledProcessError:
            print("Process is not currently activated. No need to stop.")
        except Exception as err:
            print(err)
    elif args.action == "organize":
        d = get_directory(M_PATH)
        organize(d)
    elif args.action == "stats":
        d = get_directory(M_PATH)
        display_download_stats(d)
    else:
        print("Only excepts arguments: start and stop")
