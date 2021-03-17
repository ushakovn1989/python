import os
import shutil

root_dir = 'my_project'
needed_dir = 'templates'
for root, folders, files in os.walk(root_dir):
    for folder in folders:
        if folder == needed_dir:
            path = os.path.join(root, folder)
            shutil.copytree(path, os.path.join(root_dir, needed_dir), dirs_exist_ok=True)
