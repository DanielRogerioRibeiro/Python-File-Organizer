import os
import shutil

# codigo para contar o numero de arquivos e pastas
def count_files_and_folders(folder_path, extension):
    num_files = 0
    num_folders = 0

    for item in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, item)) and item.endswith(extension):
            num_files += 1
        elif os.path.isdir(os.path.join(folder_path, item)):
            num_folders += 1
            sub_folder_path = os.path.join(folder_path, item)
            sub_num_files, sub_num_folders = count_files_and_folders(sub_folder_path, extension)
            num_files += sub_num_files
            num_folders += sub_num_folders

    return num_files, num_folders