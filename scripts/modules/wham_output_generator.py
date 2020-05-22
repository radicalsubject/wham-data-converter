#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os

working_location = os.getcwd()
# os.chdir("../")
current_working_location = os.getcwd()
# print (current_working_location)


atom_list = ["Li", "Na", "K", "Cs", "Rb"]

for atom in atom_list:

##################################################################################################
# parameters #####################################################################################

    hist_min = 1.8
    hist_max = 8
    num_bins = 150
    tol = 0.01
    temperature = 300
    numpad = 0
    metadatafile = "../../%s/dist_out/metadata_%s_dist_out" % (atom, atom)
    freefile = "../../%s/dist_out/%s.out" % (atom, atom)
###################################################################################################
###################################################################################################
    terminal_command = 'cd ../wham/wham && ./wham %s %s %s %s %s %s %s %s' % (hist_min, hist_max, num_bins, tol, temperature, numpad, metadatafile, freefile)
    print (terminal_command)

    #чистим нычки: если в вашей фазе хода вы вытянули папку с файлом предыдущей версии, то удаляем его.
    if os.path.exists(os.getcwd() + "/%s/" % (atom) + "%s.out"):
        os.remove(os.getcwd() + "/%s/" % (atom) + "%s.out")
    
    os.system(terminal_command) # выполняем комманду в терминале запуская wham
    print ("\n Calculations for %s done. \n " % (atom))
    os.chdir(working_location)
#     print (os.getcwd())
    
    
# print ("ฅ(^・ﻌ・^)ฅ - miau, i love you!")

