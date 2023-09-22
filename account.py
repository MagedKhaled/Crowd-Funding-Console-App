from project import Project
from validation import IsValid
import os
from getpass import getpass
import hashlib



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
        os.system('clear')
        if required:
            if (inpName == 'Password') or (inpName == 'RePassword'):
                inp = getpass(f"Enter Your {inpName}: ")
            else:
                inp = input(f"Enter Your {inpName}: ")
                
            if inp :
                return inp
            else:
                input(f"The {inpName} is required, press enter to continue ")
                cls.getInp(inpName,required=required)
                    
        
        else:
            return input(f"Enter Your {inpName}: ")



    def getFirstName(self):
        self.firstName = self.__class__.getInp('First Name',True)
        if IsValid.isValid('name',self.firstName):
            return
        else:
            input('The name must be alphabetic only, press enter to continue ')
            self.getFirstName()

    def getLastName(self):
        self.lastName = self.__class__.getInp('Last Name',True)
        if IsValid.isValid('name',self.lastName):
            return
        else:
            input('The name must be alphabetic only, press enter to continue ')
            self.getLastName()


    def getEmail(self):
        self.email = self.__class__.getInp('Email',True)
        state = IsValid.isValid('email',self.email,unique=True,exception='email')
        if state:
            if state == 'exist':
                input('The Email is exist, press enter to continue ')
                self.getEmail()
            else:
                return
        else:            
            input('The Email is invalid, press enter to continue ')
            self.getEmail()

    def getPass(self):
        self.passwd = self.__class__.getInp('Password',True)
        if len(self.passwd)<4:
            input("Your Password must be at least 4 characters or numbers, press enter to continue ")
            self.getPass()

        rePasswd = self.__class__.getInp('RePassword',True)
        while not (rePasswd == self.passwd) :
            print("You wrote a wrong rePassword")
            inp = input('Press Enter to rewrite the rePassword or Q to change the password: ')
            if inp.lower() == 'q':
                break
            rePasswd = self.__class__.getInp('RePassword',True)
        else:
            self.passwd = hashlib.sha256(self.passwd.encode()).hexdigest()
            return
        
        self.getPass()

    def getMobile(self):
        self.mobile = self.__class__.getInp('Phone Number')
        if IsValid.isValid('mobile',self.mobile):
            return
        else:
            input("Invalid Mobile Number, press enter to continue ")
            self.getMobile()
        


    def save(self):
        with open(f'{__class__.loginFile}','a') as file:
            file.write(str(self.__dict__)+'\n')




    @classmethod
    def login(cls,Debug=False):
        if Debug:
            userData = cls.getUserData("maged.khaled03@gmail.co")
            return User(userData)
        
        myEmail = cls.getInp("Email",True)
        userData = cls.getUserData(myEmail)
        if userData:
            while True : 
                userPass = cls.getInp("Password",True)
                userPass = hashlib.sha256(userPass.encode()).hexdigest()
                if userPass == userData['passwd']:

                    user =  User(userData)
                    return user
                else:
                    print("Wrong Password!")
                    inp = input("Press Enter to try again or 'Q' to try with another email: ")
                    if inp.lower() == 'q':
                        break
                    
        else:
            input('This Email is not exist, press enter to continue ')
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
        self.name = self.firstName+' '+self.lastName
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

                



