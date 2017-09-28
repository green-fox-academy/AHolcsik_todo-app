import sys

def app_arg():
    return len(sys.argv)

def todo_print():
    if app_arg() == 1:
        print('Command Line Todo application \n ============================= \n Command line arguments: \n -l   Lists all the tasks \n -a   Adds a new task \n -r   Removes an task \n -c   Completes an task')
    else:
        return sys.argv[1]

def todo_controller():
    if sys.argv[1] == '-l':
        pass
    elif sys.argv[1] == '-a':
        pass
    elif sys.argv[1] == '-r':
        pass
    elif sys.argv[1] == '-c':
        pass
    else:
        print('Unsuported argument')



todo_controller()

