#!/usr/bin/python3
import os

#tell script which directory it is in
current_dir = os.getcwd()

#name the filetree
cyber_folder_name = ("CyberSecurity-Notes")

#function to make entire filetree
def cyber_filetree():
    #define filetree location
    cyber_dir = os.path.join(current_dir, cyber_folder_name)
    #start the filetree
    os.makedirs(cyber_dir)

#function to make 24 week_dir
def sub_week():
    #move to CyberSecurity-Notes dir & make 24 week folders
    os.chdir(cyber_dir) 
    for enum in range(1,25):
        week_name = os.mkdir("week_" + str(enum))
      
#function to make 3 day_dir
def sub_day():
    # move into each week folder and make 3 day folders inside
    for enum in range(1,25):
        os.chdir(week_name)
        for enum in range(1,4):
            day_name = os.mkdir("day_" + str(enum))

cyber_filetree()
sub_week
sub_day



#variable aliases for day & week functions
#week = sub_week()
#day = sub_day()

#try:

#except:
#print("Directory:" + str(cyber_folder_name) + " already exists, dummy.")
