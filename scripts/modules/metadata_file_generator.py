#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os, sys
# Load the Pandas libraries with alias 'pd' 
import pandas as pd

# working_location = "/home/oikura/Desktop/Yulia/scripts/"
working_location = os.getcwd()
current_working_location = os.chdir(working_location)
# print (working_location)

# какой атом анализируем? изменить это
atom_list = ["Li", "Na", "K", "Cs", "Rb"]

for atom in atom_list:
    current_working_location = os.chdir("../%s/dist_out" % (atom)) #перемещаемся в папку
    current_working_location = os.getcwd()
    # print(current_working_location)

    # создаем массивы с данными
    file_path = []
    k = []
    loc_win_min = []

    # генерируем имя выходного файла по шаблону
    name_prefix = os.getcwd()
    name_prefix = name_prefix.split("/")
    l = len (name_prefix)
    name_prefix = name_prefix[l-2] + "_" + name_prefix[l-1]
#     print ("output metadata file is here:" + os.getcwd(), "metadata_" + name_prefix)

    #чистим нычки: если в вашей фазе хода вы вытянули папку с файлом метаданных предыдущей версии, то удаляем ёё.
    if os.path.exists(os.getcwd() + "/metadata_" + name_prefix):
        os.remove(os.getcwd() + "/metadata_" + name_prefix)
    #чистим нычки: если в вашей фазе хода вы вытянули папку с выходы wham предыдущей версии, то удаляем ёё.
    if os.path.exists(os.getcwd() + "/%s.out" % (atom)):
        os.remove(os.getcwd() + "/%s.out" % (atom))


    file_list = os.listdir(current_working_location) # list of files in directory

    # начинаем бегать по файлам
    for file_name in file_list:
        file_path.append(current_working_location + "/" + file_name) # набиваем массив путями

        end = file_name.find('_dist')
        start = file_name.find('usk') + 3
        s = file_name[start:end] # обрезаем ненужное в имени файла
        s = s[:4]
#         print (file_name)
#         print (s)
        k.append("{:.2f}".format(int(s.split("d") [0])*2)) # набиваем массив константами жесткости приложенного потенциала (k)
        loc_win_min.append("{:.2f}".format(int(s.split("d") [1])*(0.1))) # набиваем массив положение минимума приложенного квадратичного потенциала (x 0 )

    # print (file_path, k, loc_win_min)    

    # пишем массивы в датафрейм
    data = {"file_path": file_path, 
            "loc_win_min":loc_win_min,
            "k": k
           }

    df = pd.DataFrame(data)
    # print (df.head())

    df.to_csv(os.getcwd() + "/metadata_" + name_prefix, sep="\t", header=None, index=False) #запись датафрейма в выходные файлы без хедера с разделителями-табуляцией
#     print ("ฅ(^・ﻌ・^)ฅ - miau, i love you!")
    current_working_location = os.chdir(working_location)