def display_menu():
    print("\nWelcome to the To-Do List App\n")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(task_list):
    task_title = input("Enter the task title: ").strip()
    if task_title:
        task_list.append({"title": task_title, "status": "Incomplete"})
        print("Task added successfully!")
    else:
        print("Task title not valid. Please enter valid task title")

def view_tasks(task_list):
    if not task_list:
        print("No tasks at the moment.")
    else:
        print("\nTasks:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task['title']} - {task['status']}")
            

def mark_task_complete(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Enter the task number to mark complete: "))
        if 1 <= task_number <= len(task_list):
            task_list[task_number - 1]["status"] = "Complete"
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(task_list):
    view_tasks(task_list)
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(task_list):
            removed_task = task_list.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else: 
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    task_list = []
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            mark_task_complete(task_list)
        elif choice == "4":
            delete_task(task_list)
        elif choice == "5":
            print("Thank you for using our To-Do List App!")
            break
        else: 
            print("Invalid choice. Please select a number between 1 and 5. Options shown below!")

if __name__ == "__main__":
    main()


