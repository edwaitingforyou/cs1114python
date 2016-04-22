class HydroCarbon:
    '''
    This class makes hydrocarbons.
    '''
    def __init__(self,numOfH,numOfC,nameOfHydroCarbon = ""):
        self.__numOfH = numOfH
        self.__numOfC = numOfC
        self.__nameOfHydroCarbon = nameOfHydroCarbon

    def getNumberOfC(self):
        '''
        This functio  returns the number of carbon.
        '''
        return self.__numOfC

    def getNumberOfH(self):
        '''
        This function returns the number of hydrogen.
        '''
        return self.__numOfH

    def getNameOfHydroCarbon(self,nameOfHydroCarbon):
        '''
        Tis fucntion returns the name of hyrdocarbon.
        '''
        self.__nameOfHydroCarbon = nameOfHydroCarbon

    def __str__(self):
        '''
        This fucntion returns a string which will be
        printed on the screen.
        '''

        return "C%iH%i\n\t\t%s" %(self.__numOfC,self.__numOfH,self.__nameOfHydroCarbon)
    def __eq__(self,other):
        '''
        This function compare two items
        '''

        return self.__numOfH == other.__numOfH and self.__numOfC == other.__numOfC

    def __cmp__(self,other):

        if self.__numOfC > other.__numOfC:
            return 1
        elif self.numOfC == other.__numOfC and self.numOfH == other.__numOfH:
            return 0
        else:
            return -1
        
def addOneIntoList(listOfHydroCarbon,hydroCarbonMolecule):
    '''
    This function add one hydrocarbon into the total list
    '''
    listOfHydroCarbon.append(hydroCarbonMolecule)

def openAndRead(nameOfFile):
    hydrocarbonfile = open(nameOfFile,"r")
    line = hydrocarbonfile.readline()
    
def creatObjectFromLine(line):
    '''
    This function reads the hydrocarbon in line of a file
    and returns a molecule object.
    '''

    newLine = line.strip("\n")
    listLine = newLine.split()
    nameOfHC = listLine[0]
    formulaOfHC = listLine[1]
    numOfH = formulaOfHC[1:formulaOfHC.find("H")]
    numOfC = formulaOfHC[(formulaOfHC.find("H")+1):(len(formulaOfHC)+1)]
    objectOfHydroCarbon = [numOfH, numOfC, nameOfHC]
    hydrocarbonfile.close()
    return objectOfHydroCarbon
