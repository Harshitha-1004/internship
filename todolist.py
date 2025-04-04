import json
import datetime

TASKS_FILE = "tasks.json"
LAST_DATE_FILE = "last_date.txt"

DAILY_ROUTINE_TASKS = [
    "Exercise",
    "Study",
    "Sleep at least 7 hours",
    "Drink enough water",
    "Read something new"
]

class Task:
    def __init__(self, title, due_date=None):
        self.title = title
        self.due_date = due_date
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "completed": self.completed
        }

    @staticmethod
    def from_dict(data):
        task = Task(data["title"], data["due_date"])
        task.completed = data["completed"]
        return task

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return [Task.from_dict(t) for t in json.load(f)]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task.completed else "✖"
        due = f"(Due: {task.due_date})" if task.due_date else ""
        print(f"{idx}. {task.title} {due} [{status}]")

def add_task(tasks):
    title = input("Enter task title: ")
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    due = due if due else None
    tasks.append(Task(title, due))

def mark_complete(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Mark which task as complete? ")) - 1
        if 0 <= i < len(tasks):
            tasks[i].completed = True
            print("Marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        i = int(input("Delete which task? ")) - 1
        if 0 <= i < len(tasks):
            del tasks[i]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def get_today_str():
    return datetime.date.today().isoformat()

def load_last_date():
    try:
        with open(LAST_DATE_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def save_today_date():
    with open(LAST_DATE_FILE, "w") as f:
        f.write(get_today_str())

def add_daily_routines(tasks):
    today = get_today_str()
    task_titles = [t.title for t in tasks if t.due_date == today]

    for routine in DAILY_ROUTINE_TASKS:
        if routine not in task_titles:
            tasks.append(Task(routine, today))

def check_and_add_daily_tasks(tasks):
    last_date = load_last_date()
    today = get_today_str()
    if last_date != today:
        add_daily_routines(tasks)
        save_today_date()

def main():
    tasks = load_tasks()
    check_and_add_daily_tasks(tasks)

    while True:
        print("\n--- To-Do List ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Save and exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
