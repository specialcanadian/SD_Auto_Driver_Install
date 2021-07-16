# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:14:26 2021
Downloads BIOS driver for ASRock Z490 Phantom Gaming-ITX/TB3
@author: Eric
"""
# Import Splinter and Chromedriver
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
 
# Wait for 5 seconds
time.sleep(5)

executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# =============================================================================
url = 'https://www.asrock.com/MB/Intel/Z490%20Phantom%20Gaming-ITXTB3/index.asp#BIOS'
browser.visit(url)
bios_box     = browser.find_by_tag('tbody')
bios_box.find_by_tag("a")[1].click()

# Wait for 20 seconds so download completes before window closes
time.sleep(20)