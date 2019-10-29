#!/usr/bin/python3
import os
import shutil

###########################
#                         #
#    COPY ACTIVITIES      #
#                         #
###########################

#tell script which directory it is in
current_dir = os.getcwd()

#define the search_path
search_path = os.path.join("/","home","higg","Documents")

#loop thru search_path & construct file_paths
for root, dirs, files in os.walk(search_path):
    for name in files:
        current_path = os.path.join(root, name)
        print(str(current_path))
