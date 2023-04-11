import os
import shutil

# view codes ---------------------------

import os
import shutil

# code to count files and number of folders
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


# code to copy files
def copy_files(source,destination,ext):

     source_directory = source
     destination_directory = destination

     extension = ext

     for file_name in os.listdir(source_directory):
         if file_name.endswith(extension):
             source_path = os.path.join(source_directory, file_name)
             destination_path = os.path.join(destination_directory, file_name)
             shutil.copy(source_path, destination_path)



# Code to move files

def move_files_by_extension(source_folder, destination_folder, file_extension):
     if not os.path.exists(destination_folder):
         os.makedirs(destination_folder)

     for file_name in os.listdir(source_folder):
         if file_name.endswith(file_extension):
             file_path = os.path.join(source_folder, file_name)
             shutil.move(file_path, destination_folder)


# view codes End ---------------------------