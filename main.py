from task_manager.task_utils import (
    add_task,
    mark_task_complete,
    view_tasks,
    view_pending_tasks,
    calculate_progress
)

tasks = []


def display_menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. Mark Task Complete")
    print("3. View All Tasks")
    print("4. View Pending Tasks")
    print("5. Track Progress")
    print("6. Exit")


while True:
    display_menu()

    try:
        choice = input("Enter your choice: ")
    except EOFError:
        break

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        mark_task_complete(tasks)

    elif choice == "3":
        view_tasks(tasks)

    elif choice == "4":
        view_pending_tasks(tasks)

    elif choice == "5":
        print(calculate_progress(tasks))

    elif choice == "6":
        print("Exiting Task Manager...")
        break

    else:
        print("Invalid choice. Please try again.")