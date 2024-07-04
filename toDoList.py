# from datetime import datetime

# class Task:
#     def __init__(self, description, due_date=None, tags=None):
#         self.description = description
#         self.due_date = due_date
#         self.tags = tags or []
#         self.completed = False

#     def mark_completed(self):
#         self.completed = True

#     def __str__(self):
#         status = "Completed" if self.completed else "Pending"
#         due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else "No due date"
#         return f"{self.description} - {status}, Due: {due_date_str}, Tags: {', '.join(self.tags)}"

# class TaskBuilder:
#     def __init__(self, description):
#         self.description = description
#         self.due_date = None
#         self.tags = []

#     def set_due_date(self, due_date):
#         self.due_date = due_date
#         return self

#     def add_tag(self, tag):
#         self.tags.append(tag)
#         return self

#     def build(self):
#         return Task(self.description, self.due_date, self.tags)

# class Memento:
#     def __init__(self, state):
#         self.state = state

# class TaskManager:
#     def __init__(self):
#         self.tasks = []
#         self.history = []
#         self.redo_stack = []

#     def add_task(self, task):
#         self._save_state()
#         self.tasks.append(task)

#     def mark_task_completed(self, description):
#         for task in self.tasks:
#             if task.description == description:
#                 self._save_state()
#                 task.mark_completed()
#                 break

#     def delete_task(self, description):
#         self._save_state()
#         self.tasks = [task for task in self.tasks if task.description != description]

#     def _save_state(self):
#         self.history.append(Memento(self.tasks.copy()))
#         self.redo_stack.clear()

#     def undo(self):
#         if self.history:
#             memento = self.history.pop()
#             self.redo_stack.append(Memento(self.tasks.copy()))
#             self.tasks = memento.state

#     def redo(self):
#         if self.redo_stack:
#             memento = self.redo_stack.pop()
#             self.history.append(Memento(self.tasks.copy()))
#             self.tasks = memento.state

#     def view_tasks(self, filter_by=None):
#         if filter_by == "completed":
#             return [task for task in self.tasks if task.completed]
#         elif filter_by == "pending":
#             return [task for task in self.tasks if not task.completed]
#         return self.tasks

#     def __str__(self):
#         return "\n".join(str(task) for task in self.tasks)

# def main():
#     manager = TaskManager()

#     while True:
#         print("\nTo-Do List Manager")
#         print("1. Add Task")
#         print("2. Mark Task as Completed")
#         print("3. Delete Task")
#         print("4. View All Tasks")
#         print("5. View Completed Tasks")
#         print("6. View Pending Tasks")
#         print("7. Undo")
#         print("8. Redo")
#         print("9. Exit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             description = input("Enter task description: ")
#             due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
#             tags_str = input("Enter tags (comma-separated) or leave empty: ")

#             builder = TaskBuilder(description)

#             if due_date_str:
#                 due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
#                 builder.set_due_date(due_date)

#             if tags_str:
#                 tags = tags_str.split(',')
#                 for tag in tags:
#                     builder.add_tag(tag.strip())

#             task = builder.build()
#             manager.add_task(task)
#             print("Task added successfully.")

#         elif choice == '2':
#             description = input("Enter task description to mark as completed: ")
#             manager.mark_task_completed(description)
#             print("Task marked as completed.")

#         elif choice == '3':
#             description = input("Enter task description to delete: ")
#             manager.delete_task(description)
#             print("Task deleted.")

#         elif choice == '4':
#             print("All Tasks:")
#             print(manager)

#         elif choice == '5':
#             print("Completed Tasks:")
#             for task in manager.view_tasks("completed"):
#                 print(task)

#         elif choice == '6':
#             print("Pending Tasks:")
#             for task in manager.view_tasks("pending"):
#                 print(task)

#         elif choice == '7':
#             manager.undo()
#             print("Undid the last action.")

#         elif choice == '8':
#             manager.redo()
#             print("Redid the last undone action.")

#         elif choice == '9':
#             print("Exiting the To-Do List Manager.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

#---------------------------------------------------------------------------------------------------------------------------------------------------

# import pickle
# from datetime import datetime

# class Task:
#     def __init__(self, description, due_date=None, tags=None):
#         self.description = description
#         self.due_date = due_date
#         self.tags = tags or []
#         self.completed = False

