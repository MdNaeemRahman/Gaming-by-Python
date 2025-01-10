# To-Do List Application

import os

FILE_NAME = "todo_list.txt"


def load_tasks():
    """Load tasks from a file."""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]


def save_tasks(tasks):
    """Save tasks to a file."""
    with open(FILE_NAME, 'w') as file:
        for task in tasks:
            file.write(task + '\n')


def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("\nNo tasks in the to-do list.\n")
        return

    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()


def add_task(tasks):
    """Add a task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!\n")


def delete_task(tasks):
    """Delete a task from the list."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            save_tasks(tasks)
            print(f"Task '{removed_task}' deleted successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def update_task(tasks):
    """Update an existing task."""
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_number = int(input("Enter the task number to update: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_number - 1] = new_task
            save_tasks(tasks)
            print("Task updated successfully!\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")


def main():
    """Main function to run the To-Do List application."""
    tasks = load_tasks()

    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Update task")
        print("5. Exit\n")

        choice = input("Enter your choice: ")
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            update_task(tasks)
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
