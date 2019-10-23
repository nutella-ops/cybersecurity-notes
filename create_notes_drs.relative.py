#!/usr/bin/python3

import os
cwd = os.getcwd()
#print(cwd)
root = ("CyberSecurity-Notes")
sub_week = ("week_")
#sub_day = (sub_week + "day_")

os.path.join(cwd, root, sub_week)
#try:
    #os.mkdir(root)
    #for num in range(1,25):
        #os.mkdir(sub_week + str(num))
#except:
    #print("Directory:" + str(root) + " already exists, dummy.")
  
