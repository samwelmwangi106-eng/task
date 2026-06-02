from task_manager.validation import (
    validate_task_name,
    validate_task_index
)


def add_task(tasks):
    """
    Add a new task.
    """
    task_name = input("Enter task name: ")

    if validate_task_name(task_name):
        task = {
            "name": task_name,
            "completed": False
        }

        tasks.append(task)
        print("Task added successfully.")


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
        print("Task marked as complete.")


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
        print(f"{i}. {task['name']} [{status}]")


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
        print(f"{i}. {task['name']}")


def track_progress(tasks):
    """
    Show task completion progress.
    """
    if not tasks:
        print("No tasks available.")
        return

    completed = sum(
        1 for task in tasks
        if task["completed"]
    )

    total = len(tasks)

    progress = (completed / total) * 100

    print(f"\nProgress: {completed}/{total} tasks completed")
    print(f"Completion Rate: {progress:.2f}%")