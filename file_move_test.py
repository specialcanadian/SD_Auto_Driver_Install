# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:48:32 2020

Script to automatically install system drivers from dedicated
server folder

@author: Eric
"""
import os
import shutil

find_folder1 = r"C:\Users\Eric\Desktop\Test_folder1"
find_folder2 = r"C:\Users\Eric\Desktop\Test_folder2"

desktop = os.path.join(os.environ["HOMEPATH"], "Desktop")

p = os.listdir(find_folder1)
q = os.listdir(find_folder2)

print(p, q)
# print(desktop)

shutil.copy(find_folder1, find_folder2)
