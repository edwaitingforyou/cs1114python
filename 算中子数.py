#!C:\Pyhthon27\python.exe
# -*- coding: cp936 -*-
#林鸽我给你跪下了
import os
print "This is the program to caculate the number of proton number for some really stupid primary school guys."
num_protons = int(raw_input('The proton [atmoic] number is : '))
print "The proton [atomic] number is", num_protons
num_mass = int(raw_input('The mass number is : '))
print "The mass number is", num_mass
num_neutrons = num_mass - num_protons
print "The neutron number of the element is", num_neutrons
print "哈哈哈你现在你可以碾压美国人了。"
os.system("pause")
