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



firefoxOptions = FirefoxOptions(); 
firefoxOptions.set_preference("dom.webnotifications.enabled",False); 
driver = webdriver.Firefox(firefoxOptions)


driver.get('https://www.ecva.net/papers.php')

sleep(3)

# yearly_paper_section = driver.find_elements(By.XPATH,'//button[contains(text(),"ECCV")]')
all_link = []
# for paper_section in yearly_paper_section:
#     print(paper_section.get_attribute('innerHTML').strip())
#     temp = []
#     paper_section.click()
sleep(2)
list_link_paper = driver.find_elements(By.XPATH,"//div[@id='content']//dt[@class = 'ptitle']/a")
print(len(list_link_paper))
for paper in list_link_paper:
    all_link.append(paper.get_attribute('href'))
        # print(paper.get_attribute('href'))
    # all_link[f'{paper_section.get_attribute('innerHTML').strip()}'] = temp
    # sleep(2)
#     paper_section.click()
#     sleep(2)
print(f'All links crawled.')

with open("all_link.pkl","wb") as f:
    pickle.dump(all_link, f)