#     def mark_completed(self):
#         self.completed = True

#     def __str__(self):
#         status = "Completed" if self.completed else "Pending"
#         due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else "No due date"
#         return f"{self.description} - {status}, Due: {due_date_str}, Tags: {', '.join(self.tags)}"

# class TaskBuilder:
#     def __init__(self, description):
#         self.description = description
#         self.due_date = None
#         self.tags = []

#     def set_due_date(self, due_date):
#         self.due_date = due_date
#         return self

#     def add_tag(self, tag):
#         self.tags.append(tag)
#         return self

#     def build(self):
#         return Task(self.description, self.due_date, self.tags)

# class Memento:
#     def __init__(self, state):
#         self.state = state

# class TaskManager:
#     def __init__(self):
#         self.tasks = []
#         self.history = []
#         self.redo_stack = []
#         self.load_tasks()

#     def add_task(self, task):
#         self._save_state()
#         self.tasks.append(task)
#         self.save_tasks()

#     def mark_task_completed(self, description):
#         for task in self.tasks:
#             if task.description == description:
#                 self._save_state()
#                 task.mark_completed()
#                 self.save_tasks()
#                 break

#     def delete_task(self, description):
#         self._save_state()
#         self.tasks = [task for task in self.tasks if task.description != description]
#         self.save_tasks()

#     def _save_state(self):
#         self.history.append(Memento(self.tasks.copy()))
#         self.redo_stack.clear()

#     def undo(self):
#         if self.history:
#             memento = self.history.pop()
#             self.redo_stack.append(Memento(self.tasks.copy()))
#             self.tasks = memento.state
#             self.save_tasks()

#     def redo(self):
#         if self.redo_stack:
#             memento = self.redo_stack.pop()
#             self.history.append(Memento(self.tasks.copy()))
#             self.tasks = memento.state
#             self.save_tasks()

#     def view_tasks(self, filter_by=None):
#         if filter_by == "completed":
#             return [task for task in self.tasks if task.completed]
#         elif filter_by == "pending":
#             return [task for task in self.tasks if not task.completed]
#         return self.tasks

#     def save_tasks(self):
#         with open('tasks.pkl', 'wb') as file:
#             pickle.dump(self.tasks, file)

#     def load_tasks(self):
#         try:
#             with open('tasks.pkl', 'rb') as file:
#                 self.tasks = pickle.load(file)
#         except FileNotFoundError:
#             self.tasks = []

#     def __str__(self):
#         return "\n".join(str(task) for task in self.tasks)

# def main():
#     manager = TaskManager()

#     while True:
#         print("\nTo-Do List Manager")
#         print("1. Add Task")
#         print("2. Mark Task as Completed")
#         print("3. Delete Task")
#         print("4. View All Tasks")
#         print("5. View Completed Tasks")
#         print("6. View Pending Tasks")
#         print("7. Undo")
#         print("8. Redo")
#         print("9. Exit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             description = input("Enter task description: ")
#             due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
#             tags_str = input("Enter tags (comma-separated) or leave empty: ")

#             builder = TaskBuilder(description)

#             if due_date_str:
#                 due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
#                 builder.set_due_date(due_date)

#             if tags_str:
#                 tags = tags_str.split(',')
#                 for tag in tags:
#                     builder.add_tag(tag.strip())

#             task = builder.build()
#             manager.add_task(task)
#             print("Task added successfully.")

#         elif choice == '2':
#             description = input("Enter task description to mark as completed: ")
#             manager.mark_task_completed(description)
#             print("Task marked as completed.")

#         elif choice == '3':
#             description = input("Enter task description to delete: ")
#             manager.delete_task(description)
#             print("Task deleted.")

#         elif choice == '4':
#             print("All Tasks:")
#             print(manager)

#         elif choice == '5':
#             print("Completed Tasks:")
#             for task in manager.view_tasks("completed"):
#                 print(task)

#         elif choice == '6':
#             print("Pending Tasks:")
#             for task in manager.view_tasks("pending"):
#                 print(task)

#         elif choice == '7':
#             manager.undo()
#             print("Undid the last action.")

#         elif choice == '8':
#             manager.redo()
#             print("Redid the last undone action.")

