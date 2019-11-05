#!/usr/bin/python3
import os

################################
#                              #
#    Find & Print files        #
#    containing string         #
#   `.pdf` extension in        #
#    working directory         #
#                              #
################################


#function setup
################################
def file_names():
    #current working directory
    current_dir = os.getcwd()

    #output formatting
    print("")

    #list avaliable files
    for root, dirs, files in os.walk(current_dir):
        for name in files:
            if name.find(".pdf") > -1:
                print(name)

    #output formatting
    print("")
################################



#instructions
################################

file_names = str(file_names())






