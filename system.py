from account import Account,User
from project import Project 

class System:
    def startSystem(self):
        print("*************************************************")
        print("*************************************************")
        print("**************Welcome in My Project**************")
        print("*************************************************")
        print("*************************************************\n\n")
        
        self.loggingScreen()


    def loggingScreen(self):
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
            input('press enter to continue')
            self.loggingScreen()
        else:
            switcher[inp]()


    def projectScreen(self):
        print("1)Create Project")
        print("2)All Projects")
        print("3)Edit Project")
        print("4)Delete Project")
        print("5)Find Project")
        print("0)Exit")

        inp = input("Enter Your Choice: ")
        switcher = {
            '1': self.user.createProject,
            '2': self.viewProjects,
            '3': self.editProject,
            '4': self.deleteProject,
            '5': self.findProject,
            '0': self.sysExit
        }

        if not (inp in switcher):
            
            print("Invalid Input")
            input('press enter to continue')
            self.startSystem()
        else:
            switcher[inp]()

    def userLogin(self):
        self.user = Account.login()
        self.projectScreen()
    
    def userSignup(self):
        Account()

    def sysExit(self):
        exit()

    def viewProjects(self):
        Project.viewAll()
        self.projectScreen()


    def editProject(self):
        pass

    def deleteProject(self):
        pass
    
    def findProject(self):
        pass
        



sys = System()
sys.startSystem()

# def createProject(user):
#     print(user.email)
#     pro = Project(user.email)
#     print(pro.__dict__)


# user = Account.login()
# createProject(user)

