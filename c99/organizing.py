import os 
import shutil

path=input('Enter the name of the directory you would like to organize: ')

NumOFolders=os.listdir(path)

for num in NumOFolders:
    name,extention=os.path.splitext(num)
    extention=extention[1:]
    if extention=='':
        continue
    if os.path.exists(path+'/'+extention):
        shutil.move(path+'/'+num,path+'/'+extention+'/'+num)
    else:
        os.mkdir(path+'/'+extention)
        shutil.move(path+'/'+num,path+'/'+extention+'/'+num)
