import json
import os

class Task:
    def __init__(self, task_id, title, completed=False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['title'], data['completed'])

class TodoList:
    def __init__(self, filename='todos.json'):
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                content = f.read().strip()
                if content:  # Only parse if file has content
                    data = json.loads(content)
                    self.tasks = [Task.from_dict(task) for task in data]
                    if self.tasks:
                        self.next_id = max(task.id for task in self.tasks) + 1

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    def add_task(self, title):
        task = Task(self.next_id, title)
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        print(f"Task added: {task.title} (ID: {task.id})")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"ID: {task.id} | Title: {task.title} | Status: {status}")

    def update_task(self, task_id, new_title=None, toggle_complete=None):
        for task in self.tasks:
            if task.id == task_id:
                if new_title:
                    task.title = new_title
                if toggle_complete is not None:
                    task.completed = not task.completed if toggle_complete else task.completed
                self.save()
                print(f"Task updated: {task.title} (ID: {task.id})")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save()
        print(f"Task with ID {task_id} deleted.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo App Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Enter task ID: "))
                print("Update options:")
                print("a. Change title")
                print("b. Toggle completion status")
                sub_choice = input("Enter option (a/b): ")
                if sub_choice == 'a':
                    new_title = input("Enter new title: ")
                    todo_list.update_task(task_id, new_title=new_title)
                elif sub_choice == 'b':
                    todo_list.update_task(task_id, toggle_complete=True)
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid ID.")
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo_list.delete_task(task_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()