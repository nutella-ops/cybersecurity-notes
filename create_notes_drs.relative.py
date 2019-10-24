#!/usr/bin/python3

import os
cwd = os.getcwd()

#function to make 24 week_dir
define sub_week():
    for enum in range(1,25):
        os.mkdir(week_+"enum")

#function to make 3 day_dir
define sub_day():
    for enum in range(1,4):
        os.mkdir(day_+"enum")

#define master_dir
root = ("CyberSecurity-Notes")

#function call to create sub_dirs
notes_folder = os.path.join(cwd, root, "week_","day_")
os.makedirs(notes_folder)

#try:
    #os.mkdir(root)
    #for num in range(1,25):
        #os.mkdir(sub_week + str(num))
#except:
    #print("Directory:" + str(root) + " already exists, dummy.")
  
