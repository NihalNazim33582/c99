import os
import shutil

soucre=input('Enter the soucre folder name: ')
destination=input('Enter the destination name: ')

soucre=soucre+'/'
destination=destination+'/'

fileName=os.listdir(soucre)

for file in fileName:
    shutil.copy((soucre+file),destination)