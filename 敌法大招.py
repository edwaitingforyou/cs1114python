#!C:/Python27/python.exe
# -*- coding: cp936 -*-
#��ʵ����̫�����������Ҿ�д����������档
#�������������з�һ���������������ġ�
#���뼸���򵥵����־Ϳ���֪����

import os
print "Let's start!"
level_am = int(raw_input('The level of AM skill is: '))
print "Now AM has", level_am, "level C"
your_hp = int(raw_input('Enter your HP : '))
print "You now have", your_hp, "HP"
your_tmp = int(raw_input('Enter your present MP : '))
your_nmp = int(raw_input('Enter your total MP : '))
print "Your MP is", your_tmp, "/", your_nmp
if level_am == 1:
    damage_v = 0.7*0.75*your_nmp - 0.7*0.75*your_tmp
    print "The damage will be", damage_v
elif level_am == 2:
    damage_v = 0.9*0.75*your_nmp - 0.9*0.75*your_tmp
    print "The damage will be", damage_v
elif level_am == 3:
    damage_v = 1.2*0.75*your_nmp - 1.2*0.75*your_tmp
    print "The damage will be", damage_v
if damage_v < your_hp:
    print "Your are survived!"
    os.system("pause")
elif damage_v > your_hp:
    print "Haha, you will die!"
    os.system("pause")
elif damage_v == your_hp:
    print "Haha, you will die!"
    os.system("pause")

print "Have a nice game!"
