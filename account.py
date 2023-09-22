from project import Project, ImportProject

# Class to create account including sign in, sign up, 


class Account:
    loginFile = 'users/login_data'
    def __init__(self):
        self.getName() #firstName,lastName,name
        self.getEmail() #email
        self.getPass() #passwd
        self.getMobile() #mobile
        # self.fileName = self.email

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



    def getName(self):
        self.firstName = self.__class__.getInp('First Name',True)

        self.lastName = self.__class__.getInp('Last Name',True)
        self.name = self.firstName+' '+self.lastName

    def getEmail(self):
        self.email = self.__class__.getInp('Email',True)

    def getPass(self):
        self.passwd = self.__class__.getInp('Password',True)
        rePasswd = self.__class__.getInp('RePassword',True)
        while not (rePasswd == self.passwd) :
            print("You wrote a wrong rePassword")
            inp = input('Press Enter to rewrite the rePassword or Q to change the password: ')
            if inp.lower() == 'q':
                break
            rePasswd = self.__class__.getInp('RePassword',True)
        else:
            print('pass is done')
            return
        self.getPass()

    def getMobile(self):
        self.mobile = self.__class__.getInp('Phone Number')

    def save(self):
        with open(f'{__class__.loginFile}','a') as file:
            file.write(str(self.__dict__)+'\n')




    @classmethod
    def login(cls):
        myEmail = cls.getInp("Email",True)
        userData = cls.getUserData(myEmail)
        if userData:
            while True : 
                userPass = cls.getInp("Password",True)
                if userPass == userData['passwd']:
                    
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
        self.projectsTitles = []
        self.projects = []
        self.firstName = data['firstName']
        self.lastName = data['lastName']
        self.email = data['email']
        self.passwd = data['passwd']
        self.mobile = data['mobile']
        self.getMyProjects()


    def createProject(self):
        self.projects.append(Project(self.email))
        self.projectsTitles.append(self.projects[-1])


    def getMyProjects(self):
        for project in self.projectsTitles:
            self.projects.append(ImportProject(project))

                






# Account()
# Account()

# myUser = Account.login()
# print(myUser.__dict__)



