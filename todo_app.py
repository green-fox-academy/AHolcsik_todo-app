import sys

def app_arg():
    return len(sys.argv)

def todo_controller():
    if app_arg() == 1:
        print('Command Line Todo application \n ============================= \n Command line arguments: \n -l   Lists all the tasks \n -a   Adds a new task \n -r   Removes an task \n -c   Completes an task')

todo_controller()

