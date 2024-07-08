import os
import fitz as fr

logfile = "log_test.txt"
log = open(logfile, "w")
root_path = "F:\Programming\Test_Folder"

def log_txt():
    os.chdir(root_path)
    log    

def check_pdf_corruption():
    try:
        f = open(j, "r")
        font_check = fr.CheckFont
    except:
        print("Error File: " +j)
        os.chdir(root_path)
        list_of_files.append(j)
        log = open("log_test.txt","a")
        log.write(i + "\t")
        log.write(j + "\n")
        log.close()

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
                f = open(j, "r")
                font_check = fr.get_text_length
                print(font_check)
                f.close()
            except:
                print("Error File: " +j)
                os.chdir(root_path)
                list_of_files.append(j)
                log = open("log_test.txt","a")
                log.write(i + "\t")
                log.write(j + "\n")
                log.close()
    except NotADirectoryError:
        continue
          
    print(list_of_files)
    #os.chdir("../")
    os.chdir(root_path)
    print(os.getcwd())