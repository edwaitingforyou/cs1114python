#!C:\Python27\python.exe

'''
cs1114

Submission: hw09

Programmer: Beihong Chen
Username: bchen13

This program creats two classes for a company deal with workers.
Also contains a tester for these two classes.

Constratints:
The output is always displayed from left to right and from top to bottom.
'''

DUPL_WORKER_ERROR = 1
NOT_FOUND_ERROR = 2
HOUR_NUM_ERROR = 3
RATE_AMT_ERROR = 4

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
        if numOfHour >0:
            self.__hoursSinceLastPaid += numOfHour
        else:
            return HOUR_NUM_ERROR   

    def clearHours(self):
        '''
        This function clears the number of hours since the worker has been paid.
        '''
        self.__hourSinceLastPaid = 0

    def changeHourRate(self,newRate):
        '''
        This function change the hours of rate of a worker.
        '''
        if newRate <= 0:
            return RATE_AMT_ERROR
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

class Company(object):
    '''
    This class will use the WorkerRec class and has done
    her consulting with the person who will buy here type
    definition for Company.
    hire a worker
    add hours to the hours worked for any worker
    change the hourly rate for a specific worker
    grant a title to a specific worker 
    pay all the workers
    '''
    def __init__(self,nameOfCompany):
        self.__nameOfCompany = nameOfCompany
        self.__workerList = []

    def getName(self):
        ''' 
        This function gets name of company.
        '''
        return self.__nameOfCompany

    def addWorker(self,workerName,workerSSN,hoursRate):
        '''
        This function hires worker to the company.
        '''  
        worker = WorkerRec(workerName,workerSSN,hoursRate)
        if self.__findWorker(workerSSN) != len(self.__workerList):
            return DUPL_WORKER_ERROR
        self.__workerList.append(worker)

    def __findWorker(self,workerSSN):
        '''
        This function find the position of the worker in the list.
        If not find, it will return the length of the list.
        '''
        for index in range(len(self.__workerList)):
            if self.__workerList[index].getSSNOfWorker() == workerSSN:
                return index
        return len(self.__workerList)

    def workerAddHour(self,workerSSN,numOfHour):
        '''
        This function adds the hour of working for a worker.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            status = self.__workerList[self.__findWorker(workerSSN)].addHours(numOfHour)
            if status == HOUR_NUM_ERROR:
                return HOUR_NUM_ERROR
        else:
            return status
        
    def changeHourlyRate(self,workerSSN,newRate):
        '''
        This function changes the hour rate of a worker.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            status = self.__workerList[self.__findWorker(workerSSN)].changeHourRate(newRate)
            if status == RATE_AMT_ERROR:
                return status
        else:
            return NOT_FOUND_ERROR
    
    def fireWorker(self,workerSSN):
        '''
        This function fires workers.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            name = self.__workerList[self.__findWorker(workerSSN)]
            filename = name.getNameOfWorker().replace(" ","")+"FINAL.txt"
            openfile = open(filename, "w")
            openfile.write(str(name.getSSNOfWorker())+"\n")
            openfile.write("%s $%.2f %s\n"%(name.getNameOfWorker(),name.getAmt(),name.getWorkerTitle()))
            self.__workerList.remove(self.__workerList[self.__findWorker(workerSSN)])
        else:
            return NOT_FOUND_ERROR
    
    def changeTitle(self,workerSSN,title):
        '''
        This function changes the title of worker.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            self.__workerList[self.__findWorker(workerSSN)].changeWorkerTitle(title)
        else:
            return NOT_FOUND_ERROR
        
    def payWorkers(self,filename):
        '''
        This function pays the salary to all workers and clear the
        number of hours since last been paid.
        '''
        openfile = open(filename,"w")
        self.__workerList.sort()
        for workers in self.__workerList:
            openfile.write(str(workers.getSSNOfWorker())+"\n")
            openfile.write("%s $%.2f %s\n"%(workers.getNameOfWorker(),workers.getAmt(),workers.getWorkerTitle()))
        for workers in self.__workerList:
            workers.clearHours()
        openfile.close()


def main():
    company = Company("John and co")
    status = company.addWorker("Sally Jones",443882354,35.22)
    if status == DUPL_WORKER_ERROR:
        print "The worker is already in the company."
        
    status = company.addWorker("Joe Smith",283728992,25.34)
    if status == DUPL_WORKER_ERROR:
        print "The worker is already in the company."
        
    status = company.workerAddHour(443882354,11)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."
        
    status = company.workerAddHour(283728992,9)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."
        
    status = company.workerAddHour(443882354,3)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."
        
    company.payWorkers("rec01.txt")
    status = company.workerAddHour(283728992,10)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."
        
    status = company.addWorker("Ralphael",248339271,26.39)
    if status == DUPL_WORKER_ERROR:
        print "The worker is already in the company."
    status = company.workerAddHour(283728992,4)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."
    status = company.changeTitle(443882354,"Master Snake Handler")
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."

    status = company.changeHourlyRate(283728992,15.5)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == RATE_AMT_ERROR:
        print "The rate changed is wrong."
    
    status = company.workerAddHour(443882354,7)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."

    company.payWorkers("rec02.txt")

    status = company.workerAddHour(283728992,9)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."

    status = company.workerAddHour(248339271,4)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."

    status = company.fireWorker(283728992)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
        
    status = company.changeHourlyRate(248339271,26.41)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == RATE_AMT_ERROR:
        print "The rate changed is wrong."
    
    status = company.workerAddHour(248339271,18)
    if status == NOT_FOUND_ERROR:
        print "The worker is not founded."
    elif status == HOUR_NUM_ERROR:
        print "The hour adding is wrong."
    company.payWorkers("rec03.txt")

if __name__ == "__main__":
    main()
