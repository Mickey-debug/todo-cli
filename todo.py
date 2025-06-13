import json
import os
import sys

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return[]
    with open(TASKS_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return[]
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    tasks.append({
        "title": title,
        "status": "todo"
    })
    save_tasks(tasks)
    print(f"✅ Task added: {title}")

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet.")
        return
    
    found = False
    for i, task in enumerate(tasks, 1):
        if filter_status is None or task["status"] == filter_status:
            print(f"{i}. [{task['status']}] {task['title']}")
            found = True
    if not found:
        print(f"📭 No tasks with status '{filter_status}'.")

def delete_task(index):
    tasks = load_tasks()
    if index < 1 or index > len(tasks):
        print("❌ Invalid task number.")
        return
    removed = tasks.pop(index - 1)
    save_tasks(tasks)
    print(f"🗑️ Deleted: {removed['title']}")

def mark_task(index, status):
    tasks = load_tasks()
    valid_statuses = ["todo", "in-progress", "done"]
    if status not in valid_statuses:
        print(f"❌ Invalid status. Use one of: {', '.join(valid_statuses)}")
        return
    if index < 1 or index > len(tasks):
        print("❌ Invalid task number.")
        return
    tasks[index - 1]["status"] = status
    save_tasks(tasks)
    print(f"✅ Task {index} marked as {status}")



def main():
    if len(sys.argv) < 2:
        print("❌ Please enter a command (e.g., add, list, etc.)")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("❌ Please provide a task title.")
            return
        title = sys.argv[2]
        add_task(title)

    elif command == "list":
        if len(sys.argv) == 3:
            filter_status = sys.argv[2]
            valid_statuses = ["todo", "in-progress", "done"]
            if filter_status not in valid_statuses:
                print(f"❌ Invalid status. Use: {', '.join(valid_statuses)}")
                return
            list_tasks(filter_status)
        else:
            list_tasks()

    elif command == "delete":
        if len(sys.argv) < 3:
            print("❌ Please provide the task number to delete.")
            return
        try:
            index = int(sys.argv[2])
            delete_task(index)
        except ValueError:
            print("❌ Please enter a valid number.")

    elif command == "mark":
        if len(sys.argv) < 4:
            print("❌ Usage: python todo.py mark <task_number> <status>")
            return
        try:
            index = int(sys.argv[2])
            status = sys.argv[3]
            mark_task(index, status)
        except ValueError:
            print("❌ Task number must be a valid number.")

    else:
        print("❌ Unknown command.")

if __name__ == "__main__":
    main()