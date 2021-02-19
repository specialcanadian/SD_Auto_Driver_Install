# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 19:14:26 2021
Downloads drivers for ASRock Z490 Phantom Gaming-ITX/TB3
@author: Eric
"""
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import time
# Sets up Chromedriver and browser window
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

url = 'https://www.asrock.com/mb/Intel/Z490%20Phantom%20Gaming-ITXTB3/index.asp#Download'
browser.visit(url)

table_list = browser.find_by_tag('tr')
download_button = table_list[1].find_by_tag("a")
word_list = table_list[1].text
print(table_list[1].text)
#print(table_list[1].find_by_tag("a").text)
#download_button.click()
#time.sleep(20)

# ===============================================================
# Check for text
#================================================================
keyword = "Realtek"

# https://stackoverflow.com/questions/5319922/python-check-if-word-is-in-a-string
def contains_word(s, w):
    return f' {w} ' in f' {s} '

print(contains_word(table_list[1].text, keyword))