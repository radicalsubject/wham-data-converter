#!/usr/bin/env python
# coding: utf-8

# In[39]:


import os, sys
working_location = os.chdir("/home/oikura/Desktop/synchronization/WORK/IT/Yulia/scripts")
# listing directories
# print ("The dir is: %s" %os.listdir(os.getcwd())) /home/oikura/Downloads/Yulia
atom_list = ["Li", "Na", "K", "Cs", "Rb"]

for atom in atom_list:
    file_list = os.listdir("../%s/dist" % (atom))
#     print(file_list) 

    working_location = os.chdir("/home/oikura/Desktop/synchronization/WORK/IT/Yulia/%s/dist" % (atom))
    working_location = os.getcwd()
#     print(working_location)
    for file_name in file_list:
        if not file_name.find('.csv') == (-1):
            new_name = file_name [:len(file_name)-4]
            os.rename(file_name, new_name)
##         os.rename(file_name, file_name + ".csv")

    file_list = os.listdir("./")
#     print(file_list)
    working_location = os.chdir("/home/oikura/Desktop/synchronization/WORK/IT/Yulia/scripts")
