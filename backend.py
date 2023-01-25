import os
import time
class User:
    def __init__(self,username):
        '''
            default constructor
        '''
        self.username = username
        self.location = os.getcwd() + "/root/" + self.username
        list_of_dir = os.listdir(os.getcwd()+"/root")
        if self.username not in list_of_dir:
            try:
                os.mkdir(self.location)
            except OSError:
                print("user folder could not be created")
        self.location = os.getcwd() + "/root/" + self.username


    def change_directory(self,dir_name):
        '''
            to move from one directory to other
        '''
        print(self.location)
        if dir_name == "..":
            split_string = self.location.split("/")
            split_string.pop(len(split_string)-1)
            self.location = "/".join(split_string)
            print(self.location)
            return "directory changed"
        else:
            if dir_name in os.listdir(self.location):
                self.location = self.location+"/"+dir_name
                print(self.location)
                return "changed directory"
            else:
                return "directory not found"


    def create_directory(self,dir_name ):
        '''
            to create a new folder
        '''
        if dir_name in os.listdir(self.location):
            return "cannot create the folder as it already exists"
        else:
            os.mkdir(self.location+"/"+dir_name)
            return "created !!!"



    def write_to_file(self,file_name, msg):
        '''
            to write to a file
        '''
        message = " "
        for i in msg:
            message = message + " " + i
        if message!= "":
            open_file = open(self.location + "/" + file_name, 'a')
            open_file.write(f'{message}\n\t')
            open_file.close()
            return "data entered"
        else:
            open_file = open(self.location + "/" + file_name, 'a')
            open_file.write("")
            open_file.close()
            return "data deleted"

    def read_from_file(self,dir_name):
        '''
            to read from a file
        '''
        try:
            if dir_name in os.listdir(self.location):
                open_file = open(self.location+"/"+dir_name,"r")
                data =  open_file.read()
                open_file.close()
                return data
            else:
                return "failed to open the respective file"
        except OSError as err:
            return err

#-------------------------------------------------

def register(uid,pwd):
    '''
        to register a user
    '''
    open_file = open('userdetails.txt','r')
    for i in open_file:
        data_split = i.split(" ")
        user = data_split[0]
        if user == uid:
            return "user with same name exists"
    open_file.close()
    open_file = open("userdetails.txt",'a')
    open_file.write("\n"+uid+" "+pwd)
    open_file.close
    return "user created"

def login(uid,pwd):
    '''
        to login a user
    '''
    users = []
    open_file = open("userslog.txt",'r')
    for i in open_file:
        users.append(i)
    open_file.close()
    open_file = open('userdetails.txt','r')
    user_data = open_file.read()
    user_lists = user_data.split("\n")
    for i in user_lists:
        print(i)
        data_split = i.split(" ")
        print(data_split)
        user = data_split[0]
        pword = data_split[1]
        if (user) == uid and (pwd) == pword:
            if uid+"\n" not in users:
                msg = "logged in"
                open_file2 = open("userslog.txt",'a')
                open_file2.write(uid+"\n")
                open_file2.close()
            else:
                msg = "user already logged in"
        else:
            msg = "username or password mismatch"
    open_file.close()
    return msg

def logout(uid):
    '''
        to log out a user
    '''
    users = []
    open_file = open("userslog.txt",'r')
    for i in open_file:
        users.append(i)
    open_file.close()
    open_file = open("userslog.txt",'w')
    for i in users:
        if uid + "\n" != i:
            open_file.write(i)
    return "user logged out"

def display_list(loc):
    '''
        to display list of files
    '''
    for i in os.listdir(loc):
        print(i+" "+str(os.stat(loc+"/"+i).st_size)+" "+time.ctime(os.path.getctime(loc+"/"+i)))


