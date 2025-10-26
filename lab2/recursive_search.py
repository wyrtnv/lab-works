import os


def find_files(start_dir, extension):
    found_files = []

    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    return found_files


STARTING_DIRECTORY = '.'
TARGET_EXTENSION = '.py'

python_files = find_files(STARTING_DIRECTORY, TARGET_EXTENSION)

if python_files:
    print(
        f"Found {len(python_files)} file(s) with extension '{TARGET_EXTENSION}':")
    for file_path in python_files:
        print(f"- {file_path}")
else:
    print(f"No files with extension '{TARGET_EXTENSION}' found.")
