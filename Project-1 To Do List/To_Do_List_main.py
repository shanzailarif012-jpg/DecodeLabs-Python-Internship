# Project 1: To-Do List | DecodeLabs Python Internship 2026
# Name: Muhammad Shanzail (Dev_Shanzail)
# Purpose: A simple console-based to-do list app that lets users add and view tasks using Python lists.


my_tasks = []

while True:
    print("1:Add Tasks\n2:View Tasks\n3:Exit")

    choice=int(input("Enter Your Choice: "))

    if choice == 1:
        print("Add Task")
        task=input("Enter Task: ")
        my_tasks.append(task)

    elif choice == 2:
        print("View Tasks")
        if my_tasks == []:
            print("No Task Yet!")
        else:
            for index,i in enumerate(my_tasks, start=1):
                print(index,i)
                

    elif choice ==3:
        print("Exit")
        break
    else:
        print("Invalid Choice")   


