# 📝 To-Do CLI App

A simple command-line application to help you manage your tasks. You can add, update, delete, and mark tasks as done or in progress — all from the terminal!

## 🚀 Features

- Add a task
- Update a task
- Delete a task
- Mark tasks as done or in progress
- List all tasks
- Filter tasks by status (done, not done, in progress)
- Saves your data in a local JSON file

## 🛠️ How to Run

Make sure you have Python installed.

### 1. Open your terminal  
### 2. Run the app like this:

```bash
python todo.py add "Buy groceries"
python todo.py update 1 "Buy groceries and cook"
python todo.py delete 2
python todo.py mark 3 in-progress
python todo.py list
python todo.py list done
python todo.py list not-done
python todo.py list in-progress
