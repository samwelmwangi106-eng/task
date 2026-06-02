from task_manager.validation import (
    validate_task_name,
    validate_task_index
)


def add_task(tasks):
    """
    Add a new task.
    """
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date: ")

    if validate_task_name(title):
        task = {
            "title": title,
            "description": description,
            "due_date": due_date,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully!")


def mark_task_complete(tasks):
    """
    Mark a task as completed.
    """
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    choice = input("Enter task number to mark complete: ")

    if validate_task_index(choice, tasks):
        index = int(choice) - 1
        tasks[index]["completed"] = True
        print("Task marked as complete!")


def view_tasks(tasks):
    """
    Display all tasks.
    """
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['title']} [{status}]")


def view_pending_tasks(tasks):
    """
    Display pending tasks only.
    """
    pending = [task for task in tasks if not task["completed"]]

    if not pending:
        print("No pending tasks.")
        return

    print("\nPending Tasks:")

    for i, task in enumerate(pending, start=1):
        print(f"{i}. {task['title']}")


def calculate_progress(tasks):
    """
    Calculate completion percentage.
    """
    if len(tasks) == 0:
        return 0.0

    completed = sum(1 for task in tasks if task["completed"])

    return (completed / len(tasks)) * 100