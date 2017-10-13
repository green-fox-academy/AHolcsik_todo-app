import sys

def app_arg():
    return len(sys.argv)


def todo_print():
    if app_arg() == 1:
        print('Command Line Todo application \n ============================= \n Command line arguments: \n -l   Lists all the tasks \n -a   Adds a new task \n -r   Removes an task \n -c   Completes an task')
    else:
        return sys.argv[1]


def todo_controller():
    if app_arg() == 1:
        todo_print()
    if sys.argv[1] == '-l':
        list_todo()
    elif sys.argv[1] == '-a':
        add_todo()
    elif sys.argv[1] == '-r':
        remove_todo()
    elif sys.argv[1] == '-c':
        check_todo()
    else:
        print('Unsuported argument')

file_name = 'todo.txt'

# def chek_if():
#     try:
#         f = open(file_name, 'r')
#         for line in f.readlines:
            
    

def list_todo():
    try:
        f = open(file_name, 'r')
        first_char = f.read(1)
        if not first_char:
            print('No todos for today! :)')
        else:
            for index, line in enumerate(f.readlines()):
                print(index + 1, '-', line)
            f.close()
    except IOError:
        print('Unable to read file: ', file_name)


def add_todo():
    try:
        f = open(file_name, 'a')
        f.write(sys.argv[2] + '\n')
    except IOError:
        print('Unable to read file: ', file_name)    


def remove_todo():
    try:
        f = open(file_name, 'r')
        listed = list(f)
        del listed[int(sys.argv[2])]
        f = open(file_name, 'w')
        for line in listed:
            f.write(line)
        f.close()
    except IOError:
        print('Unable to read file: ', file_name)    




# def check_todo():
#     try:
#         f = open(file_name, 'r')
#         for line in f.readlines:
#             pass






todo_controller()

