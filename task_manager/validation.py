def validate_task_name(task_name):
    """
    Validate task name input.
    """
    if not task_name.strip():
        print("Error: Task name cannot be empty.")
        return False
    return True


def validate_task_index(index, tasks):
    """
    Validate task number entered by user.
    """
    try:
        index = int(index)

        if index < 1 or index > len(tasks):
            print("Error: Task number out of range.")
            return False

        return True

    except ValueError:
        print("Error: Please enter a valid number.")
        return False