#!/usr/bin/python3

import os
cwd = os.getcwd()
print(cwd)

root = ("CyberSecurity-Notes")

notes_folder = os.path.join(cwd, root, "week_","day_")

os.makedirs(notes_folder)

#try:
    #os.mkdir(root)
    #for num in range(1,25):
        #os.mkdir(sub_week + str(num))
#except:
    #print("Directory:" + str(root) + " already exists, dummy.")
  
