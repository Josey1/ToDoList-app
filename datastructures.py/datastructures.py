
todo_list = [] #List containing the tasks to be done
    

# A function to add items to my list
def add_item(item):
    #Providing a placeholder to input new items on my list
    
    item = input("Add new item to list: ")
    todo_list.append(item)#The added item is added to my todo_list
    return todo_list

#Finding a specific to do item on list
def find_item(item):
    todo_list.count(item)# if the count of a particular item on list is greater than zero, then that item is in list
    if todo_list.count(item) > 0:
        return item
    else:
        print("Item is not in my todo_list")


# Deleting a specific to do item on my list
def delete_item(item):
   todo_list.remove(item)
   return todo_list

# Editing a specific todo_item on the list
def replace_item(item):
    for n, i in enumerate(todo_list:
        if i = = "item":
            todo_list[n] = "new_item"

    
# clearing the todo_list items


def delete_all_items():
    todo_list.clear()
    return todo_list
