import os
import datetime
import shutil
import time



def getFiles(dir):
    return os.listdir(dir)

def printList(list):
    print("\n-----Printing Files & Folders-----")
    i = 1
    for item in list:
        print(str(i) + " " + item)
        i = i + 1

def checkDirectories(dir, list):
    print("\n-----Checking directory for folders.-----")
    i = 1
    for item in list:
        if os.path.isdir(os.path.join(dir, item)):
            print(str(i) + " " + os.path.join(dir, item))
            i = i+1

def removeDirectories(dir, list):
    print("\n-----Removing folders from list.-----")
    rmlist = []
    for item in list:
        if os.path.isdir(os.path.join(dir, item)):
            rmlist.append(item)
    for removable in rmlist:
        print("Removing " + removable + ".")
        list.remove(removable)
    return list

def organizeFiles(dir, list):
    for item in reversed(list):
        # Get the creation year of the file
        year = str(datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(dir, item))))[0:4]

        # Create the year directory if it doesn't exist
        if not os.path.exists(os.path.join(dir, year)):
            os.makedirs(os.path.join(dir, year))

        # Get the file extension
        file_extension = os.path.splitext(item)[1][1:]

        # Create the file type directory if it doesn't exist
        if not os.path.exists(os.path.join(dir, year, file_extension)):
            os.makedirs(os.path.join(dir, year, file_extension))

        # Move the file to the appropriate directory
        shutil.move(os.path.join(dir, item), os.path.join(dir, year, file_extension, item))

def main():
    # Directory to be maintained
    dir = "V:\\Users\\Alan\\Downloads"

    # Get list of items in the directory
    files = getFiles(dir)
    #checkDirectories(dir, files)

    # Remove pre-existing directories from list
    files = removeDirectories(dir, files)

    # Organize remaining files into folders
    organizeFiles(dir, files)

main()