def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added!")

def view_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found!")
                return
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task.strip()}")
    except FileNotFoundError:
        print("No tasks yet!")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()

        if 0 < num <= len(tasks):
            tasks.pop(num - 1)

            with open("tasks.txt", "w") as file:
                file.writelines(tasks)

            print("Task deleted!")
        else:
            print("Invalid number!")
    except:
        print("Error!")

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice")