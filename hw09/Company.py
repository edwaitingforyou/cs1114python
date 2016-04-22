from WorkerRec import WorkerRec
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
        workerName = WorkerRec(workerName,workerSSN,hoursRate)
        self.__workerList.append(workerName)

    def workerAddHour(self,workerSSN,numOfHour):
        '''
        This function adds the hour of working for a worker.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            self.__workerList[self.__findWorker(workerSSN)].addHours(numOfHour)

    def changeHourlyRate(self,workerSSN,newRate):
        '''
        This function changes the hour rate of a worker.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            self.__workerList[self.__findWorker(workerSSN)].changeHourRate(newRate)

    def fireWorker(self,workerSSN):
        '''
        This function fires workers.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
            name = self.__workerList[self.__findWorker(workerSSN)]
            filename = name.getNameOfWorker().strip()+"FINAL.txt"
            openfile = open(filename, "w")
            openfile.write(str(name.getSSNOfWorker())+"\n")
            openfile.write("%s $%.2f %s\n"%(name.getNameOfWorker(),name.getAmt(),name.getWorkerTitle()))
            self.__workerList.remove(self.__workerList[self.__findWorker(workerSSN)])

    def changeTitle(self,workerSSN,title):
        '''
        This function changes the title of worker.
        '''
        if self.__findWorker(workerSSN) != len(self.__workerList):
             self.__workerList[self.__findWorker(workerSSN)].changeWorkerTitle(title)

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

    def __findWorker(self,workerSSN):
        '''
        This function find the position of the worker in the list.
        If not find, it will return the length of the list.
        '''
        for index in range(len(self.__workerList)):
            if self.__workerList[index].getSSNOfWorker() == workerSSN:
                return index
        return len(self.__workerList)
