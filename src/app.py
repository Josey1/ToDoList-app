from tasks import todo_list, create_task, delete_task
from tasks import delete_all_tasks, mark_as_finished
from accounts import accounts, add_account, login

#Allowing the person to input their username and password in order to sign in
if __name__ == "__main__":
    
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    
    print("You are signed in!")
    

   #For a person without an account to create one!
    add_account(name, password)


    #Providing options
       

    print("Select Option:")
    print("1: Create Task")
    print("2: Delete Task")
    print("3: Delete all Tasks")
    print("4:Mark a task finished")
    print("0: Quit")
    
    selection = int(input("selection: "))
    task = str(input("Enter a task: "))
    
# Allowing user to choose the option to carry out
    def select_tasks():
        selection = int(input("selection: "))

    if selection == 1:
           task = str(input("Enter a task: "))
    if task !=" ":
                create_task(task)
                print("Your task has been added.")
        
        
    elif  selection == 2:
                task = input("Enter task to delete. ")
                delete_task(task)
        
    
    elif  selection == 3:
               delete_all_tasks()
               print("All tasks have been deleted. ")
        
        
    elif selection == 4:
               task = input("Enter task to complete: ")    
               mark_as_finished(task)

    elif selection == 0:
               print("Good bye!")
               quit()
    else:
              print("Login to redo process")
   
