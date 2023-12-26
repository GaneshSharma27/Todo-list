# Making a To-Do list App which will store your task's data in a csv or txt file
# You can add more tasks, delete tasks and list them all together

def add_tasks(str):
    with open("new_file_tasks.txt", "a") as file:
        file.write(f"{str}\n")

def remove_tasks(int):
    tasks_list = []
    with open("new_file_tasks.txt", "r") as file:
        for line in file:
            tasks_list.append(line.rstrip())
    try:
        tasks_list.pop(int - 1)
        with open("new_file_tasks.txt", "w") as file:
            for each_task_in_list in tasks_list:
                file.write(f"{each_task_in_list}\n")
    except IndexError:
        print("Please select the number within task range!")

def list_tasks():
    with open("new_file_tasks.txt", "r") as file:
        all_tasks = file.readlines()
    
    print("\nYour tasks:")
    if (len(all_tasks) == 0):
        print("----No tasks entered!----\n")
    else:
        for i in range(0, len(all_tasks)):
            print(f"{i + 1}. {all_tasks[i].strip()}")
        print("\n")

def clear_all_tasks():
    with open("new_file_tasks.txt", "w") as file:
        file.close()

def main():
    while True:
        try:
            list_tasks()
            print("----Please select any one!----")
            print("1. Add task\n2. Remove a tasks\n3. List all tasks\n4. Clear all tasks")
            choose_command = int(input("Choose any number from 1, 2, 3 and 4: "))
            match(choose_command):
                case 1:
                    print("-------------------------------------------")
                    task = input("Task: ")
                    add_tasks(task)
                case 2:
                    print("-------------------------------------------")
                    remove_task_number = int(input("\nTask's number you want to remove: "))
                    remove_tasks(remove_task_number)
                case 3:
                    print("-------------------------------------------")
                    list_tasks()
                case 4:
                    clear_all_tasks()
                case _:
                    print("Enter values from 1, 2 and 3!")
        except ValueError:
            print("Only integer values are acceptable!")
            pass
        print("-------------------------------------------")

if __name__ == "__main__":
    main()
