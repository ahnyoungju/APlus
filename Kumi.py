# provide menu for (1) adding items and print ADD (2) deleting items and print DELETE (3) print list SHOW (4) assistance HELP (5) exit QUIT commands

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
  5. QUIT : to exit app

  -----------------------------------------------------------
  """)

    user = input("What is your name?\n")
    print("Hello " + user + "!")
    print("Type each item you need and press enter. When done, make a selection from the above menu from 1 to 5.")

def show_list():
    # print current list of items

    print("Your shopping list: ")

    for item in shopping_list:
        print(item)

def add_item_to_list(new_item):
    # add new item to list

    shopping_list.append(new_item)
    print("{} has been added. Your Shopping List now has {} items.".format(new_item, len(shopping_list)))

#------------ start ---------------
show_help()
while True:

    # user will be asked for new items to add
    new_item = input("> ")

    # user have option to quit app
    if new_item == "1":
        show_list()
        #print("Let’s hit the road! You are ready to go shopping!")
        #break
    # user will be asked for item to delete
    elif new_item == "2":
        delete_item = input("Which item would you like to remove?\n")
        if delete_item in shopping_list:
            shopping_list.remove(delete_item)
        else:
            print("This is not in the list.")

        show_list()
        continue
        #print("Let’s hit the road! You are ready to go shopping!")
        #break
    elif new_item == "3":
        show_list()
        #print("Let’s hit the road! You are ready to go shopping!")
        #break
        continue
    elif new_item == "4":
        show_help()
        continue
    elif new_item == "5":
        show_list()
        with open("ShoppingList.json", "w") as fout:
           fout.write(str(shopping_list))

        print("Let’s hit the road! You are ready to go shopping!")
        break

    add_item_to_list(new_item)
