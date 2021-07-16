# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
# Sets up Chromedriver and browser window
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.asrock.com/mb/Intel/Z490%20Phantom%20Gaming-ITXTB3/index.asp#Download'
browser.visit(url)
# ============= IMPORTANT how to find tags based on attributes===================================================================
table_list = browser.find_by_tag('input[value="BIOS"]')
print(table_list['value'])
# ===========================================================================================

#============ Parses dir and closes once done, saving mem ===============================================
with os.scandir(r"C:\Users\Eric\Downloads") as dir_contents:
    for entry in dir_contents:
        info = entry.stat()
        print(info.st_mtime)
#============ Parses dir and closes once done, saving mem ===============================================
