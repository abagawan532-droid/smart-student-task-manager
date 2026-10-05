"""
Smart Student Task Manager
A professional command-line productivity application for students.

Author: Altaf Bagawan
Branch: Information Science Engineering
Institution: Bapuji Institute of Engineering & Technology, Davanagere
"""

import json
from pathlib import Path
from datetime import datetime

DATA_FILE = Path("tasks.json")
VALID_PRIORITIES = {"Low", "Medium", "High"}


def load_tasks():
    """Load tasks from the JSON data file."""
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read saved tasks. Starting with an empty list.")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON data file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def next_task_id(tasks):
    """Generate the next available task ID."""
    return max((task.get("id", 0) for task in tasks), default=0) + 1


def choose_priority():
    """Read and validate a task priority."""
    while True:
        priority = input("Priority [Low/Medium/High] (default: Medium): ").strip().title()
        if not priority:
            return "Medium"
        if priority in VALID_PRIORITIES:
            return priority
        print("Please enter Low, Medium, or High.")


def add_task(tasks):
    """Create and store a new task."""
    title = input("Task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    priority = choose_priority()

    task = {
        "id": next_task_id(tasks),
        "title": title,
        "priority": priority,
        "status": "Pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"Task #{task['id']} added successfully.")


def display_tasks(tasks):
    """Display all tasks in a readable format."""
    if not tasks:
        print("\nNo tasks available.")
        return

    print("\n" + "=" * 85)
    print(f"{'ID':<5}{'STATUS':<13}{'PRIORITY':<12}{'TASK':<40}{'CREATED'}")
    print("=" * 85)

    for task in tasks:
        print(
            f"{task['id']:<5}"
            f"{task['status']:<13}"
            f"{task['priority']:<12}"
            f"{task['title'][:38]:<40}"
            f"{task['created_at']}"
        )

    print("=" * 85)


def find_task(tasks, task_id):
    """Find a task by ID."""
    return next((task for task in tasks if task.get("id") == task_id), None)


def get_task_id():
    """Read a valid numeric task ID."""
    try:
        return int(input("Enter task ID: ").strip())
    except ValueError:
        print("Please enter a valid numeric ID.")
        return None


def complete_task(tasks):
    """Mark a pending task as completed."""
    display_tasks(tasks)
    task_id = get_task_id()

    if task_id is None:
        return

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    task["status"] = "Completed"
    save_tasks(tasks)
    print(f"Task #{task_id} marked as completed.")


def delete_task(tasks):
    """Delete a task by ID."""
    display_tasks(tasks)
    task_id = get_task_id()

    if task_id is None:
        return

    task = find_task(tasks, task_id)

    if not task:
        print("Task not found.")
        return

    tasks.remove(task)
    save_tasks(tasks)
    print(f"Task #{task_id} deleted successfully.")


def show_summary(tasks):
    """Display a short task summary."""
    total = len(tasks)
    completed = sum(task.get("status") == "Completed" for task in tasks)
    pending = total - completed

    print("\n--- Task Summary ---")
    print(f"Total tasks     : {total}")
    print(f"Pending tasks   : {pending}")
    print(f"Completed tasks : {completed}")


def main():
    """Run the application."""
    tasks = load_tasks()

    while True:
        print("\n" + "=" * 45)
        print("       SMART STUDENT TASK MANAGER")
        print("=" * 45)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Task Summary")
        print("6. Exit")
        print("=" * 45)

        choice = input("Select an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            show_summary(tasks)
        elif choice == "6":
            print("Thank you for using Smart Student Task Manager.")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
