import os
from lib.mappings import get_current_mappings
from lib.mappings import get_all_directories

mapping = "mappings.json"

MAPPINGS = get_current_mappings(mapping)


def organize(path):
    files_in_downloads = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]

    for file in files_in_downloads:
        file_path = os.path.join(path, file)

        _, file_extension = os.path.splitext(file_path)
        try:
            dest_dir = MAPPINGS[file_extension.lower()]
        except KeyError:
            print("Extension {} did not exist in MAPPINGS".format(file_extension))
            continue
        base_directory = path
        file_name = file
        new_path = base_directory + "/" + dest_dir + "/" + file_name
        new_directory = os.path.dirname(new_path)
        if not os.path.exists(new_directory):
            try:
                os.mkdir(new_directory)
            except OSError:
                print("Creation of the directory {} failed".format(new_directory))
                return
        try:
            os.rename(file_path, new_path)
        except Exception as e:
            print("{}  :  {}".format(e, file))


def reorganize(path):
    directories = get_all_directories(mapping)
    dirs_in_downloads = [os.path.join(path, file) for file in os.listdir(path)
                         if os.path.isdir(os.path.join(path, file))]
    for directory in dirs_in_downloads:
        directory_name = os.path.basename(directory)
        if directory_name not in directories:
            # Maybe think about making it recursive to deal with directories as well
            files_in_dir = [os.path.join(directory_name, file) for file in os.listdir(directory_name)
                            if os.path.isfile(os.path.join(directory_name, file))]
            for file in files_in_dir:
                file_name = os.path.basename(file)
                new_path = path + "/" + file_name
                try:
                    os.rename(file, new_path)
                except FileExistsError:
                    print("File {} already exists.\n {} will not be moved".format(new_path, file))
                except OSError:
                    print("{} is a non empty dictionary. Must be removed.".format(new_path))
                except Exception as err:
                    print(err)
    organize(path)
