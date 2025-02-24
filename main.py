from colorama import Fore, Style, init
from datetime import datetime, timedelta
import re
init(autoreset=True)


# print task list
# add task / remove task / mark task as done / set deadline for task /    view tasks / exit
# -a clean / -d clean /       -c clean      / -t clean 12:43:29 2-24-2025/  -view / -exit

def add_task(task):
    try:
        hours = int(input("How many hours from now is the deadline? "))
    except ValueError:
        print(Fore.RED + Style.BRIGHT + "Invalid input! Please enter a number.")
        return
    deadline = datetime.now() + timedelta(hours=hours)
    formatted_deadline = deadline.strftime("%Y-%m-%d %I:%M %p")

    with open('Tasks', 'a') as file:
        file.write(f"Task: {task.capitalize()} | Deadline: {formatted_deadline}\n")

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"The task {task} has been added and set to {formatted_deadline}")


def remove_task(task):
    with open("Tasks", 'r') as file:
        tasks = file.readlines()

    if len(tasks) == 1:
        with open('Tasks', 'w') as file:
            file.write('')
        print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"The task '{task}' has been removed")
        return

    if task.lower() not in "".join(tasks).lower():
        print("Task not found")
        return

    updated_tasks = [line for line in tasks if task.lower() != line.split("|")[0].replace("Task:", "").strip().lower()]

    with open('Tasks', 'w') as file:
        file.writelines(updated_tasks)

    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"The task '{task}' has been removed")



def mark_task_done(task):
    with open("Tasks", "r") as file:
        tasks = file.readlines()
    updated_tasks = []
    task_found = False
    for line in tasks:
        task_name = line.split("|")[0].replace("Task:", "").strip().lower()
        if task_name == task.lower():
            updated_tasks.append(f"Task: {task.capitalize()} | Deadline: Task done\n")
            task_found = True
        else:
            updated_tasks.append(line)
    if not task_found:
        print("Task not found")
        return
    with open("Tasks", "w") as file:
        file.writelines(updated_tasks)

    print(f"✅ The task '{task}' has been marked as DONE!")


def change_deadline(task, hours):
    deadline = datetime.now() + timedelta(hours=hours)
    formatted_deadline = deadline.strftime("%Y-%m-%d %I:%M %p")
    with open('Tasks', 'r') as file:
        tasks = file.readlines()
    if task.lower() not in "".join(tasks).lower():
        print("Task not found")
        return
    updated_tasks = []
    for line in tasks:
        task_name = line.split("|")[0].replace("Task:", "").strip().lower()
        if task_name == task.lower():
            updated_tasks.append(f"Task: {task.capitalize()} | Deadline: {formatted_deadline}\n")
        else:
            updated_tasks.append(line)
    with open("Tasks", "w") as file:
        file.writelines(updated_tasks)
    print(Fore.LIGHTGREEN_EX + Style.BRIGHT + f"Task {task} deadline has been set to {formatted_deadline}")


def show_tasks(filename="Tasks"):
    with open(filename, "r") as file:
        tasks = file.readlines()

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task.strip()}")


def main():
    print(
        "Welcome to your task system")
    print("Type -help for help: ")
    x = ''
    while x.lower().strip() != '-q':
        x = input()
        if x.lower().strip() == '-q': break
        if x.lower() == '-help':
            print("#### Commands list ####")
            print("-a (task name) adds a new task")
            print("-d (task name) removes a task")
            print("-time (task name) (number of hours) updates a deadline")
            print("-v shows all tasks")
            print("-q quits the program")
        elif x.lower().strip().split()[0] == '-a':
            add_task(x.split("-a")[1].strip())

        elif x.lower().strip().split()[0] == '-d':
            remove_task(x.split("-d")[1].strip())

        elif x.lower().split()[0] == '-time':
            string = x.split("-time")[1].strip()
            words = re.findall(r'\b[a-zA-Z]+\b', string)
            numbers = re.findall(r'\b\d+\b', string)
            change_deadline(" ".join(words) , int("".join(numbers)))
        elif x.lower().split()[0] == '-v':
            show_tasks()

        else: print(Fore.RED + Style.BRIGHT + "Command not found! do -help")
if __name__ == '__main__':
    main()
