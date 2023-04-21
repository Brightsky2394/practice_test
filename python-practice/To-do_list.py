#!/usr/bin/python3

print("To-do list")
tasks = []


def add_task():
    task = input("Enter a task: ")
    tasks.append(task)


def remove_task():
    task = input("Enter task to be remove: ")
    tasks.remove(task) if task in tasks else print("task not found")


def display_task():
    if not tasks:
        print("Tasks list is empty")
    else:
        for j, task in enumerate(tasks):
            print("{}.{}".format(j + 1, task))


def complete_task():
    task = input("Enter the completed task: ")
    index = tasks.index(task)
    tasks[index] = f"[x] {task}"
    print(tasks[index])


def sort_tasks():
    tasks.sort()


def main():
    approve = False
    while not approve:
        print("""
        To-do list manager
        1. add a task
        2. remove a task
        3. display tasks
        4. complete task
        5. sort tasks list
        6. Exit
        """)
        choice = input("Enter a choice: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            remove_task()
        elif choice == '3':
            display_task()
        elif choice == '4':
            complete_task()
        elif choice == '5':
            sort_tasks()
        elif choice == '6':
            print("Program Terminated")
            break
        else:
            print("Incorrect choice")


if __name__ == "__main__":
    main()

