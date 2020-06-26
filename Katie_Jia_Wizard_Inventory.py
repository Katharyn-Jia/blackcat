##############################################################################
## Program that keeps track of the inventory of items a wizard is carrying. ##
## Your program will allow the user to show/add/remove/edit the items the   ##
##      wizard is carrying. 
#PROG 110
#Katharyn Jia
#June 10 2020
############################################################################
def display_title():
    print("The Wizard Inventory program")
    print()    

def display_menu():
    print("COMMAND MENU")
    print("show - Show all items")
    print("grab - Grab an item")
    print("edit - Edit an item")
    print("drop - Drop an item")
    print("exit - Exit program")
    print()

def show(inventory):
    '''Show Current Inventory'''
    for item in inventory:
        print("Item %d of 4: %s" %((1+ inventory.index(item)),item))

def grab_item(inventory):
    '''add new item if inventory is less than 4 items'''
    #if inventory is full
    if len(inventory) >= 4:
        print("You cannot carry any more items, please drop something first")
    else: 
        item = input("Name of New Item: ")
        inventory.append(item)
        #validate item has been added, then confirm
        if item in inventory:
            print("%s has been added to you inventory as item %d of 4" %(item, (inventory.index(item)+1)))
        #not sure about the use cases for this (interrupted processes?)
        else:
            print("Grab unsucessful, please try again")

def edit_item(inventory):
    '''edit name of a specific item in inventory'''
    while True:
        item_num = input("Please enter the item number of the item you wish to edit ('s' to show list): ")
        valid = (item_num.lower() == 's') or ((int(item_num)-1) in range(len(inventory)))
        #provide list of current items with index
        if item_num.lower() == 's':
            show(inventory)
            continue
        #loop for invalid input
        elif valid == False:
            print("Invalid item number")
            continue
        #edit name of item at index from input
        else: 
            item_num = (int(item_num)-1)
            new_item = input("New Name: ")
            inventory[item_num] = new_item
            #confirmation statement
            if inventory[item_num] == new_item:
                print("Item %d was updated." %(item_num+1))
            else:
                print("Edit failed, please try again.")
            break


def drop_item(inventory):
    '''Remove an item from the inventory'''
    #Check for empty inventory
    if len(inventory) == 0:
        print("You have no items to drop. Grab an item")
    else:
        while True:
            item_num = input("Please enter the item number of the item you wish to edit ('s' to show list): ")
            #bool to validate input
            valid = (item_num.lower() == 's') or ((int(item_num)-1) in range(len(inventory)))
            #added help for user: show list of items and indexes
            if item_num.lower() == 's':
                show(inventory)
                continue
            #invalid input loop
            elif valid == False:
                print("Invalid item number")
                continue
            #remove specified item
            else: 
                item_num = (int(item_num)-1)
                removed_item = inventory[item_num]
                #confirmation check
                confirm = input("Are you sure you would like to remove %s? (y to proceed) " %removed_item)
                if confirm.lower() == 'y':    
                    del inventory[item_num] 
                    print("%s was dropped." % removed_item)
                    break
                #all other inputs will return user to main menu
                else:
                    print("Item was not dropped.")
                    break

def main():
    display_title()
    display_menu()

    # start with these 3 items
    inventory = ["wooden staff", "wizard hat",
                 "cloth shoes"]

    while True:        
        command = input("Command: ")        
        if command == "show":
            show(inventory)
        elif command == "grab":
            grab_item(inventory)
        elif command == "edit":
            edit_item(inventory)
        elif command == "drop":
            drop_item(inventory)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
