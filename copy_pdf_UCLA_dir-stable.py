#!/usr/bin/python3
import os, shutil

################################
#                              #
#    Find & Print files        #
#    containing string         #
#   `.pdf` extension in        #
#    working directory         #
#                              #
################################


#function to find .pdf files in UCLArepo
################################
def file_names():


    #remote directory
    remote_dir = os.path.join("/","root","Downloads","UCLArepo")

    #list avaliable files
    for root, dirs, files in os.walk(remote_dir):
        for name in root, dirs, files:
            print(name)
            
            #if name.find(".pdf") > -1:
                #return os.path.join(name)

##################################



#instructions
##################################
#current working directory
current_dir = os.getcwd()

#variableize function
file_names = str(file_names())

#copy files from UCLArepo to current directory
shutil.copy(file_names, current_dir)
