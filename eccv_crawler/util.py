from time import sleep
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException, MoveTargetOutOfBoundsException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import pickle
import os
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
import hashlib
import uuid
import logging
import eccv_crawler.my_logger as my_logger

root_logger = logging.getLogger()
file_handler = logging.FileHandler('util_log.log',mode = 'w')
root_logger.setLevel(logging.INFO)
root_logger.addHandler(file_handler)

my_logger.my_function()



#Util function
def make_ordinal(n):
    '''
    Convert an integer into its ordinal representation::

        make_ordinal(0)   => '0th'
        make_ordinal(3)   => '3rd'
        make_ordinal(122) => '122nd'
        make_ordinal(213) => '213th'
    '''
    n = int(n)
    if 11 <= (n % 100) <= 13:
        suffix = 'th'
    else:
        suffix = ['th', 'st', 'nd', 'rd', 'th'][min(n % 10, 4)]
    return str(n) + suffix

##Page manipulation function
def scroll_until_end(driver,pause_time = 4):
    #This function scroll infinitely until the web is no longer scrollable
    SCROLL_PAUSE_TIME = pause_time


    print('Start scrolling.')
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    print(last_height)
    while True:
        # Scroll down to bottom


        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

        