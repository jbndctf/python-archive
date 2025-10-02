"""
To Do List

A to do list program where you can add, remove, edit, and list tasks.
"""

FILE_NAME: str = "to-do-list.txt"


HELP_MESSAGE: str = """Commands
add: Add a task.
remove: Remove a task.
edit: Edit a task.
list: List all tasks.
quit: Quit program.
help: Help.
"""
INVALID_TASK_MESSAGE: str = "Invalid task."
INVALID_TASK_NUMBER_MESSAGE: str = "Invalid task number."
UNKNOWN_COMMAND_MESSAGE: str = "Command does not exist."
EMPTY_TASKS_MESSAGE: str = "No tasks."

TASK_PROMPT: str = "Enter a new task: "
TASK_NUMBER_PROMPT: str = "Enter a task number: "
COMMAND_PROMPT: str = "Enter a command: "


def prompt_task() -> str:
    """
    Prompts for task.

    Returns:
        str: A task inputted from the user.
    """
    return input(TASK_PROMPT)


def prompt_task_number() -> int:
    """
    Prompts for task number.

    Returns:
        int: A task number inputted from the user.
    """
    return int(input(TASK_NUMBER_PROMPT))


def get_tasks() -> list[str]:
    """
    Reads tasks from file.

    Returns:
        list[str]: A list of the tasks read from the file.
    """
    with open(FILE_NAME, "r") as file:
        return file.readlines()


def is_valid_task_number(task_number: int, tasks: list[str]) -> bool:
    """
    Checks if task number is within the valid range [1, len(tasks)]

    Returns:
        bool: True, if the number is within the valid range, False otherwise.
    """
    return 1 <= task_number <= len(tasks)


def add_task() -> None:
    """
    Prompts and adds task when the add command is entered.
    """
    new_task: str = prompt_task()

    if not new_task:
        print(INVALID_TASK_MESSAGE)
        return

    with open(FILE_NAME, "a") as file:
        file.write(new_task)


def remove_task() -> None:
    """
    Prompts and remove task when the remove command is entered.
    """
    try:
        task_number: int = prompt_task_number()
    except ValueError:
        print(INVALID_TASK_NUMBER_MESSAGE)
        return

    tasks: list[str] = get_tasks()

    if not is_valid_task_number(task_number, tasks):
        print(INVALID_TASK_NUMBER_MESSAGE)
        return

    with open(FILE_NAME, "w") as file:
        for i, task in enumerate(tasks, start=1):
            if i != task_number:
                file.write(task)


def edit_task() -> None:
    """
    Prompts and edits task when the edit command is entered.
    """
    try:
        task_number: int = prompt_task_number()
    except ValueError:
        print(INVALID_TASK_NUMBER_MESSAGE)
        return

    tasks: list[str] = get_tasks()

    if not is_valid_task_number(task_number, tasks):
        print(INVALID_TASK_NUMBER_MESSAGE)
        return

    new_task: str = prompt_task()

    if not new_task:
        print(INVALID_TASK_MESSAGE)
        return

    with open(FILE_NAME, "w") as file:
        for i, task in enumerate(tasks, start=1):
            if i != task_number:
                file.write(task)
            else:
                file.write(new_task)


def list_tasks() -> None:
    """
    Prints all tasks when the list command is entered.
    """
    tasks: list[str] = get_tasks()

    if not tasks:
        print(EMPTY_TASKS_MESSAGE)
        return

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")


def helper() -> None:
    """
    Prints a message when the help command is entered.
    """
    print(HELP_MESSAGE)


def unknown() -> None:
    """
    Prints a message when an unknown command is entered.
    """
    print(UNKNOWN_COMMAND_MESSAGE)


COMMANDS = {
    "add": add_task,
    "remove": remove_task,
    "list": list_tasks,
    "edit": edit_task,
    "help": helper,
}


def main() -> None:
    """
    To do list program.

    A to do list program where you can add, remove, list or edit tasks.
    """
    while True:
        command: str = input(COMMAND_PROMPT).lower().strip()
        if command in ["quit"]:
            break
        COMMANDS.get(command, unknown)()


if __name__ == "__main__":
    main()
