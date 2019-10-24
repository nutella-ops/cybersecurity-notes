#!/usr/bin/python3

import os
current_dir = os.getcwd()

#function to make 24 week_dir
def sub_week():
    for enum in range(1,25):
        week_name = os.mkdir("week_" + str(enum))
        #return week_name
#function to make 3 day_dir
def sub_day():
    for enum in range(1,4):
        day_name = os.mkdir("day_" + str(enum))
        #return day_name

#name the filesystem
home_folder = ("CyberSecurity-Notes")
week = sub_week()
day = sub_day()
#try:
#function call to create sub_dirs
filesystem = os.path.join(current_dir, home_folder, str(week), str(day))
os.makedirs(filesystem)

#except:
#print("Directory:" + str(home_folder) + " already exists, dummy.")
  
