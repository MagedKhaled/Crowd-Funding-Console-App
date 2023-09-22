from account import Account
from project import Project 
import os

class System:
    def startSystem(self):
        os.system('clear')
        print("*************************************************")
        print("*************************************************")
        print("**************Welcome in My Project**************")
        print("*************************************************")
        print("*************************************************\n\n")
        input("Press Enter to continue ")
        self.loggingScreen()


    def loggingScreen(self):
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

        if not (inp in switcher):
            print("Invalid Input")
            input('press enter to continue ')
            self.loggingScreen()
        else:
            switcher[inp]()


    def projectScreen(self):
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

        if not (inp in switcher):
            print("Invalid Input")
            input('press enter to continue')
            self.startSystem()
        else:
            switcher[inp]()

    def userLogin(self):
        os.system('clear')
        self.user = Account.login(Debug=False)
        input(f"Welcome {self.user.name}, press Enter to continue ")
        self.projectScreen()
    
    def userSignup(self):
        os.system('clear')
        Account()
        input("Your Account created successfully, press Enter to continue ")
        self.loggingScreen()

    def userLogout(self):
        self.user = None
        self.loggingScreen()

    def createProject(self):
        os.system('clear')
        self.user.createProject()
        input("Your project created successfully, press enter to continue")
        self.projectScreen()

    def viewProjects(self):
        os.system('clear')
        Project.viewAll()
        input("Press Enter to continue ")
        self.projectScreen()


    def chooseProject(self):
        os.system('clear')
        userProjects = self.user.projects
        print("Your available projects: ")
        for i in range(len(userProjects)):
            print(f"{i+1}){userProjects[i]}")
        print("0)Exit")

        
        inp = input("Enter Your Choice: ")
        switcher = {
            str(i+1): userProjects[i] for i in range(len(userProjects))
        }

        if inp == 0:
            self.projectScreen()
            
        elif not (inp in switcher):
            print("Invalid Input")
            input('press enter to continue')
            self.chooseProject()
        
        else:
            project = Project.getProject(switcher[inp])
            return project 
 
    def editProject(self):
        project = self.chooseProject()
        if project :
            self.editProjectStage2(project)

    def editProjectStage2(self,project):
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
            "0":self.chooseProject
        }
        

        inp = input("Enter The field to Edit: ")
        if not (inp in switcher):
            print("Invalid Input")
            input('press enter to continue')
            self.editProjectStage2()
        else:
            switcher[inp](project)
            project.saveProject()


    def getTitle(self,project):
        os.system('clear')
        oldTitle = project.title
        project.getTitle()
        Project.deleteProject(oldTitle)
        input(f"Project's title updated to {project.title}, Press Enter to continue")
        self.editProjectStage2(project)


    def getDetails(self,project):
        os.system('clear')
        project.getDetails()
        input(f"Project's details updated to {project.details}, Press Enter to continue")
        self.editProjectStage2(project)

    def getTarget(self,project):
        os.system('clear')
        project.getTarget()
        input(f"Project's target updated to {project.target}, Press Enter to continue")
        self.editProjectStage2(project)

    def getStart(self,project):
        os.system('clear')
        project.getStart()
        input(f"Project's start date updated to {project.startTime}, Press Enter to continue")
        self.editProjectStage2(project)

    def getEnd(self,project):
        os.system('clear')
        project.getEnd()
        input(f"Project's end date updated to {project.endTime}, Press Enter to continue")
        self.editProjectStage2(project)

    def deleteProject(self):
        project = self.chooseProject()
        inp = input(f"You Will delete {project.title} project, press 'yes' to continue")
        if inp.lower() == 'yes':
            title = project.title
            Project.deleteProject(project.title)
            input(f"The project {title} deleted successfully, press enter to continue")
            self.projectScreen()
        else:
            input("Delete process is canceled, press enter to continue ")
            self.projectScreen()
        
    
    def findProject(self):
        pass
        



sys = System()
sys.startSystem()