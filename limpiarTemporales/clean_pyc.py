import os

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".pyc"):
            file_path = os.path.join(root, file)
            print(f"Deleting {file_path}")
            os.remove(file_path)