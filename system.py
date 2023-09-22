# System class located to manage the flow of the program and the connection between Account class and project class




from account import Account
from project import Project,ImportProject
from validation import IsValid
from datetime import datetime
import os

class System:
    def __init__(self):
        self.Debug = False #just for debugging if true will pass the sign in operation

    def startSystem(self): #Say Hello 
        os.system('clear')
        print("*************************************************")
        print("*************************************************")
        print("**************Welcome in My Project**************")
        print("*************************************************")
        print("*************************************************\n\n")
        input("Press Enter to continue ")
        self.loggingScreen()


    def loggingScreen(self): #login-signup screen
        os.system('clear')
        print("1)Login")
        print("2)Signup")
        print("0)Exit")
        inp = input("Enter Your Choice: ")

        switcher = {
            '1': self.userLogin,
            '2': self.userSignup,
            '0': self.sysExit
        }

        if not (inp in switcher):#wrong input
            print("Invalid Input")
            input('press enter to continue ')
            self.loggingScreen()
        else:
            switcher[inp]()


    def projectScreen(self):#user screen after logging
        os.system('clear')
        print("1)Create Project")
        print("2)All Projects")
        print("3)Edit Project")
        print("4)Delete Project")
        print("5)Find Project")
        print("0)Logout")

        inp = input("Enter Your Choice: ")
        switcher = {
            '1': self.createProject,
            '2': self.viewProjects,
            '3': self.editProject,
            '4': self.deleteProject,
            '5': self.findProject,
            '0': self.userLogout
        }

        if not (inp in switcher):#wrong choice
            print("Invalid Input")
            input('press enter to continue')
            self.startSystem()
        else:
            switcher[inp]()

    


    def userLogin(self):#login
        os.system('clear')
        self.user = Account.login(Debug=self.Debug) #saving which user is logged 
        input(f"Welcome {self.user.name}, press Enter to continue ")
        self.projectScreen()
    
    def userSignup(self):#signup
        os.system('clear')
        Account()#The init function in Account make new user
        input("Your Account created successfully, press Enter to continue ")
        self.loggingScreen()

    def userLogout(self):#logout
        self.user = None
        self.loggingScreen()

    def createProject(self):#create new project
        os.system('clear')
        self.user.createProject()
        input("Your project created successfully, press enter to continue")
        self.projectScreen()

    def viewProjects(self):#view projects titles then you can choose project for other details
        os.system('clear')
        projectTitles = Project.viewAll()#returns data like [{'userID':'maged','project':'magedProject'}]
        print("0)Exit")
        inp = input("Choose a project to view: ")
        
        switcher = {
            str(i+1):projectTitles[i] for i in range(len(projectTitles))
        }
        if inp in switcher:
            project = Project.getProject(switcher[inp])
        elif inp == '0':
            self.projectScreen()
        else:
            input("Invalid input, press enter to try again")
            self.viewProjects()
        os.system('clear')
        for key,value in project.__dict__.items():#show details of the project you selected
            print(f"{key}: {value}")
        input('Press Enter to continue ')

        self.projectScreen()


    def chooseProject(self):#helpful function to make menu of projects to choose from 
        os.system('clear')
        self.user.getMyProjects()
        userProjects = self.user.projects
        print("Your available projects: ")
        for i in range(len(userProjects)):
            print(f"{i+1}){userProjects[i]}")
        print("0)Exit")

        
        inp = input("Enter Your Choice: ")
        switcher = {
            str(i+1): userProjects[i] for i in range(len(userProjects))
        }

        if inp == '0':
            self.projectScreen()
            
        elif not (inp in switcher):
            print("Invalid Input")
            input('press enter to continue')
            self.chooseProject()
        
        else:
            project = Project.getProject(switcher[inp])#function takes project's title and returns a project object
            return project 
 
    def editProject(self,_=None):#make edit on selected project
        project = self.chooseProject()
        if project :
            self.editProjectStage2(project)

    def editProjectStage2(self,project):#menu for available methods to edit on a project
        os.system('clear')
        switcher = {}
        print("1)Title")
        print("2)Details")
        print("3)Target")
        print("4)Start Date")
        print("5)End Date")
        print("0)Exit")


        switcher = {
            "1":self.getTitle,
            "2":self.getDetails,
            "3":self.getTarget,
            "4":self.getStart,
            "5":self.getEnd,
            "6":self.chooseProject,
            "0":self.editProject
        }
        

        inp = input("Enter The field to Edit: ")
        if not (inp in switcher):
            print("Invalid Input")
            input('press enter to continue')
            self.editProjectStage2()
        else:
            switcher[inp](project)
            project.saveProject()#save project on file


    def getTitle(self,project):#edit title
        os.system('clear')
        oldTitle = project.title
        project.getTitle()
        state = IsValid.isValid('title',project.title,unique=True,exception='title')
        if state == 'exist':
            input("This title is exist, press enter to continue")
            project.title = oldTitle
            self.getTitle(project)
        elif not state:
            input("Invalid Input, press enter to try again")
            project.title = oldTitle
            self.getTitle()
        project = ImportProject(project.__dict__)
        Project.deleteProject(oldTitle)
        project.saveProject()
        
        input(f"Project's title updated to {project.title}, Press Enter to continue")
        self.editProjectStage2(project)


    def getDetails(self,project):#edit details
        os.system('clear')
        project.getDetails()
        input(f"Project's details updated to {project.details}, Press Enter to continue")
        self.editProjectStage2(project)

    def getTarget(self,project):#edit target
        os.system('clear')
        project.getTarget()
        input(f"Project's target updated to {project.target}, Press Enter to continue")
        self.editProjectStage2(project)

    def getStart(self,project):#edit start time
        os.system('clear')
        project.getStart()
        input(f"Project's start date updated to {project.startTime}, Press Enter to continue")
        self.editProjectStage2(project)

    def getEnd(self,project):#edit end time
        os.system('clear')
        project.getEnd()
        input(f"Project's end date updated to {project.endTime}, Press Enter to continue")
        self.editProjectStage2(project)

    def deleteProject(self):#delete a project
        project = self.chooseProject()
        inp = input(f"You Will delete {project.title} project, press 'yes' to continue: ")
        if inp.lower() == 'yes':
            title = project.title
            Project.deleteProject(project.title)
            input(f"The project {title} deleted successfully, press enter to continue")
            self.projectScreen()
        else:
            input("Delete process is canceled, press enter to continue ")
            self.projectScreen()
        
    
    def findProject(self):#search on a project by [title,target<>=,Time>>shows all projects opens in a specific time(start<time<end)]
        os.system('clear')
        print("Available search methods:\n")
        print("1)Title")
        print("2)Target")
        print("3)Available Projects in specific Time")
        print("0)Exit")

        inp = input("Enter your choice: ")
        switcher = {
            "1":self.findTitle,
            "2":self.findTarget,
            "3":self.findTime,
            "0":self.projectScreen
        }

        if inp in switcher:
            switcher[inp]()
        else:
            input("Invalid Choice, press enter to try again ")
            self.findProject()

        

    def findTitle(self):#search on title
        os.system('clear')
        inp = input("Enter the title of the project: ")
        projectTitles = Project.getProjectTitles()
        titles = []
        for title in projectTitles:
            titles.append(eval(title)['project'])
            
        if inp in titles:
            
            
            project = Project.getProject(inp)
            for key,value in project.__dict__.items():
                print(f"{key}: {value}")
            input("Press enter to continue")
            self.findProject()
        else:
            inp = input(f"There are no project with the title '{inp}', press enter to continue or q to quit")
            if inp.lower() == 'q':
                self.findProject()
            else:
                self.findTitle()

    def findTarget(self):#search on target
        os.system('clear')
        inp = input("Enter the Target of the project: ")
        if not IsValid.isValid('number',inp):
            input("Invalid Number!,press enter to continue")
            self.findTarget()
        
        operation = input("Enter the operation(<,>,=)")
        if not operation in ['<','>','=']:
            input("Invalid Operation!,press enter to continue")
            self.findTarget()
        
        projectTitles = Project.getProjectTitles()
        titles = []
        for title in projectTitles:
            titles.append(eval(title)['project'])
            
        projects = []
        for project in titles:
            myProject = Project.getProject(project)
            if operation == '=':
                if int(myProject.target) == int(inp):
                    projects.append(myProject)
            elif operation == '>':
                if int(myProject.target) > int(inp):
                    projects.append(myProject)
            elif operation == '<':
                if int(myProject.target) < int(inp):
                    projects.append(myProject)
        self.availableProjects(projects)

    def availableProjects(self,projects):#helpful function to make menu of projects that achieved the search condition
        switcher = {}
        os.system('clear')
        print('Available Projects: ')
        for i in range(len(projects)):
            print(f'{i+1}){projects[i].title}')
            switcher[str(i+1)] = projects[i]
        print("0)Exit")
        
        inp = input("Select Project to view: ")
        os.system("clear")
        if inp in switcher:
            for key,value in switcher[inp].__dict__.items():
                print(f"{key}: {value}")
            input("Press enter to continue")
            self.availableProjects(projects)

        elif inp == '0':
            self.findProject()
        else:
            input("Invalid input!, press enter to continue")
            self.availableProjects(projects)

        


        
                    

    def findTime(self):#search on time
        os.system('clear')
        inp = input("Enter the date you want to check: ")
        if not IsValid.isValid('date',inp):
            input("Wrong date formate, the date must be like 22-3-2020, press enter to continue")
            self.findTime()

        projectTitles = Project.getProjectTitles()
        projects = []
        for title in projectTitles:
            
            title = eval(title)['project']
            project = Project.getProject(title)
            checkTime = datetime.strptime(inp, "%d-%m-%Y")
            startTime = datetime.strptime(project.startTime, "%d-%m-%Y")
            endTime = datetime.strptime(project.endTime, "%d-%m-%Y")
            if (startTime < checkTime) and (checkTime < endTime):
                projects.append(Project.getProject(title))
        self.availableProjects(projects)

            
            


    def sysExit(self):#last screen before ending
        os.system('clear')
        print('****************************************************************')
        print('*****************Thanks For Choosing My Project*****************')
        print('****************************************************************\n\n')
        input('Press enter to continue')
        exit()


if __name__ == '__main__':
    sys = System()
    sys.startSystem()