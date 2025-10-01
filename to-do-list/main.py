def add_task():
    new_task = input("New Task: ")

    if new_task.isspace():
        return

    with open("to-do-list.txt", "a") as file:
        file.write(new_task)


def remove_task():
    try:
        task_number = int(input("Task Number: "))
    except ValueError:
        return

    with open("to-do-list.txt", "r") as file:
        lines = file.readlines()

    with open("to-do-list.txt", "w") as file:
        for i, line in enumerate(lines, start=1):
            if i != task_number:
                file.write(line)


def replace_task():
    try:
        task_number = int(input("Task Number: "))
    except ValueError:
        return

    new_task = input("New Task: ")

    if new_task.isspace():
        return

    with open("to-do-list.txt", "r") as file:
        lines = file.readlines()

    with open("to-do-list.txt", "w") as file:
        for i, line in enumerate(lines, start=1):
            if i != task_number:
                file.write(line)
            else:
                file.write(new_task)


def list_tasks():
    with open("to-do-list.txt", "r") as file:
        lines = file.readlines()
        if not lines:
            print("No tasks")
        else:
            for i, line in enumerate(lines, start=1):
                print(f"{i}. {line.strip()}")


def help():
    print("Commands")
    print("add - Add a task to the list.")
    print("rm | remove - Remove a task from the list.")
    print("ls | list - List the tasks")
    print("r | replace - Replace a task on the list.")
    print("q | quit - Quit.")
    print("h | help - Help.")


def unknown():
    print("Command does not exist.")


def main() -> None:
    while True:
        command = input("Command: ").lower().strip()
        if command == "add":
            add_task()
        elif command in ["rm", "remove"]:
            remove_task()
        elif command in ["ls", "list"]:
            list_tasks()
        elif command in ["r", "replace"]:
            replace_task()
        elif command in ["q", "quit"]:
            break
        elif command in ["h", "help"]:
            help()
        else:
            unknown()


if __name__ == "__main__":
    main()
