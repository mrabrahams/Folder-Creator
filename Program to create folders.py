# importing os module
import os
import pyinputplus as pyip


def user_input():
    # name of folder and number to create
    directory = pyip.inputStr("Enter the name of the folder you would like to create: ")
    num_folders = pyip.inputNum("Enter the number of folders with that name you want to create: ", min=1) ## no negative numbers

    # Parent Directory path
    parent_dir = pyip.inputStr("please enter the location you would like to create the folder/s, "
                       "example: /Users/chosenUser/Google Drive: \n")
    
    # sub folder creation
    choice = pyip.inputYesNo("Do you want to create any subfolders in this directory? ")
    num_sfolders = 0

    if choice.lower()[0] == "y":
        num_sfolders = pyip.inputNum("How many subfolders would you liker to create? ")
        folder_ls = []

    # send arguments to function
    folder_creator(parent_dir, directory, num_folders, num_sfolders, folder_ls)

# folder creation function
def folder_creator(parent_dir, folder, amount, num_sub, sub_dir):
    
    for i in range(0, amount):
        # create folder
        os.mkdir(os.path.join(parent_dir, folder))
        print("Folder created: " + folder)
        # create subfolders
        if num_sub > 0:
            for i in range(0, num_sub):
                sub_dir.append(pyip.inputStr("Enter the name of the subfolder you would like to create: "))
                os.mkdir(os.path.join(parent_dir, folder, sub_dir[i]))
            print("Directory '% s' created" % i)

    # does the user want to run program again
    selection()


def selection():

    choice = pyip.inputYesNo("Would you like to run the program again? (yes/no): ")

    if choice.lower()[0] == "y":
        user_input()

    elif choice.lower()[0] == "n":
        print("Thank you, goodbye!")
        return 


if __name__ == "__main__": # used to execute code only if the file was run directly. calls the necessary functions

    # start program
    user_input()