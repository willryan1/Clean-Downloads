import json


def get_current_mappings(mapping):
    current_mappings = {}
    with open(mapping, "r") as read_file:
        mappings = json.load(read_file)
    for directory, file_ext in mappings["file_types"].items():
        for ext in file_ext:
            current_mappings["."+ext] = directory
    return current_mappings


def get_all_directories(mapping):
    directories = []
    with open(mapping, "r") as f:
        mappings = json.load(f)["file_types"]
    for directory in mappings:
        directories.append(directory)
    return directories


def get_directory(mapping):
    with open(mapping, "r") as f:
        directory = json.load(f)["directory"]
    return directory
