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

class LinkError(Exception):
    pass

# firefoxOptions = FirefoxOptions(); 
# firefoxOptions.set_preference("dom.webnotifications.enabled",False); 
# driver = webdriver.Firefox(firefoxOptions)

# with open('all_link.pkl', 'rb') as f:
#     link_lst = pickle.load(f)

# link = 'https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/4_ECCV_2024_paper.php'

def paper_page_crawler(driver,link):

    driver.get(link)

    paper_info = {}
    
    ##
    title = driver.find_elements(By.XPATH,'//div[@id = "papertitle"]')

    if len(title) != 1:
        raise LinkError('There are more (less) than one title in this paper page, check again.')
    else:
        paper_title = title[0].get_attribute('innerHTML').strip()
    paper_info['Title'] = paper_title

    ##
    authors = driver.find_elements(By.XPATH,'//div[@id = "authors"]//i')

    if len(authors) != 1:
        raise LinkError('There are more(less) than one authors section in this paper page, check again.')
    else:
        authors_name = authors[0].get_attribute('innerHTML').strip()

    paper_info['Authors'] = authors_name

    ###
    abstract = driver.find_elements(By.XPATH,"//div[@id = 'abstract']")

    if len(abstract) != 1:
        raise LinkError('There are more(less) than on abstract section in this paper page, check again.')
    else:
        abstract_content = abstract[0].get_attribute('innerHTML').strip()

    paper_info['Abstract'] = abstract_content

    ##
    pdf_url = None
    try:
        pdf_urls = driver.find_elements(By.XPATH,"//a[text() = 'pdf']")
        if len(pdf_urls) > 1:
            raise LinkError('There are more than one pdf_url in this paper page, check again.')
        else:
            pdf_url = pdf_urls[0].get_attribute('href')
            # print(pdf_url)
            # re.sub(r'^.*?I', 'I', pdf_url)
    except (NoSuchElementException,IndexError) as e:
        print(f'No pdf available for {link}')

    paper_info['pdf_url'] = pdf_url

    ##
    supp_material_url = None
    try:
        supp_material_urls = driver.find_elements(By.XPATH,"//a[contains(text(),'supplementary material')]")
        if len(supp_material_urls) > 1:
            raise LinkError('There are more than one url for supplementary material in this paper page, check again.')
        else:
            supp_material_url = supp_material_urls[0].get_attribute('href')
            # print(supp_material_url)
            # re.sub(r'^.*?I', 'I', pdf_url)
    except (NoSuchElementException,IndexError) as e:
        print(f'No supplementary material available for {link}')

    paper_info['Suppementary Material'] = supp_material_url

    ##
    DOI_url = None
    try:
        DOI_urls = driver.find_elements(By.XPATH,"//a[contains(text(),'DOI')]")
        if len(DOI_urls) > 1:
            raise LinkError('There are more than one DOI in this paper page, check again.')
        else:
            DOI_url = DOI_urls[0].get_attribute('href')
            # print(DOI_url)
            # re.sub(r'^.*?I', 'I', pdf_url)
    except (NoSuchElementException,IndexError) as e:
        print(f'No DOI for {link}')
    paper_info['DOI'] = DOI_url
    
    years = [2024,2022,2020,2018]

    for year in years:
        if f'eccv_{year}' in link:
            paper_info['Year'] = year
        else:
            continue


    return paper_info
