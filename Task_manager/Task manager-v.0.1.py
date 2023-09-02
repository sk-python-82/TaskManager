# Define the filename for storing tasks
task_file = "tasks.txt"

# Function to add a new task to the task list
def add_task(task):
    """Add a new task to the task list."""
    with open(task_file, "a") as file:
        file.write(task + "\n")

# Function to view all tasks in the task list
def view_tasks():
    """View all tasks in the task list."""
    try:
        with open(task_file, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
            else:
                print("Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks found.")

# Function to edit an existing task
def edit_task(task_number, new_task):
    """Edit an existing task."""
    try:
        with open(task_file, "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = new_task + "\n"
                with open(task_file, "w") as file:
                    file.writelines(tasks)
            else:
                print("Task number out of range.")
    except FileNotFoundError:
        print("No tasks found.")

# Function to delete an existing task
def delete_task(task_number):
    """Delete an existing task."""
    try:
        with open(task_file, "r") as file:
            tasks = file.readlines()
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                with open(task_file, "w") as file:
                    file.writelines(tasks)
                print(f"Deleted task: {deleted_task.strip()}")
            else:
                print("Task number out of range.")
    except FileNotFoundError:
        print("No tasks found.")

# Main program loop
while True:
    # Display the Task Manager menu
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Quit")

    # Get user's choice
    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == "1":
        task = input("Enter the task: ")
        add_task(task)
        print("Task added successfully!")

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        task_number = int(input("Enter the task number to edit: "))
        new_task = input("Enter the new task: ")
        edit_task(task_number, new_task)
        print("Task edited successfully!")

    elif choice == "4":
        task_number = int(input("Enter the task number to delete: "))
        delete_task(task_number)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
