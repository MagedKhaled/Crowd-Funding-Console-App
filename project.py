import os
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

    def getDetails(self):
        self.details = self.__class__.getInp('Details')
        
    def getTarget(self):
        self.target = self.__class__.getInp('Target')

    def getStart(self):
        self.startTime = self.__class__.getInp('Start Time')
    
    def getEnd(self):
        self.endTime = self.__class__.getInp('End Time')

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
        
        cls.printOut('All Projects: ',projectsTitles)



    @classmethod
    def printOut(cls,massage,dataList):
        print(massage)

        
        for i in range(len(dataList)):
            print(f"{i+1})",end='')
            print(dataList[i])

    @classmethod
    def getProject(cls,projectTitle):
        with open(f"projects/{projectTitle}",'r') as file:
            project = file.readline()
            project = eval(project)
            return ImportProject(project)
        
    @classmethod
    def deleteProject(cls,projectToDelete):
        projectTitles = cls.getProjectTitles()
        with open(cls.projectTitles,'a') as file:
            for project in projectTitles:
                project = eval(project)
                if project['project'] == projectToDelete:
                    continue
                file.writelines(str(project)+"\n")
        
        os.remove(f"projects/{projectToDelete}")












class ImportProject(Project):
    def __init__(self,data):
        print(data)
        self.title = data['title']
        self.userID = data['userID']
        self.details = data['details']
        self.target = data['target']
        self.startTime = data['startTime']
        self.endTime = data['endTime']




        















