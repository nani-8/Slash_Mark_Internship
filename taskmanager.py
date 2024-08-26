import datetime
import random
class Task:
    def __init__(self, description, priority=0):
        self.description = description
        self.priority = priority
        self.created_at = datetime.datetime.now()

    def __str__(self):
        return f"{self.priority}: {self.description}"
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority=0):
        task = Task(description, priority)
        self.tasks.append(task)

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i}: {task}")

    def prioritize_task(self, task_index, new_priority):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].priority = new_priority

    def recommend_task(self):
        random.shuffle(self.tasks)  # For simplicity, recommend a random task
        return self.tasks[0]
def main():
    task_manager = TaskManager()

    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. List tasks")
        print("4. Prioritize task")
        print("5. Recommend task")
        print("6. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            description = input("Enter task description: ")
            priority = int(input("Enter priority (0-10): "))
            task_manager.add_task(description, priority)
        elif choice == 2:
            task_index = int(input("Enter task index to remove: "))
            task_manager.remove_task(task_index)
        elif choice == 3:
            task_manager.list_tasks()
        elif choice == 4:
            task_index = int(input("Enter task index to prioritize: "))
            new_priority = int(input("Enter new priority (0-10): "))
            task_manager.prioritize_task(task_index, new_priority)
        elif choice == 5:
            recommended_task = task_manager.recommend_task()
            print("Recommended task:")
            print(recommended_task)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()