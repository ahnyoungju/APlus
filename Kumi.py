# provide menu for (1) adding items and print ADD (2) deleting items and print DELETE (3) print list SHOW (4) assistance HELP commands

# provide list of all items

shopping_list = []


def show_help():
    # print instructions to use menu on app

    print("""
  -----------------------------------------------------------

  SHOPPING LIST MENU:

  1. ADD : to add new item and print shopping list
  2. DELETE : to delete item and print shopping list
  3. SHOW : to print list of current items
  4. HELP : to bring up menu  

  -----------------------------------------------------------
  """)

    user = input("What is your name?\n")
    print("Hello " + user + "!")
    print(
        "Enter item you need and press enter. Repeat for every new item to add. When finished, make a selection from the above menu")


def show_list():
    # print current list of items

    print("Your shopping list: ")

    for item in shopping_list:
        print(item)


def add_item_to_list(new_item):
    # add new item to shopping list

    shopping_list.append(new_item)
    print("{} has been added. Your Shopping List now has {} items.".format(new_item, len(shopping_list)))


show_help()
while True:

    # user will be asked for new items to add
    new_item = input("> ")

    # user have option to quit app
    if new_item == "1":
        show_list()
        break
    elif new_item == "2":
        delete_item = input("Which item would you like to remove?\n")
        shopping_list.remove(delete_item)
        show_list()
        continue
    elif new_item == "3":
        show_list()
        continue
    elif new_item == "4":
        show_help()
        continue

    add_item_to_list(new_item)