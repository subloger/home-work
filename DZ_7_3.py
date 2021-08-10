import os
import shutil


dst_1 = 'templates'                                         # Имя директории назначения
dst_2 = 'templates_1'                                       # Промежуточная директория
for folder in os.walk('my_project'):
    if folder[1] == ['templates']:
        if not os.path.exists(dst_1):
            path = os.path.join(folder[0], folder[1][0])
            shutil.copytree(path, dst_1)
        else:
            path = os.path.join(folder[0], folder[1][0])
            fol = os.listdir(path)
            fol = os.path.join(dst_2, fol[0])
            shutil.copytree(path, dst_2)
            shutil.move(fol, dst_1)
            os.rmdir(dst_2)
