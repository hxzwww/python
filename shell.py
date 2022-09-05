import os

os.system("clear")
current_dir = os.getcwd()

#print("Available commands:\n ls\n la\n pwd\n cd\n cp\n mv\n rm\n touch *\n\
# vim *\n python3 *.py\n g++ *.cpp\n clang++ *.cpp\n ./*\n exit shell\n")

def ls():
    for element in os.listdir(current_dir):
        if element[0] != '.':
            print(element, end='\t ')
    print()

def la():                                                                       
    for element in os.listdir(current_dir):                                     
        print(element, end='\t ')                                           
    print()

def cd_home_dir():                                                                                                      
    count = 0                                                                                                           
    global current_dir                                                                                                  
    for i in range(len(current_dir)):                                                                                   
        if current_dir[i] == '/':                                                                                       
            count += 1                                                                                                  
        if count == 3:                                                                                                  
            current_dir = current_dir[0:i]                                                                              
            return

def cd(to):
    global current_dir
    if to == '~':
        cd_home_dir()
        return
    if to == '..':
        current_dir = current_dir[0:current_dir.rfind('/')]
    elif to == '.':
        return
    else:
        exists = False
        for element in os.listdir(current_dir):
            if element == to:
                exists = True
        if exists:
            current_dir += '/' + to
        else:
            print('no such file or directory')

def make_single_command(cmd):
    cmd = cmd.split()
    new_cmd = ''
    for i in range(len(cmd) - 1):
        new_cmd += cmd[i] + ' '
    new_cmd += ' ' + current_dir + '/' + cmd[len(cmd) - 1]
    return new_cmd

def make_double_command(cmd):
    cmd = cmd.split()
    new_cmd = ''
    for i in range(len(cmd) - 2):
        new_cmd += cmd[i] + ' '
    new_cmd += ' ' + current_dir + '/' + cmd[len(cmd) - 2] + \
            ' ' + current_dir + '/' + cmd[len(cmd) - 1]
    return new_cmd


single_command_dict = ['rm', 'touch', 'vim', 'python3', 'g++', 'clang++',
        'mkdir', 'rmdir']
double_command_dict = ['cp', 'mv']

while True:
    print(current_dir + '$', end=' ')
    command = input()
    switch = command.split()[0]
    if command == 'exit shell':
        break
    elif command == 'ls':
        ls()
    elif command == 'la':
        la()
    elif command == 'pwd':
        print(current_dir)
    elif command == 'clear' or command == 'poweroff':
        os.system(command)
    elif command.split()[0] == 'cd':
        if len(command.split()) > 1:
            tmp = command.split()[1].split('/')
            for i in tmp:
                cd(i)
        else: 
            cd_home_dir()
    elif command.split()[0] in single_command_dict:
        os.system(make_single_command(command))
    elif command.split()[0] in double_command_dict:
        os.system(make_double_command(command))
    else:
        print("invalid command")

