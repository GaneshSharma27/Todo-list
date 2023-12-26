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
* And then using the `for` loop to iterate each line and append them to the `tasks_list = []` and clear the trailing whitespaces using the `rstrip()` function.
