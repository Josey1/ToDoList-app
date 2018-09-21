# This file contains code that manages your todo_list
todo_list = [] #List containing the tasks to be done
finished_task = '[Finished]'
    

# Write a function creates a task


def create_task(task):
    """
    Adds the task (string value) to todo_list
    """
    task = input("State your new task: ")#providing placeholder for inputting new tasks
  
    #adding created new tasks to the todo_list using the append function
   
    todo_list.append(task)
    return todo_list
    

# Write a function deletes a task


def delete_task(task):
    """
    Removes the specified task from the todo_list
    """
    todo_list.remove(task)
    return todo_list

# Write a function that marks a task finished


def mark_as_finished(task):
    """
    Append the string label '[finished]' at the end of the task 
    if it does not already have the label appended.
    It should remain in the todo_list
    """
    task_index = todo_list.index(task)
    todo_list[task_index] = task + " [finished]"
 
    return todo_list
       
       

# Write a function deletes all tasks


def delete_all_tasks():
    """
    Empty the the todo_lsit
    """
    todo_list.clear()
    return todo_list
