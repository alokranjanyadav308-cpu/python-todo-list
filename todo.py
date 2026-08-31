import json
import os

FILE = "tasks.json"


def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks():
    with open(FILE, "w") as file:
        json.dump(tasks, file, indent=4)


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter your task: ")
        tasks.append({"task": task, "done": False})
        save_tasks()
        print("✅ Task added and saved!")

    elif choice == "2":
        if not tasks:
            print("📭 No tasks yet.")
        else:
            print("\nYour Tasks:")
            for i, item in enumerate(tasks, 1):
                status = "✅" if item["done"] else "❌"
                print(f"{i}. {status} {item['task']}")

    elif choice == "3":
        if not tasks:
            print("📭 No tasks yet.")
        else:
            number = int(input("Enter task number to complete: "))

            if 1 <= number <= len(tasks):
                tasks[number - 1]["done"] = True
                save_tasks()
                print("🎉 Task completed and saved!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("📭 No tasks yet.")
        else:
            number = int(input("Enter task number to delete: "))

            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                save_tasks()
                print(f"🗑️ Deleted: {deleted['task']}")
            else:
                print("❌ Invalid task number.")

    elif choice == "5":
        print("👋 Goodbye!")
        break

    else:
        print("❌ Invalid option.")
