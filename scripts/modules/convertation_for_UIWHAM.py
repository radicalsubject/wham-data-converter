#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, sys
import pandas as pd
import shutil

working_location = os.chdir("/home/oikura/Desktop/Yulia/scripts/")

working_location = os.getcwd()
current_working_location = os.chdir(working_location)
# print (working_location)

atom_list = ["Li", "Na", "K", "Cs", "Rb"]

for atom in atom_list:
    
    # создаем массивы с данными
    file_path = []
    k = []
    loc_win_min = []

    
    if not os.path.exists("../%s/uiwham" % (atom)):
        os.mkdir("../%s/uiwham" % (atom))
    else:
        shutil.rmtree("../%s/uiwham" % (atom))
        os.mkdir("../%s/uiwham" % (atom))
    source_file_list = os.listdir("../%s/dist" % (atom))
    
    current_working_location = os.chdir("../%s/dist" % (atom))
    current_working_location = os.getcwd()
    print(current_working_location, " converting......")
    counter = 0
    for file_name in source_file_list:
        data = pd.read_csv(current_working_location + "/" + file_name, sep='\s+', header=None)
#         print (file_name)
           
        end = file_name.find('_dist')
        start = file_name.find('usk') + 3
        s = file_name[start:end] # обрезаем ненужное в имени файла
        s = s[:4]
#         print (file_name)
#         print (s)
        k.append("{:.2f}".format(int(s.split("d") [0])*2)) # набиваем массив константами жесткости приложенного потенциала (k)
        loc_win_min.append("{:.2f}".format(int(s.split("d") [1])*(0.1)/0.529177)) # набиваем массив положение минимума приложенного квадратичного потенциала (x 0 )

#         print (file_path, k, loc_win_min)    

        new_data = pd.DataFrame({"RC_Value": data [1]})
        new_data['force-constant'] = k [counter]
        new_data['RC-reference-value'] = loc_win_min[counter]
        new_data=new_data.astype(float)

#         print (new_data)
        os.chdir(working_location)
        new_data.to_csv("../%s/uiwham/" % (atom) + file_name, sep="\t", header = None, index=False)
        counter = counter + 1
        
print ("UIWHAM convertation done.")



