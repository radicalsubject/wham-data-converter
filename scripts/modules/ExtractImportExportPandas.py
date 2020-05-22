#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os, sys
# Load the Pandas libraries with alias 'pd' 
import pandas as pd
import shutil
import platform

# working_location = "/home/oikura/Desktop/Yulia/scripts/"
working_location = os.getcwd()
current_working_location = os.chdir(working_location)
#system detection
# platform.system()
# print (working_location, "\n", os.listdir(".."), "\n", platform.system())

atom_list = ["Li", "Na", "K", "Cs", "Rb"]

######### big block for unpacking of archived data in Linux systems ####################################
########################################################################################################
########################################################################################################
def unpacking_linux (atom):
    if not os.path.exists("../%s/dist" % (atom)):
        zipped_files = os.listdir("../%s/" % (atom))
        for zipped_file in zipped_files:
            if zipped_file.find('.gz') != (-1):
                gunzip_command = "gunzip -kf ../%s/%s" % (atom, zipped_file) # forced overwrite key
                unzip_command = "unzip ../%s/%s -d ../%s" % (atom, zipped_file [:len(zipped_file)-3], atom)
                unpack_command = gunzip_command + " && " + unzip_command
                print (unpack_command)
                os.system (unpack_command)
            else:
                unzip_command = "unzip ../%s/%s -d ../%s" % (atom, zipped_file, atom)
                os.system (unzip_command)
    else:
        shutil.rmtree("../%s/dist" % (atom))
        zipped_files = os.listdir("../%s/" % (atom))
        for zipped_file in zipped_files:
            if zipped_file.find('.gz') != (-1):
                gunzip_command = "gunzip -kf ../%s/%s" % (atom, zipped_file) # forced overwrite key
                unzip_command = "unzip ../%s/%s -d ../%s" % (atom, zipped_file [:len(zipped_file)-3], atom)
                unpack_command = gunzip_command + " && " + unzip_command
#                 print (unpack_command)
                os.system(unpack_command)
            else:
                unzip_command = "unzip ../%s/%s -d ../%s" % (atom, zipped_file, atom)
                os.system (unzip_command)
####################################################################################################### 
####################################################################################################### 

def read_write_data (file_name):
    # Control delimiters, rows, column names with read_csv 
    data = pd.read_csv(current_working_location + "/" + file_name, sep='\s+', header=None) 
    data = data.dropna()
    del data[5], data[4], data[3], data[2] #удаление столбцов с нулями
    # print (data.head())
    data[1] = data[1].apply(lambda x: x*0.529177) #conversion of bohr radii to angstrom
    # formatting data to float
    data[1] = data[1].map('{:,.5f}'.format)
    data[0] = data[0].map('{:.8f}'.format)
    ###### конвертировать формат имени выходных файлов если необходимо:
    # l = len (file_name)-4 #определение длина файла в количестве символов минус расширение файла
    # file_name = file_name[:l] #укорачивание имени файла на .csv
    data.to_csv("../dist_out/" + file_name, sep="\t", header=None, index=False) #запись датафрейма в выходные файлы без хедера с разделителями-табуляцией
    
####################################################################################################### 
####################################################################################################### 
for atom in atom_list:
    unpacking_linux(atom)
    
    file_list = os.listdir("../%s/dist" % (atom))
    #file_list = os.listdir("/home/oikura/Downloads/Yulia/Cs/k8/")
    #print(file_list) 
    current_working_location = os.chdir("../%s/dist" % (atom))
    current_working_location = os.getcwd()
#     print(current_working_location, " converting......")
    
    if not os.path.exists("../dist_out/"):
        os.mkdir("../dist_out/")
        
    for file_name in file_list:
        read_write_data(file_name)
        
    #specially for Cs
    if atom == "Cs":
        if not os.path.exists("../k8_out/"):
            os.mkdir("../k8_out/")
        file_list = os.listdir("../k8")
        current_working_location = os.chdir("../k8")
        current_working_location = os.getcwd()
#         print(current_working_location, " converting k8......")
        
        for file_name in file_list:
        # Control delimiters, rows, column names with read_csv 
        # data = pd.read_csv("/home/oikura/Downloads/Yulia/Cs/k8/" + file_name, sep='\s+', header=None) 
            data = pd.read_csv(current_working_location + "/" + file_name, sep='\s+', header=None) 
            data.dropna(inplace= True)
            del data[5], data[4], data[3], data[2] #удаление столбцов с нулями

            # print (data.head())
            data[1] = data[1].apply(lambda x: x*0.529177) #conversion of bohr radii to angstrom

            # formatting data to float
            data[1] = data[1].map('{:,.5f}'.format)
            data[0] = data[0].map('{:.8f}'.format)

                ###### конвертировать формат имени выходных файлов если необходимо:
                # l = len (file_name)-4 #определение длина файла в количестве символов минус расширение файла
                # file_name = file_name[:l] #укорачивание имени файла на .csv
            data.to_csv("../k8_out/" + file_name, sep="\t", header=None, index=False) #запись датафрейма в выходные файлы без хедера с разделителями-табуляцией

    
    # возвращаем программу обратно в исходную директорию    
    current_working_location = os.chdir(working_location)
#     print ("\n Done! \n")
print ("Finished convertation for WHAM, see files in ..%s/dist_out directories.")
