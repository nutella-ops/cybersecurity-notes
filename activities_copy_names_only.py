#!/usr/bin/python3
import os

################################
#                              #
#    Find & Print files        #
#    containing string         #
#    `Activities` in           #
#    working directory         #
#                              #
################################

def file_names():
    #current working directory
    current_dir = os.getcwd()
    
#remote directory
    remote_dir = os.path.join("/","root","Downloads","UCLArepo")

    #output formatting
    print("")

    #list avaliable files
    for root, dirs, files in os.walk(remote_dir):
        for name in dirs:
            if name.find("Activities") > -1:
                print(files)

    #output formatting
    print("")

file_names = str(file_names())
