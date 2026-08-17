# 4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

def list_directory_contents(path="."):
    """
    Prints all files and directories in the given path.
    Default path is the current working directory.
    """
    try:
        # Validate that the path exists and is a directory
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"Error: '{path}' is not a directory.")
            return

        # List all files and directories
        contents = os.listdir(path)
        if not contents:
            print(f"The directory '{path}' is empty.")
            return

        print(f"Contents of '{path}':")
        for item in contents:
            print(item)

    except PermissionError:
        print(f"Permission denied: Cannot access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# You can change the path below to any directory you want to inspect
directory_path = "."  # Current directory
list_directory_contents(directory_path)
