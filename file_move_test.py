# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:48:32 2020

Script to automatically install system drivers from dedicated
server folder

@author: Eric
"""
import os
import shutil

find_folder1 = r"C:\Users\Eric\Desktop\Test_folder1\Test_text.txt"
find_folder2 = r"C:\Users\Eric\Desktop\Test_folder2\Test_text.txt"

os.rename(find_folder2, find_folder1)
