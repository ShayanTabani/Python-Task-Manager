# empty list to store our tasks
tasks = []

def show_tasks():
    # check if there are no tasks
    if not tasks:
        print("\n📂 No tasks available right now!")
    else:
        print("\n📋 Your Tasks:")
        # loop through tasks and print them with numbers
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

# main loop to keep the app running
while True:
    print("\n--- 🛠️ TASK MANAGER ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Delete a task")
    print("4. Exit")

    choice = input("Select an option (1/2/3/4): ")

    if choice == '1':
        new_task = input("Enter task name: ")
        tasks.append(new_task) # add task to the end of the list
        print(f"✅ '{new_task}' added successfully!")
        
    elif choice == '2':
        show_tasks()
        
    elif choice == '3':
        show_tasks()
        if tasks:
            try:
                task_num = int(input("Enter task number to delete: "))
                # check if the number is within our list range
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"🗑️ '{removed}' deleted!")
                else:
                    print("⚠️ Invalid number!")
            except ValueError:
                print("⚠️ Please enter a valid number.")
                
    elif choice == '4':
        print("👋 Goodbye! Exiting app...")
        break # stop the loop
        
    else:
        print("⚠️ Invalid choice. Try again.")