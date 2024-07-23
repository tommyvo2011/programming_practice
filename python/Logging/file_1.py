import os
import pymupdf as pm

logfile = "log_test.txt"
log = open(logfile, "w")
root_path = "C:\Test_Folder"

# Check for the number of pages within the document if
# unable then it will create an exception error and add to log
def check_pdf_corruption():
    try:
        doc = pm.open(k)
        num_pages = doc.page_count
        print(num_pages)
        doc.close()
    except:
        print("Error File: " + k)
        os.chdir(root_path)
        list_of_files.append(k)
        log = open("log_test.txt","a")
        log.write(i + "\t")
        log.write(j + "\t")
        log.write(k + "\n")
        log.close()
        os.chdir(i)

list_of_dir = []
os.chdir(root_path)

# Grabs the directories' names
for dir in os.listdir():
    list_of_dir.append(dir)
print(list_of_dir)

# Files through each Project Contract ID
for i in list_of_dir:
    list_of_subdir = []
    list_of_files = []
    try:
        # Puts all the subdirectories inside of the Project Contract ID into an array
        os.chdir(i)
        for subdir in os.listdir():
             list_of_subdir.append(subdir)
             print(subdir)

        print(os.getcwd())
        # Checks List of Subdirectories
        for j in list_of_subdir:
            print(os.getcwd())
            try:
                os.chdir(j)
                print(os.getcwd())
                # Checks List of Files
                for k in os.listdir():
                    print(os.getcwd())
                    check_pdf_corruption()
           
            except NotADirectoryError:
                continue

    except NotADirectoryError:
                continue
    print(list_of_files)
    os.chdir(root_path)
    print(os.getcwd())