import os

logfile = "log_test.txt"
log = open(logfile, "w")
root_path = "C:\Test_Folder"


def log_txt():
    os.chdir(root_path)
    log    

list_of_dir = []


# Grabs the subdirectories' name
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
            list_of_files.append(j)
            os.chdir(j)
            if(os.)
            try:
                log
            except IOError:
                log_txt()
                log.write(i, "\t", j)
    except NotADirectoryError:
        continue
          
    print(list_of_files)
    os.chdir("../")