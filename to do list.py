# Simple To-Do List Application

tasks = []

def show_menu():
    print("\n----- TO-DO LIST MENU -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")

    # Add Task
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Update Task
    elif choice == "3":
        if not tasks:
            print("No tasks to update.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = int(input("Enter task number to update: "))
            if 1 <= task_number <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[task_number - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if not tasks:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            task_number = int(input("Enter task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print("Deleted task:", deleted_task)
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "5":
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1-5.")