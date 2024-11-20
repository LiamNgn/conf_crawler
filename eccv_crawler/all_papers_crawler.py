from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions,FirefoxService
import os
from selenium.webdriver.common.alert import Alert
from time import sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, MoveTargetOutOfBoundsException
from eccv_crawler.util import scroll_until_end
from selenium.webdriver.firefox.options import Options
import pickle
from io import StringIO
import lxml.etree
from selenium.webdriver.common.action_chains import ActionChains
from eccv_crawler.paper_crawler import *


firefoxOptions = FirefoxOptions(); 
firefoxOptions.set_preference("dom.webnotifications.enabled",False); 
driver = webdriver.Firefox(firefoxOptions)

with open('all_link.pkl', 'rb') as f:
    link_lst = pickle.load(f)

crawled_results = []

# keylist = [key for key in link_lst.keys()]

crawled_link = []

for link in link_lst:
    if link in crawled_link:
        print('Link crawled.')
        continue
    else:
        paper_content = paper_page_crawler(driver,link)
        crawled_results.append(paper_content)
        crawled_link.append(link)

# for year in keylist:
#     print(year)
#     crawled_results = []
#     for page_link in link_lst[year]:
#         if page_link in crawled_link:
#             print('Link crawled.')
#             continue
#         else:
#             paper_content = paper_page_crawler(driver,page_link)
#             crawled_results.append(paper_content)
#             crawled_link.append(page_link)
#     print(crawled_results)
#     result_dict[year] = crawled_results
#     print(f'{year} crawled successfully.')


with open('all_papers_ECVA_info.pkl', 'wb') as f:
    pickle.dump(crawled_results,f)
