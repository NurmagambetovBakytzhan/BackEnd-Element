import os

os.chdir("C:\\")
while(True):
    orig_comm = input("Enter command: ")
    comm = orig_comm
    second_comm = ""
    try:
        second_comm = orig_comm.split(' ')[1]
        comm = orig_comm.split(' ')[0]
    except:
        pass

    if comm == "dir":
        for i in os.listdir():
            print(i)

    elif comm == "cd..":
        if(os.getcwd != "C:\\"):
            os.chdir(os.path.dirname(os.getcwd()))
        
        print(os.getcwd())
    elif comm == "cd":
        
        if(second_comm in os.listdir()):
            os.chdir(second_comm)
        else:
            print("No such directory!")
            raise FileNotFoundError
        print(os.getcwd())
    elif comm == "mkdir":
        if second_comm not in os.listdir():
            os.mkdir(second_comm)
        else:
            print("File with such name already exists!")
            raise FileExistsError
        print(os.getcwd())
    elif comm == "rmdir":
        if second_comm in os.listdir():

            os.rmdir(second_comm)
            print("Deleted succesfully!")
        else:
            print("No such directory")
            raise FileNotFoundError
    elif comm == "remove":
        if second_comm in os.listdir():
            os.remove(second_comm)
        else:
            print("No such directory")
            raise FileNotFoundError
    
    elif comm == "rename":
        third_comm = orig_comm.split(" ")[2]
        if(second_comm in os.listdir()):
            os.rename(second_comm, third_comm)
        else:
            print("No such file or directory")
            raise FileNotFoundError
        print(os.getcwd())

    elif comm == "read":
        if(second_comm in os.listdir() ):
            with open(second_comm) as f:
                lines = f.readlines()
                for l in lines:
                    print(l)
        else:
            print("No such file!")
            raise FileNotFoundError
    
    elif comm == "quit":
        print("Good bye!")
        break