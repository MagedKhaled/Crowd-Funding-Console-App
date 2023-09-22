
class Project:
    projectFolder = 'projects/'
    projectTitles = 'projects/__Titles__'
    def __init__(self,userID):
        self.projectTitles = self.getProjectTitles()
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
        with open(f"{self.__class__.projectFolder}/{self.title}",'a') as file:
            file.write(str(self.__dict__))
        
        with open(self.__class__.projectTitles,'a') as file:
            file.write(f"{self.userID}:{self.title}")

    @classmethod
    def getProjectTitles(cls):
        with open(cls.projectTitles,'r') as file:
            projects = file.readlines()
            print(projects)

    @classmethod
    def viewAll(cls):
        cls.getProjectTitles()
        pass







class ImportProject(Project):
    def __init__(self,title):
        with open(f'projects/{title}','r') as file:
            print(file.readline)



        















