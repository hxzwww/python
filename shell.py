import os

current_dir = os.getcwd()

print("Available commands:\n ls\n la\n pwd\n cd\n cp\n mv\n rm\n touch *\n\
 vim *\n python3 *.py\n g++ *.cpp\n clang++ *.cpp\n ./*\n exit shell\n")

def ls():
    for element in os.listdir(current_dir):
        if element[0] != '.':
            print(element, end='\t ')
    print()

def la():                                                                       
    for element in os.listdir(current_dir):                                     
        print(element, end='\t ')                                           
    print()

def pwd():
    print('  ' + current_dir)

def cd(to):
    global current_dir
    if to == '..':
        current_dir = current_dir[0:current_dir.rfind('/')]
    else:
        current_dir += '/' + to

def execute(command):
    os.system(command)

while True:
    print(current_dir + '$', end=' ')
    command = input()
    if command == 'exit shell':
        break
    elif command == 'ls':
        ls()
    elif command == 'la':
        la()
    elif command == 'pwd':
        pwd()
    elif command[0:2] == 'cd':
        cd(command.split()[1])
    elif command[0:2] == 'cp':
        execute('cp ' + current_dir + '/' + command.split()[1] + \
                ' ' + current_dir + '/' + command.split()[2])
    elif command[0:2] == 'mv':
        execute('mv ' + current_dir + '/' + command.split()[1] + \
                ' ' + current_dir + '/' + command.split()[2])
    elif command[0:2] == 'rm':
        execute('rm ' + current_dir + '/' + command.split()[1])
    elif command.split()[0] == 'touch':
        execute('touch ' + current_dir + '/' + command.split()[1])
    elif command.split()[0] == 'vim':
        execute('vim ' + current_dir + '/' + command.split()[1])
    elif command.split()[0] == 'python3':
        execute('python3 ' + current_dir + '/' + command.split()[1])
    elif command.split()[0] == 'g++':
        execute('g++ ' + current_dir + '/' + command.split()[1])
    elif command.split()[0] == 'clang++':
        execute('clang++ ' + current_dir + '/' + command.split()[1])
    elif command[0:2] == './':
        execute('./ ' + current_dir + '/' + command.split()[1])
    else:
        print('Invalid command!')

