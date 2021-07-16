# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 18:48:32 2020

Script to automatically install system drivers from dedicated
server folder

@author: Eric
"""
import os
import shutil
import time
# ============================================================================
# with os.scandir(r"C:\Users\Eric\Downloads") as dir_contents:
#     for entry in dir_contents:
#         info = entry.stat()
#         print(info.st_mtime)
# ref_time = time.time()
# oreo = list(os.scandir(r"C:\Users\Eric\Downloads")) 
# print(type(ref_time))
# cream = time.ctime(oreo[0].stat().st_mtime)
# for maple in oreo:
#     cream = (maple.stat().st_mtime)
#     if cream >= ref_time:
#         print("hit")
#     else:
#         print("miss")
    # print(type(cream))
# print(oreo[0].name)
head = "hEad"
string = r"Buffalo {}".format(head)
print(string)
# find_folder1 = r"C:\Users\Eric\Downloads\MoveMe.txt"
# find_folder2 = r"C:\Users\Eric\Desktop\Test_folder2\MoveMe.txt"
# os.rename(find_folder1, find_folder2)
