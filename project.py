import os
from validation import IsValid
from datetime import datetime
class Project:
    projectFolder = 'projects/'
    projectTitles = 'projects/__Titles__'
    def __init__(self,userID):
        self.userID=userID
        self.getTitle()
        self.getDetails()
        self.getTarget()
        self.getStart()
        self.getEnd()
        self.saveProject()

    @classmethod
    def getInp(cls,inpName,required=False):
        os.system('clear')
        if required:
            inp = input(f"Enter Your Project's {inpName}: ")
            while True: 
                
                if inp :
                    return inp
                print(f"The {inpName} of your Project is required!")
                inp = input(f"Enter Your Project's {inpName}: ")
        else:
            return input(f"Enter Your Project's {inpName}: ")


    def getTitle(self):
        self.title = self.__class__.getInp('Title',True)
        valid = IsValid.isValid('title',self.title,unique=True,exception='title')
        if valid :
            if valid == 'exist':
                input('The project title is exist ')
                self.getTitle()
            else:
                return 
        else:
            
            input('Invalid input, press enter to continue ')
            self.getTitle()



    def getDetails(self):
    
        self.details = self.__class__.getInp('Details')
        if len(self.details) > 1000:
            input("you can't write more than 1000 character, press enter to continue  ")
            self.getDetails()
        else:
            return
        
    def getTarget(self):

        self.target = self.__class__.getInp('Target in EGP')
        if IsValid.isValid('number',self.target):
            return
        else:
            input('Target must be number, press enter to continue ')
            self.getTarget()

    def getStart(self):
        self.startTime = self.__class__.getInp('Start Time')
        if IsValid.isValid('date',self.startTime):
            return
        else:
            input('Start date must be like 23-1-2023, press enter to continue  ')
            self.getStart()
    
    def getEnd(self):
        self.endTime = self.__class__.getInp('End Time')
        if IsValid.isValid('date',self.endTime):
            startTime = datetime.strptime(self.startTime, "%d-%m-%Y")
            endTime = datetime.strptime(self.endTime, "%d-%m-%Y")
            if startTime > endTime:
                print("End Time can't be lower than start time")
                inp = input("press enter to retry or 'q' to enter start time again: ")
                if inp.lower() == 'q':
                    self.getStart()
                self.getEnd()
            return
        else:
            input('End date must be like 23-1-2023, press enter to continue  ')
            self.getEnd()

    def saveProject(self):
        with open(f"{self.__class__.projectFolder}/{self.title}",'w') as file:
            file.write(str(self.__dict__)+"\n")
        
        with open(self.__class__.projectTitles,'a') as file:
            myDict = {'user':self.userID,'project':self.title}
            file.writelines(str(myDict)+"\n")

    @classmethod
    def getProjectTitles(cls):
        with open(cls.projectTitles,'r') as file:
            projects = file.readlines()
        return projects

    @classmethod
    def viewAll(cls):
        projects = cls.getProjectTitles()


        projectsTitles = []
        for project in projects:
            project = eval(project)
            projectsTitles.append(project['project'])
        
        print('All Projects: ')
        for i in range(len(projectsTitles)):
            print(f"{i+1})",end='')
            print(projectsTitles[i])   
        return projectsTitles    

    @classmethod
    def getProject(cls,projectTitle):
        with open(f"projects/{projectTitle}",'r') as file:
            project = file.readline()
            project = eval(project)
            return ImportProject(project)
        
    @classmethod
    def deleteProject(cls,projectToDelete):
        projectTitles = cls.getProjectTitles()
        with open(cls.projectTitles,'w') as file:
            for project in projectTitles:
                project = eval(project)
                if project['project'] == projectToDelete:
                    continue
                file.writelines(str(project)+"\n")
        
        os.remove(f"projects/{projectToDelete}")












class ImportProject(Project):
    def __init__(self,data):
        self.title = data['title']
        self.userID = data['userID']
        self.details = data['details']
        self.target = data['target']
        self.startTime = data['startTime']
        self.endTime = data['endTime']




        















