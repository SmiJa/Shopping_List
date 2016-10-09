import os
# make a list to hold onto our items
shopping_list = []
lists = []
c_file_name = ""

lists_path = 'lists'

if not os.path.exists(lists_path):
    os.makedirs(lists_path)

# print out instructions on how to use the app
print("Add items to your list.")
print("Enter 'DONE' one you are finished.")
print (c_file_name)

def show_help():
    print(
    """
    SHOW - will show you what is currently on the list
    DONE - will end the add new items option.
    HELP - will show a Help menu""")

def show_list():
    count = 1
    print("You have {} items on your list.".format(len(shopping_list)))
    print("Heres your list:")
    for item in shopping_list:
        print(str(count) + ". " + str(item))
        count += 1

def show_lists():
    for file in os.listdir(lists_path):
        print(file)

def add_item():
    global c_file_name
    shopping_list.append(new_item)
    print("You now have {} item(s) on your list".format(len(shopping_list)))
    if c_file_name == "":
        print("Your current file name is {}.".format("untitled"))
        print("You should save your list.")
    

def save_list():
    global c_file_name
    if c_file_name == "":
        file_save = open(lists_path + "/untitled.txt", 'w')
        for item in shopping_list:
            file_save.write(item + "\n")
        
        print("Your list has been saved as untitled")
    else:
        file_save = open(lists_path + "/" + c_file_name + ".txt", 'w')
        for item in shopping_list:
            file_save.write(item + "\n")
        print("Your list has been saved as {}".format(c_file_name))

    file_save.close()

def save_list_as():
    global c_file_name
    print("What would you like to name your list?")
    print("")
    new_file_name = input("> ")
    c_file_name = new_file_name
    file_save_as = open(lists_path + "/" + c_file_name + ".txt", 'w')

    for item in shopping_list:
        file_save_as.write(item + "\n")

    file_save_as.close()
    print("You saved your list as {}".format(c_file_name))


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
    print("Your list has been loaded")


while True:
    # ask for new items
    new_item = input("> ")

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
    else:
        # add new items to our list
        add_item()

# print out the list
show_list()
