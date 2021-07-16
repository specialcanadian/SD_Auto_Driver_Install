# Import Splinter and Chromedriver
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import shutil
# =============================================================================
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
url = 'https://www.asrock.com/MB/Intel/Z490%20Phantom%20Gaming-ITXTB3/index.asp#BIOS'
# =============================================================================
# Reference time, script will move files modified/downloaded after this time
ref_time = time.time() 

browser.visit(url)
bios_box     = browser.find_by_tag('tbody')
bios_box.find_by_tag("a")[1].click()
# Wait for 20 seconds so download completes before window closes
time.sleep(10)

# Move files =========================================================================
pack = list(os.scandir(r"C:\Users\Eric\Downloads")) 
for oreo in pack:
    cream     = (oreo.stat().st_mtime)
    file_name = oreo.name 
    if cream >= ref_time:
        print("hit")
        try:
            find_folder1 = oreo.path
            find_folder2 = r"C:\Users\Eric\Desktop\Test_folder2\{}".format(file_name)
            os.rename(find_folder1, find_folder2)
        except FileExistsError:
            print("{} is latest version".format(file_name))
            os.remove(oreo.path)

