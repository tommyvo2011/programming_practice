import os
import pymupdf as pm

logfile = "log_test.txt"
log = open(logfile, "w")
root_path = "F:\Programming\Test_Folder"

# Check for the number of pages within the document if
# unable then it will create an exception error and add to log
def check_pdf_corruption():
    try:
        doc = pm.open(j)
        num_pages = doc.page_count
        print(num_pages)
        doc.close()
    except:
        print("Error File: " + j)
        os.chdir(root_path)
        list_of_files.append(j)
        log = open("log_test.txt","a")
        log.write(i + "\t")
        log.write(j + "\n")
        log.close()
        os.chdir(i)

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
            check_pdf_corruption()
    except NotADirectoryError:
        continue
          
    print(list_of_files)
    os.chdir(root_path)
    print(os.getcwd())