#         elif choice == '9':
#             print("Exiting the To-Do List Manager.")
#             break

#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()


#--------------------------------------------------------------------------------------------------------------------------------------

import pickle
from datetime import datetime, timedelta

class Task:
    def __init__(self, description, due_date=None, tags=None):
        self.description = description
        self.due_date = due_date
        self.tags = tags or []
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = self.due_date.strftime('%Y-%m-%d') if self.due_date else "No due date"
        return f"{self.description} - {status}, Due: {due_date_str}, Tags: {', '.join(self.tags)}\n"

class TaskBuilder:
    def __init__(self, description):
        self.description = description
        self.due_date = None
        self.tags = []

    def set_due_date(self, due_date):
        self.due_date = due_date
        return self

    def add_tag(self, tag):
        self.tags.append(tag)
        return self

    def build(self):
        return Task(self.description, self.due_date, self.tags)

class Memento:
    def __init__(self, state):
        self.state = state

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.history = []
        self.redo_stack = []
        self.load_tasks()

    def add_task(self, task):
        self._save_state()
        self.tasks.append(task)
        self.save_tasks()

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                self._save_state()
                task.mark_completed()
                self.save_tasks()
                break

    def delete_task(self, description):
        self._save_state()
        self.tasks = [task for task in self.tasks if task.description != description]
        self.save_tasks()

    def _save_state(self):
        self.history.append(Memento(self.tasks.copy()))
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            memento = self.history.pop()
            self.redo_stack.append(Memento(self.tasks.copy()))
            self.tasks = memento.state
            self.save_tasks()

    def redo(self):
        if self.redo_stack:
            memento = self.redo_stack.pop()
            self.history.append(Memento(self.tasks.copy()))
            self.tasks = memento.state
            self.save_tasks()

    def view_tasks(self, filter_by=None):
        if filter_by == "completed":
            return [task for task in self.tasks if task.completed]
        elif filter_by == "pending":
            return [task for task in self.tasks if not task.completed]
        return self.tasks

    def save_tasks(self):
        with open('tasks.pkl', 'wb') as file:
            pickle.dump(self.tasks, file)

    def load_tasks(self):
        try:
            with open('tasks.pkl', 'rb') as file:
                self.tasks = pickle.load(file)
        except FileNotFoundError:
            self.tasks = []

    def __str__(self):
        return "\n".join(str(task) for task in self.tasks)

def valid_date(input_date):
    try:
        due_date = datetime.strptime(input_date, '%Y-%m-%d')
        if due_date < datetime.now():
            print("The due date cannot be in the past. Please enter a future date.")
            return False
        return due_date
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return False

def main():
    manager = TaskManager()

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. View Completed Tasks")
        print("6. View Pending Tasks")
        print("7. Undo")
        print("8. Redo")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            while True:
                due_date_str = input("Enter due date (YYYY-MM-DD) or leave empty: ")
                if due_date_str == "":
                    due_date = None
                    break
                else:
                    due_date = valid_date(due_date_str)
                    if due_date:
                        break
            tags_str = input("Enter tags (comma-separated) or leave empty: ")

            builder = TaskBuilder(description)

            if due_date:
                builder.set_due_date(due_date)

            if tags_str:
                tags = tags_str.split(',')
                for tag in tags:
                    builder.add_tag(tag.strip())

            task = builder.build()
            manager.add_task(task)
            print("Task added successfully.")

        elif choice == '2':
            description = input("Enter task description to mark as completed: ")
            manager.mark_task_completed(description)
            print("Task marked as completed.")

        elif choice == '3':
            description = input("Enter task description to delete: ")
            manager.delete_task(description)
            print("Task deleted.")

        elif choice == '4':
            print("All Tasks:")
            print(manager)

        elif choice == '5':
            print("Completed Tasks:")
            for task in manager.view_tasks("completed"):
                print(task)

        elif choice == '6':
            print("Pending Tasks:")
            for task in manager.view_tasks("pending"):
                print(task)

        elif choice == '7':
            manager.undo()
            print("Undid the last action.")

        elif choice == '8':
            manager.redo()
            print("Redid the last undone action.")

        elif choice == '9':
            print("Exiting the To-Do List Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


































