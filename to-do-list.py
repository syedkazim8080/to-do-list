import os

# First of all creat a file in which we store a tasks
FILE_NAME = "task.txt"
# Then make a function for every task
def load_task():

    tasks = []

    if not os.path.exists(FILE_NAME):
        return tasks

    with open(FILE_NAME, "r") as file:

        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.rsplit("|", 1)

            if len(parts) == 2:
                title, status = parts
                tasks.append({"title": title.strip(), "completed": status.strip() == "DONE"})

    return tasks

def save_task(tasks):

    with open(FILE_NAME, "w") as file:

        for task in tasks:
            status = "DONE" if task["completed"] else "PENDING"
            file.write(f"{task['title']} | {status}\n")

def add_task(tasks):

    title = input("Enter your task name: ").strip()

    if not title:
        print("Please enter any task!")
        return

    print("Your task is:", title)

    tasks.append({"title": title, "completed": False})
    save_task(tasks)
    print(f"Task '{title}' added successfully!")

def view_task(tasks):

    if not tasks:
        print("No task added!")
        return

    print("\n------- YOUR TASKS -------")

    for number, task in enumerate(tasks, start=1):
        status = "[✔] Done" if task["completed"] else "Pending"
        print(f"{number}. {task['title']}  -  {status}")

def get_task_number(tasks, action):

    view_task(tasks)

    if not tasks:
        return None

    try:

        number = int(input(f"Enter the task number to {action}: "))

        if 1 <= number <= len(tasks):
            return number - 1

        print("Enter a valid task number!")

    except ValueError:

        print("Enter a valid number!")

    return None

def mark_completed(tasks):

    index = get_task_number(tasks, "mark as completed")

    if index is None:
        return

    if tasks[index]["completed"]:
        print("Task is already completed!")
        return

    tasks[index]["completed"] = True
    save_task(tasks)
    print(f"Task '{tasks[index]['title']}' marked as completed!")

def delete_task(tasks):

    index = get_task_number(tasks, "delete")

    if index is None:
        return

    removed = tasks.pop(index)
    save_task(tasks)
    print(f"Task '{removed['title']}' is deleted!")
# Then show a tasks in which you select a task
def SHOW_MENU():

    print("\n-----SHOW MENU-----")
    print("1. Add task")
    print("2. View task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")
# Then implemention of task which you select
def main():

    tasks = load_task()

    while True:

        SHOW_MENU()
        choice = input("Enter your option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_task(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            save_task(tasks)
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

print("-----DONE-----")