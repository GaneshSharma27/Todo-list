# Todo-list (Project Summary)
I made a Todo list app based on Python and it runs on Command Line Interface (CLI), it doesn't have any fancy User Interface (UI).
This to-do list saves your tasks in a .txt file which means it doesn't store your tasks in a list or any other data structure which ultimately stores all your data in the memory and you can access those data until you close your program.
I've solved this problem by saving all your tasks to a .txt file which will keep your tasks stored in your secondary memory, which won't clear your tasks until you choose to clear those tasks.
My to-do list app gives you features like adding tasks, removing tasks, listing all the tasks that have been added and clearing all your tasks.
Although it runs on Command Line Interface (CLI) it also has exceptional handling functionality by which if a malicious user uses my program then the program won't completely crash instead it'll display a subtle error message and prompt the user to input again.

# How the app was made:
For functionalities like adding tasks, removing tasks, listing tasks and clearing all tasks I made separate functions for each of those.<br/><br/>
### **In `add_tasks()` function:**
```
def add_tasks(str):
    with open("new_file_tasks.txt", "a") as file:
        file.write(f"{str}\n")
```
* The `add_tasks()` function contains function parameters `"str"`
* I used the `open()` function to open `"new_file_tasks.txt"` in append mode using `"a"` after the file name.
* Using the `write()` function which appends a string to the file with `"str"` and then linebreak by using `"\n"`.

### **In `remove_tasks()` function:**
```
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
```
* The `remove_tasks()` takes `int` as a function argument which stores the task's index that has to be deleted.
* What I came to when deleting the task is that first I'll declare an empty list `tasks_list = []` and using `open()` I'll open `"new_file_tasks.txt"` in read mode using `"r"`.
* And then using the `for` loop to iterate each line and append them to the `tasks_list = []` and clear the trailing whitespaces using the `tasks_list.append(line.rstrip())` function.
* Now that I've appended all the tasks in the list in the form of a string in the `try` block using `tasks_list.pop(int - 1)` this will pop out the task's index which was entered by the user.
* And now `with open("new_file_tasks.txt")` will open the .txt file in write mode using `"w"` and using `for` loop iterate each task in the `tasks_list = []` and write them into `"new_file_tasks.txt"` and after each task being added linebreak `"\n"`.
* In the `except` block I've handled `IndexError` which can happen if the user knowingly/unknowingly tries to enter an index that is greater than the total number of tasks.

### **In `list_tasks()` function:**
```
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
```
* Opening all the tasks using `open("new_file_tasks.txt", "r")` function in read mode using `"r"`.
* Now, read all the tasks into a list `all_tasks` by assigning it with `file.readlines()`.
* Then, using conditionals, check if there are no tasks by using `len(all_tasks) == 0` and then print "---No tasks entered!---".
* Else, using `for` loop in `range(0, len(all_tasks))` prints all the tasks by striping the whitespaces using the `strip()` function and listing them in numbered order.

### **In `clear_all_tasks()` function:**
```
def clear_all_tasks():
    with open("new_file_tasks.txt", "w") as file:
        file.close()
```
* Opening file with `open()` function and in write mode `"w"` and if we close the file without entering anything then it'll clear the file contents.
* Mind you, that while using `"w"` opens the file in *writing mode* and anything you save will erase the previous content and then rewrite it while `"a"` will open the file *append* mode this will append all the changes you make without making any changes to the previous content in the file.

Now at last,
### **In `main()` body:**
```
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
```
* I'm using a `while` loop to keep the user prompted to choose from the options to add, remove, list and clear tasks.
* In the `try` block using the `choose_command` variable I'm taking integer input from the user for choosing between:
  1. Add task.
  2. Remove a task.
  3. List all tasks.
  4. Clear all tasks.
* If the user maliciously enters a value other than integer the program won't crash but again prompt the user with the message "Only integer values are acceptable!" and if they enter a value other than 1, 2, 3 and 4 then the program will again prompt the user "Enter values from 1, 2, 3 and 4!".
* If the user enters "1" as input then the` case 1` block will be executed and it asks the user to enter the task, he/she wants to be stored. And then pass it as a function argument in the `add_tasks()` function.
* In `case 2` first I've declared a variable `remove_task number` which takes an integer input of the task's index you want to delete and then this variable is taken as a function argument by `remove_tasks()`.
* In `case 3` I've made a `list_tasks()` function call.
* In `case 4` I've made a `clear_all_tasks()` function call.

# Here's the output of the program:
https://github.com/GaneshSharma27/Todo-list/assets/90471588/752437be-71f9-4b2b-9424-c9c4b19cb5e4
