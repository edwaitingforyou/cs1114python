# -*- coding: cp936 -*-
#在改变每小时工资的时候，如果区别之前的工资以及之后的工资
class WorkerRec(object):
    '''
    This class includes SSN which uniquely identifies the worker
    hourly pay rate (there is no overtime)
    hours worked since last getting paid
    '''
    def __init__(self,workerName,workerSSN,hoursRate = float(17.22),hoursSinceLastPaid=0,workerTitle = ""):
        self.__workerSSN = workerSSN
        self.__workerName = workerName
        self.__hoursSinceLastPaid = hoursSinceLastPaid
        self.__hoursRate = hoursRate
        self.__workerTitle = workerTitle

    def getSSNOfWorker(self):
        '''
        This function returns the SSN of a worker.
        '''
        return self.__workerSSN

    def getHoursSinceLastPaid(self):
        '''
        This function returns the hours since the worker last has been paid.
        '''
        return self.__hoursSinceLastPaid

    def getNameOfWorker(self):
        '''
        This function returns the name of the worker.
        '''
        return self.__workerName

    def getHoursRate(self):
        '''
        This function returns the hours rate of a worker.
        '''
        return self.__hoursRate

    def getWorkerTitle(self):
        '''
        This funcion returns the title of a worker.
        '''
        return self.__workerTitle

    def getAmt(self):
        '''
        This function returns the amount of salary must be paid.
        '''
        return self.__hoursRate * self.__hoursSinceLastPaid

    def addHours(self,numOfHour):
        '''
        This function adds working hour to a worker.
        '''
        self.__hoursSinceLastPaid += numOfHour

    def clearHours(self):
        '''
        This function clears the number of hours since the worker has been paid.
        '''
        self.__hourSinceLastPaid = 0

    def changeHourRate(self,newRate):
        '''
        This function change the hours of rate of a worker.
        '''
        self.__hoursRate = newRate

    def changeWorkerTitle(self,newTitle):
        '''
        This function change the title of a worker.
        '''
        self.__workerTitle = "[%s]"%(newTitle)
        
    def __eq__(self,other):
        return self.__workerSSN == other.__workerSSN

    def __cmp__(self,other):
        if self.getAmt() > other.getAmt():
            return 1
        elif self.getAmt() < other.getAmt():
            return -1
        else:
            if self.__workerSSN > other.__workerSSN:
                return 1
            elif self.__workerSSN < other.__workerSSN:
                return -1

    def __str__(self):
        return self.__nameOfWorker
