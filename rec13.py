ERROR_CODE = 1
class Pointdata(object):
    '''
    This class is for plenty points in the universe.
    '''
    def __init__(self,valueOfX = 0,valueOfY = 0):
        self.valueOfX = valueOfX
        self.valueOfY = valueOfY

    def getValueOfX(self):
        return self.valueOfX

    def getValueOfY(self):
        return self.valueOfY

    def __str__(self):
        return "(%5f,%5f)"%(self.valueOfX, self.valueOfY)

    def expand(self,timesOfExpand=1):
        self.__valueOfX = self.__valueOfX * timesOfExpand
        self.__valueOfY = self.__valueOfY * timesOfExpand

    def __eq__(self,other):
        return self.__valueOfX == other.__valueOfX and self.__valueOfY == other.__valueOfY

class Quadrant(object):
    '''
    This class inclueds a set of points.
    '''
    def __init__(self,nameOfQuadrant):
        self.__nameOfQuadrant = nameOfQuadrant
        self.__listOfPoint = []

    def getNameOfQuadrant(self):
        return self.__nameOfQuadrant

    def addPoint(self,Point):
        if Point is not in self.__listOfPoint:
            self.__listOfPoint.append(str(Point))

    def __str__(self):
        return str(self.__listOfPoint = [])

class Line(object):
    '''
    This class defines verticle line.
    '''
    def __init__(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def __eq__(self,other):
        return self.__x == other.__x and self.__y == other.__y

    def __str__(self):
        return "(%5f,%5f;%5f,%5f)"%(self.__x1,self.__y1,self.__x2,self.__y2)

def openAndReadFile(filename):
    '''
    This function open the file and collect data.
    '''
    openfile = open(filename,"r")
    dataList=[]
    for lines in openfile:
        lst = lines.split()
        x = float(lst[0])
        y = float(lst[1])
        data = Pointdata(x,y)
        dataList.append(data)
    openfile.close()
    return dataList

def writePointIntoQuadrant(pointList,Quadrant):
    '''
    This function puts Point into Quadrant.
    '''
    for data in pointList:
        Quadrant.addPoint(data)

def writePointintoLine(pointList,Line):
    '''
    This function puts Point into Line if satisifies.
    '''
    lineList = []
    for data in pointList:
        pointList.remove(data)
        for newData in pointList:
            if data.getValueOfY == newData.getValueOfY:
                Line = Line(data.getValueOfX,data.getVauleOfY,newData.getValueOfX,newData.getValueOfY)
                lineList.append(Line)
    return lineList

def calDistantFromOrgin(pointList):
    '''
    This function calculate the distant from the point to orgin.
    '''
    resList = []
    for data in pointList:
        res = (data.getValueOfX**2+data.getValueOfY**2)**(1/2)
        resList.append(res)
    return resList

def writeLineIntoFile(nameOfFile,lineList):
    '''
    This function creats a file and write Line into it.
    '''
    openfile= open(filename,"w")
    for data in lineList:
        openfile.write(str(data)+"\n")
    openfile.close()
