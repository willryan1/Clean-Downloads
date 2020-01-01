# Clean Downloads
> Python script that automatically keeps your Downloads folder clean to your liking


## Usage

#### Install Dependencies
```shell script
pip install -r requirements.txt
```

#### Configuration File
The JSON file mappings.json holds all of the mappings of file extensions to the
directory names. It also holds the path of the directory will be organized.
By default the directory will be an empty sting in order to make the script work,
you must put the directory name there. The current mappings are my default mappings, feel free
to change them.

#### Running

After you have inputted the directory in mappings.json, you can now do many things on that
directory using run.py.

The script run.py executes all of the main functionality of this project.

```
python run.py [-h] action
```

There are 4 main commands that are accepted from the action command line arguments:
start, stop, organize, and stats. 

```shell script
python run.py start
```

Start will use nohup to call clean.py and start a process that will run in the background
to automatically clean the downloads folder. While the process is running, whenever
a file is moved or added to downloads, it will autmatically put it into the folder that is
assigned to its file extension in mappings.json.

To check if the process is running you can enter on mac or linux:
```
ps -e | grep clean.py
```
If the output looks like this:
```
28959 ttys000    0:02.19 python3 /Users/user/path/clean_downloads/clean.py
30788 ttys000    0:00.00 grep clean.py
```
If the top line is missing then the process is not running.

To stop the process, simply enter:
```shell script
python run.py stop
```

To organize your directory to the specifications in mappings.json you can enter:

```shell script
python run.py organize
```

This script will go through the directory and every file with an extension in the mappings.json 
file will be moved to the correct directory. Directories and files with extensions not in mappings.json,
will not be moved.

You can also use the stats action to find the stats about the directory chosen.

```shell script
python run.py stats
```

#### Still want to implement

Want to implement an other option to hold everything else if wanted (specific or not)

Want to implement a way to reorganize when the mappings are different (go through each
directory and check if it is a mapping, and if not put it back to the base directory
then go back through and reorganize)

Think bigger to how to organize whole computer / file system

Maybe: check for empty files recursively

## JSON Mappings

Put your mappings in a json format with the directories mapped to a list of text extentions
that will organize the files

Options: Look for best default settings

Also: try and find a database with all of the extensions

Maybe implement an ordering by time
