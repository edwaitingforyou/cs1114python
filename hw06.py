#!C:\Python27\python.exe
'''
cs1114
Submission: hw06
Programmer: Beihong Chen
Username: bchen13
Purpose of program: This program takes two lists and returns a list of
those elements that both have in common.

The program always goes from top to bottom.
'''

def combineLists(lista,listb):
    '''
    This function is used to take
    two lists and returns a list of those
    elements that both have in common.
    '''

    newList = []
    for index in lista:
        while lista.count(index) > 1:
            lista.remove(index)
    for index in lista:
        if index in listb:
            newList.append(index)

    return newList

