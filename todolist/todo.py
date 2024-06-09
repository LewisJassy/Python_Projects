# a todo list application
# add tasks
def add_task():
    """Add tasks to the task.txt file"""
    tasks = []
    while True:
        task = input("Enter your task (or 'q' to quit): ").strip()
        if task.lower() != 'q':
            tasks.append(task)
        else:
            break

    if tasks:
        with open("task.txt", "a") as file:
            file.write(" \n".join(tasks) + "\n")  # join task with space and add newline
        print("Task added successfully")
    else:
        print("No task added")

# view tasks
def view_task():
    """View tasks from the task.txt file"""
    with open("task.txt") as file:
        tasks = file.readlines()
        if tasks:
            print("Your tasks are:")
            for index, task in enumerate(tasks, 1): #this line gets the index of the task and the task itself
                print(f"{index}. {task.strip()}")
        else:
            print("No task found")

# mark completed tasks
def mark_complete_tasks():
    """Mark completed tasks in the task.txt file"""
    complete_task = int(input("Enter the task number you want to mark as complete: "))
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    if tasks:
        if 1 <= complete_task <= len(tasks):
            task_to_complete = tasks[complete_task - 1].strip()
            if not task_to_complete.endswith("- Completed"):  # Check if task is not already marked as completed
                tasks[complete_task - 1] = task_to_complete + " - Completed\n"  # Mark task as completed
                with open("task.txt", "w") as file:
                    file.write("".join(tasks))
                print("Task marked as completed")
            else:
                print("Task already marked as completed")
        else:
            print("Invalid task number")

def delete_tasks():
    """Delete tasks from the task.txt file"""
    delete_task = int(input("Enter the task number you want to delete: "))
    with open("task.txt", "r") as file:
        tasks = file.readlines()

    if tasks:
        if 1<= delete_task <= len(tasks):
            tasks.remove(tasks[delete_task - 1])
            with open("task.txt", "w") as file:
                file.write("".join(tasks))
            print("Task deleted successfully")
        else:
            print("Invalid task number")

# main function
def choice():
    """Display the menu and return the choice"""
    print("1. Add task")
    print("2. View task")
    print("3. Mark completed tasks")
    print("4. Delete tasks")
    print("5. Exit")
    return int(input("Enter your choice: "))  # return the choice

while True:
    try:
        ch = choice()
        if ch == 1:
            add_task()
        elif ch == 2:
            view_task()
        elif ch == 3:
            mark_complete_tasks()
        elif ch == 4:
            delete_tasks()
        elif ch == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice")

    except ValueError:
        print("Invalid choice. Enter a valid choice")
