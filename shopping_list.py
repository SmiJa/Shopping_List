import os

# make a list to hold onto our items
shopping_list = []

# current file name is empty
c_file_name = ""

# directory name
lists_path = 'lists'
current_dir = ""
root = '.'

# check to see if the "lists" directory exsists
# if not, create the "lists" directory.
if not os.path.exists(lists_path):
    os.makedirs(lists_path)

current_dir = lists_path

# print out instructions on how to use the app
print("Add items to your list.")
print("Enter 'DONE' one you are finished.")

# shows the HELP menu
def show_help():
    print(
    """
    SHOW - will show you what is currently on the list
    DONE - will end the add new items option.
    HELP - will show a Help menu
    LISTS - will show you a list of files available to load.
    LOAD - will load the file you select.
    SAVE - will save the current file.
    SAVE AS - will allow you to choose the name of you file.
    NEW DIR - will allow you to create a new directory to save files.
    CHANGE DIR - will change the directory.
    SHOW DIR - will show directory list.""")
    print("")

# create a new directory.
def new_dir():
    global current_dir
    print("Enter the name of your NEW directory")
    new_dir = input(">: ")
    os.makedirs(new_dir)
    current_dir = new_dir
    print("Your new directory is: " + current_dir)


# change directory.
# def change_dir():

# Show a list of folders
# def show_dirs():
#     for dir in os.walk(root):
#         print(dir)

# shows the current list.
def show_list():
    count = 1
    print("You have {} items on your list.".format(len(shopping_list)))
    print("Heres your list:")
    for item in shopping_list:
        print(str(count) + ". " + str(item))
        count += 1

# shows the current files in the "lists" directory.
def show_lists():
    for file in os.listdir(lists_path):
        print(file)

# adds the item to shopping_list
def add_item():
    # pull in the current file name
    global c_file_name
    shopping_list.append(new_item)
    print("You now have {} item(s) on your list".format(len(shopping_list)))
    print("Your current directory is: " + current_dir)
    print("")

    # check to see if current file name is empty
    if c_file_name == "":
        print("Your current file name is {}.".format("untitled".upper()))
        print("Your current directory is: " + current_dir)
        print("You should save your list.")
        print("")


# saves the list to a text file in the "lists" directory
def save_list():
    global c_file_name
    if c_file_name == "":
        file_save = open(current_dir + "/untitled.txt", 'w')
        for item in shopping_list:
            file_save.write(item + "\n")

        print("Your list has been saved as untitled")
        print("")
    else:
        file_save = open(current_dir + "/" + c_file_name + ".txt", 'w')
        for item in shopping_list:
            file_save.write(item + "\n")
        print("Your list has been saved as {}".format(c_file_name))
        print("")

    file_save.close()

def save_list_as():
    global c_file_name
    print("What would you like to name your list?")
    print("")
    new_file_name = input("> ")
    c_file_name = new_file_name
    file_save_as = open(current_dir + "/" + c_file_name + ".txt", 'w')

    for item in shopping_list:
        file_save_as.write(item + "\n")

    file_save_as.close()
    print("You saved your list as {}".format(c_file_name))
    print("")

# def check_if_same():

def load_file():
    global c_file_name
    del shopping_list[:]
    print("Which file would you like to load?")
    file_to_load = input("> ")
    file_read = open(lists_path + "/" + file_to_load + ".txt", "r")
    c_file_name = file_to_load

    for line in file_read:
        shopping_list.append(line)

    file_read.close()
    print("{} has been loaded".format(c_file_name))
    print("")


while True:
    # ask for new items
    new_item = input(">: ")

    if new_item.upper() == 'DONE':
        # be able to quit the app
        break
    elif new_item.upper() == 'SHOW':
        show_list()
        continue
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'SAVE':
        save_list()
        continue
    elif new_item.upper() == 'LOAD':
        load_file()
        continue
    elif new_item.upper() == 'SAVE AS':
        save_list_as()
        continue
    elif new_item.upper() == 'LISTS':
        show_lists()
        continue
    elif new_item.upper() == 'NEW DIR':
        new_dir()
        continue
    elif new_item.upper() == 'CHANGE DIR':
        change_dir()
        continue
    elif new_item.upper() == 'SHOW DIR':
        show_dirs()
        continue
    elif new_item == "":
        # check to see if user just hit enter with a blank line.
        print("Please enter an item.")
        print("")
    else:
        # add new items to our list
        add_item()

# print out the list
show_list()
