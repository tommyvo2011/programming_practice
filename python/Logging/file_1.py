import os

logfile = "log_test.txt"
log = open(logfile, "w")
root_path = "C:\Test_Folder"

def log_txt():
    os.chdir(root_path)
    log    


list_of_dir = []

os.chdir(root_path)

# Grabs the directories' names
for x in os.listdir():
    list_of_dir.append(x)
print(list_of_dir)

#Grabs the files' name
for i in list_of_dir:
    list_of_files = []
    
    try:
        os.chdir(i)
        print(os.getcwd())
        #Creates a list of the files names and append them to an array
        for j in os.listdir():
            try:
                with open(j, "a+"):
                    j.close()
            except OSError:
                os.chdir(root_path)
                list_of_files.append(j)
                with open("log_test.txt", "a+"):
                    log.append(j + "\n")
                    log.close()
    except NotADirectoryError:
        continue
          
    print(list_of_files)
    os.chdir("../")