#!/usr/bin/python3
import os

#tell script which directory it is in
current_dir = os.getcwd()

#name the filetree
cyber_folder_name = ("CyberSecurity-Notes")

#define filetree location
cyber_home = os.path.join(current_dir, cyber_folder_name)

#define week_dir 
week_name = os.path.join(cyber_home, "week_")

#move to CyberSecurity-Notes dir & make 24 week folders
def sub_week():
    os.chdir(cyber_home) 
    for enum in range(1,25):
        week_name = os.mkdir("week_" + str(enum))
    
# iterate thru week_dir & make day_dir(3x) for each
def sub_day():
    for enum in range(1,25):
        os.chdir(week_name + str(enum))
        for enum in range(1,4):
            day_name = os.mkdir("day_" + str(enum))

#unecessary function to make entire filetree ;)
def boom():
    os.makedirs(cyber_home)
    sub_week()
    sub_day()


try:
    boom()

except:
   print("{"+ cyber_home +"}" + " already exists, mothafucka.")
