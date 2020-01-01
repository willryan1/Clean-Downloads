import os


def display_download_stats(path):
    files_in_downloads = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    n_files_in_downloads = len(files_in_downloads)

    directories_in_downloads = [os.path.join(path, file) for file in os.listdir(path) if
                                os.path.isdir(os.path.join(path, file))]
    n_directories_in_downloads = len(directories_in_downloads)

    empty_directories = [os.path.basename(directory) for directory in directories_in_downloads
                         if not os.listdir(directory)]
    n_empty_directories = len(empty_directories)

    directory_lengths = [len(os.listdir(directory)) for directory in directories_in_downloads]
    avg_directory_size = sum(directory_lengths) / len(directory_lengths)

    print("===========================================================")
    print("+++++++++++++++++++++ DOWNLOADS STATS +++++++++++++++++++++")
    print("===========================================================")
    print("Number of files: {}".format(n_files_in_downloads))
    print("Number of directories: {}".format(n_directories_in_downloads))
    print("Number of emtpy directories: {}".format(n_empty_directories))
    if n_empty_directories:
        print("The empty dictionaries are:\n")
        for d in empty_directories:
            print(d)
    print("Average directory size: {}".format(round(avg_directory_size, 2)))
    print("===========================================================")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("===========================================================")
