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
with os.scandir(r"C:\Users\Eric\Downloads") as dir_contents:
    for entry in dir_contents:
        print(type(entry.name))
# ref_time = time.time()
# oreo = list(os.scandir(r"C:\Users\Eric\Downloads")) 
# print(oreo[0])
# print((ref_time))
# cream = time.ctime(oreo[0].stat().st_mtime)
# for maple in oreo:
#     cream = (maple.stat().st_mtime)
#     if cream >= ref_time:
#         print("hit")
#     else:
#         print("miss")
#     print(type(cream))


# find_folder1 = r"C:\Users\Eric\Downloads\471.41-desktop-win10-64bit-international-dch-whql (1).exe"
# find_folder2 = r"C:\Users\Eric\Desktop\Test_folder2\471.41-desktop-win10-64bit-international-dch-whql (1).exe"
# os.rename(find_folder1, find_folder2)

# head = "hEad"
# string = r"Buffalo {}".format(head)
# print(string)