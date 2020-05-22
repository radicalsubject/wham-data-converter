#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os, sys
import pandas as pd
import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
import numpy as np
import platform
import plotly.graph_objects as go
import scipy
from scipy import signal

# working_location = "/Users/gn-3/Desktop/WORK/IT/Yulia/scripts"
# current_working_location = os.chdir(working_location)
working_location = os.getcwd()
current_working_location = os.chdir(working_location)

#system detection
# platform.system()

# print (working_location, "\n", os.listdir("."), "\n", platform.system())

# import statsmodels.formula.api as smf
from scipy.interpolate import make_interp_spline, BSpline

fig = plt.figure(figsize = (40,18))
ax = plt.subplot(111)

###### какой атом анализируем?###############################################################################
atom_list = ["Li", "Na", "K", "Cs", "Rb"]
counter = 0
colours = ["red", "green", "blue", "black", "purple"]
for atom in atom_list:
#############################################################################################################

    current_working_location = os.chdir("../%s/dist_out" % (atom)) # перемещение процесса в локацию не нужно и дает ошибку когда работаешь с относительными путями
    current_working_location = os.getcwd()
#     print(working_location)

    #read wham output data
    data = pd.read_csv(current_working_location + "/%s.out" % (atom), sep='\s+') # без header=None так как хочу обращаться к столбцам по легенде

    #чистим данные от NaN
    data = data.fillna(0) #заполняем нулями отсутствующие данные NaN
    indexNaN = data['Prob'] == 0 #получаем датафрейм в котором в столбце Prob нули
    index_drop_NaN = data[indexNaN].index #получаем индексы строк, которые надо дропнуть
    data.drop(index_drop_NaN, inplace=True) #дропаем
    # print (data) #просмотр полученного фрейма

    graph_df = pd.DataFrame({"x, Coor": data ["#Coor"], 'y, Free': data ["Free"]}) #creating array for plotting
#     print (graph_df)
    graph_df.to_csv("../%s.csv" % (atom), sep="\t", header=None, index=False) #запись датафрейма в выходные файлы без хедера с разделителями-табуляцией
    graph_df=graph_df.astype(float)

######сглаживание линейными сплайнами ############################################################################33
    # вытаскиваем из датафрейма листы с переменными которые будем фиттить
    x = graph_df ["x, Coor"].to_list()
    y = graph_df ["y, Free"].to_list()
    #  print (x, y)
#     fitted_data = pd.DataFrame(columns=['y', 'x'])
#     fitted_data['x'] = x
#     fitted_data['y'] = y

## 300 represents number of points to make between T.min and T.max
    xnew = np.linspace(np.array(x).min(), np.array(x).max(), 250) 
## сглаживание кривой
# кубические сплайны
    y1_smooth = scipy.interpolate.interp1d(x,y, kind = 'cubic')
    plt.plot(xnew, y1_smooth(xnew), linewidth = 3, label = atom)
    
#     h = signal.get_window('triang', 60)
#     fil = signal.convolve(x, h / h.sum())
#     fig, ax = plt.subplots(1, 1, figsize=(6, 4))
#     plt.plot(y, fil[:len(x)], '-w', lw=2)
    
#     y2_smooth = scipy.interpolate.interp1d(x,y, kind = 'nearest')
#     plt.plot(xnew, y2_smooth(xnew), linewidth = 0.8, label = 'nearest')
    
#     y3_smooth = scipy.interpolate.interp1d(x,y, kind = 'linear')
#     plt.plot(xnew, y3_smooth(xnew), linewidth = 0.8, label = 'linear')

#     graph_df.plot(kind='scatter',x='x, Coor',y='y, Free', color=colours [counter], ax=ax, label=atom)
#     graph_df.plot(x='x, Coor',y='y, Free', color=colours [counter], ax=ax, label='')

    
    counter = counter + 1
    # показать график
    ax.legend()
    ax.grid(True)
    current_working_location = os.chdir("../")
current_working_location = os.chdir("../scripts")
plt.show()