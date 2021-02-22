"""
Script to download latest GeForce driver 
"""
# Import Splinter and Chromedriver
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
 

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# =============================================================================
url = 'https://www.nvidia.com/Download/driverResults.aspx/170312/en-us'
browser.visit(url)

bios_box     = browser.find_by_tag('a[id=lnkDwnldBtn]')
print(bios_box['href'])
bios_box.click()
time.sleep(20)