# import os
# import shutil

# folderName=input('What is the name of the folder?: ')
# where=input('Where is this folder going: ')

# folderName=folderName+'/'
# where=where+'/'

# Listing=os.listdir(folderName)

# for folder in folderName:
#     shutil.move((folderName+folder),where)

import os
import shutil

soucre=input('Enter the soucre folder name: ')
destination=input('Enter the destination name: ')

soucre=soucre+'/'
destination=destination+'/'

fileName=os.listdir(soucre)

for file in fileName:
    shutil.move((soucre+file),destination)