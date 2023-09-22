from project import Project, ImportProject
from validation import IsValid


# Class to create account including sign in, sign up, 


class Account:
    loginFile = 'users/login_data'
    def __init__(self):
        self.getFirstName() #firstName
        self.getLastName() #lastName
        self.name = self.firstName+' '+self.lastName #name
        self.getEmail() #email
        self.getPass() #passwd
        self.getMobile() #mobile
        self.save() #write in my file

    @classmethod
    def getInp(cls,inpName,required=False):
        if required:
            inp = input(f"Enter Your {inpName}: ")
            while True: 
                
                if inp :
                    return inp
                print(f"The {inpName} is required!")
                inp = input(f"Enter Your {inpName}: ")
                    
        
        else:
            return input(f"Enter Your {inpName}: ")



    def getFirstName(self):
        self.firstName = self.__class__.getInp('First Name',True)
        if IsValid.isValid('name',self.firstName):
            return
        else:
            print('The name must be alphabetic only!')
            self.getFirstName()

    def getLastName(self):
        self.lastName = self.__class__.getInp('Last Name',True)
        if IsValid.isValid('name',self.lastName):
            return
        else:
            print('The name must be alphabetic only!')
            self.getLastName()


    def getEmail(self):
        self.email = self.__class__.getInp('Email',True)
        if IsValid.isValid('email',self.email):
            return
        else:
            print('The Email is invalid!')
            self.getEmail()

    def getPass(self):
        self.passwd = self.__class__.getInp('Password',True)
        if len(self.passwd)<4:
            print("Your Password must be at least 4 characters or numbers")
            self.getPass()

        rePasswd = self.__class__.getInp('RePassword',True)
        while not (rePasswd == self.passwd) :
            print("You wrote a wrong rePassword")
            inp = input('Press Enter to rewrite the rePassword or Q to change the password: ')
            if inp.lower() == 'q':
                break
            rePasswd = self.__class__.getInp('RePassword',True)
        else:
            return
        self.getPass()

    def getMobile(self):
        self.mobile = self.__class__.getInp('Phone Number')
        if IsValid.isValid('mobile',self.mobile):
            return
        else:
            print("Invalid Mobile Number!")
            self.getMobile()
        


    def save(self):
        with open(f'{__class__.loginFile}','a') as file:
            file.write(str(self.__dict__)+'\n')




    @classmethod
    def login(cls,Debug=False):
        print(Debug)
        if Debug:
            userData = cls.getUserData("magedkh")
            return User(userData)
        
        myEmail = cls.getInp("Email",True)
        userData = cls.getUserData(myEmail)
        if userData:
            while True : 
                userPass = cls.getInp("Password",True)
                if userPass == userData['passwd']:
                    print(userData)
                    return User(userData)
                else:
                    print("Wrong Password!")
                    inp = input("Press Enter to try again or 'Q' to try with another email: ")
                    if inp.lower() == 'q':
                        break
                    
        else:
            print('This Email is not exist')
        cls.login()


    @classmethod
    def getUserData(cls,myEmail):
        with open(cls.loginFile,'r') as file:
            users = file.readlines()
            for user in users:
                user = eval(user)
                if user['email'] == myEmail:
                    return user
        return None
            




class User(Account):
    def __init__(self,data):
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.passwd = data['passwd']
        self.mobile = data['mobile']
        self.getMyProjects()



    def createProject(self):
        Project(self.email)
        self.getMyProjects()


    def getMyProjects(self):
        self.projects = []
        projects = Project.getProjectTitles()
        
        for project in projects:
            project = eval(project)
            if project['user'] == self.email:
                self.projects.append(project['project'])

                



