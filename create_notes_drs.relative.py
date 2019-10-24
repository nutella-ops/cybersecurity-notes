#!/usr/bin/python3

import os
current_dir = os.getcwd()

#function to make 24 week_dir
#define sub_week():
    #for enum in range(1,25):
        #os.mkdir(week_+"enum")

#function to make 3 day_dir
#define sub_day():
    #for enum in range(1,4):
        #os.mkdir(day_+"enum")

#name the filesystem
home_name = ("CyberSecurity-Notes")

#function call to create sub_dirs
filesystem = os.path.join(current_dir, home_name, "week_","day_")
os.makedirs(filesystem)

#try:
    #os.mkdir(root)
    #for num in range(1,25):
        #os.mkdir(sub_week + str(num))
#except:
    ##print("Directory:" + str(root) + " already exists, dummy.")
  
