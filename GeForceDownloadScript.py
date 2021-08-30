# Import Dependicies
from selenium.webdriver import Edge
from selenium.webdriver.support.ui import Select
import time

import os
import shutil
# Open Edge instance for navigation
ref_time = time.time()

# driver = Edge(executable_path=r"C:\Users\Eric\Desktop\Coding Stuff\SD_Code\SD_Auto_Driver_Install\edgedriver_win64\msedgedriver.exe")
driver = Edge(executable_path=r"edgedriver_win64\msedgedriver.exe")
# Navigate to specified website
driver.get("https://www.nvidia.com/Download/index.aspx?lang=en-in")
time.sleep(5)

#This block of code sets all the dropdown menus to the correct selections
#==============================================================================================

# Store product type drop down menu as object and Select GeForce from dropdown menu
product_type_selector = Select(driver.find_element_by_id('selProductSeriesType'))
product_type_selector.select_by_value('1')


product_series_selector = Select(driver.find_element_by_id('selProductSeries'))
product_series_selector.select_by_visible_text('GeForce RTX 30 Series')


download_type_selector = Select(driver.find_element_by_id('ddlDownloadTypeCrdGrd'))
download_type_selector.select_by_visible_text('Game Ready Driver (GRD)')


download_language_selector = Select(driver.find_element_by_id('ddlLanguage'))
download_language_selector.select_by_value('1')

# Clicks button to search for driver
search_button = driver.find_element_by_xpath("//a[@href='javascript: GetDriver();']")
search_button.click()
time.sleep(5)

# CLicks button to search for 
download_link = driver.find_element_by_id('lnkDwnldBtn')
download_link.click()
time.sleep(5)

download_button = driver.find_element_by_xpath("//a[starts-with(@href, '//us.download.nvidia.com/Windows')]")
download_button.click()
time.sleep(80)

all_files = list(os.scandir(r"C:\Users\Eric\Downloads")) 
for entry in all_files:
    mod_time = (entry.stat().st_mtime)
    if mod_time >= ref_time:
        driver_name       = entry.name
        driver_file_path  = entry.path
        current_path      = driver_file_path
        format_test       = "1234"
        server_path       = r"C:\Users\Eric\Desktop\Test_folder2\{}.exe".format(driver_name)
        os.rename(driver_file_path, server_path)
        

    