import os

if not os.path.exists('--my_project'):
    os.makedirs('--my_project\--settings')
    os.chdir('--my_project')
    os.mkdir('--mainapp')
    os.mkdir('--adminapp')
    os.mkdir('--authapp')
else:
    print('"Folder is exist"')
