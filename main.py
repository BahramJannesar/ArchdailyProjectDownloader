
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import os
import requests
import time
import re
from bs4 import BeautifulSoup
import json

chromedriver = "/driver/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)

base_url = 'https://www.archdaily.com/'


project_link = base_url + input('Project Code : ')

def project_scraper(driver , project_link):
            response = requests.get(project_link)
            soup = BeautifulSoup(response.content , 'html.parser')
            paragraph = soup.find_all('p')
            list_of_paragraph = []
            for each_paragpraph in paragraph:
                list_of_paragraph.append(each_paragpraph.text.strip())
            driver.get(project_link)

            timeout = 20
            try:
                WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js-char-list", " " ))]')))
            except TimeoutException:
                print('Timed out waiting for page to load')
                driver.quit()
            try:    
                area =  driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__item", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]')[0].text.split(':')[1].strip()
                year =  driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__item", " " )) and (((count(preceding-sibling::*) + 1) = 3) and parent::*)]')[0].text.split(':')[1].strip()
                photographs = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__item", " " )) and (((count(preceding-sibling::*) + 1) = 4) and parent::*)]')[0].text.split(':')[1].strip()
            except:
                area = ''
                year = ''
                photographs = ''   
            project_dict =  {
                    'Project ID': project_link[26:32],
                    'Project Titel' :driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-title-big--bmargin-big", " " ))]')[0].text.split('/')[0].strip(),
                    'Project Type': driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__header-category", " " ))]//a')[0].text.strip(),
                    'City': driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__header-location", " " ))]')[0].text.split(',')[0].strip(),
                    'Country': driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__header-location", " " ))]//a')[0].text.strip(),
                    'Architects': driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "afd-specs__item", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]')[0].text.split(':')[1].strip(),
                    'Area': area,
                    'Year': year,
                    'Photographs': photographs,
                    'Project URL': project_link.strip(),
                    'Text Content': list_of_paragraph[7:-2]
                    
            } 
            project_js = json.dumps(project_dict, indent=4 , ensure_ascii=False).encode('utf8')
            with open('projct_details.json', 'w' , encoding='utf-8') as file:
                file.write(project_js.decode() + ',')
            print('Project details are ready.')

def project_image_downloader(driver ,project_link):
    response = requests.get(project_link)
    soup = BeautifulSoup(response.content , 'html.parser')
    a_tag = soup.find('a' , attrs={'class':'gallery-link afd-desktop-e'})
    link = base_url + a_tag.get('href')
    driver.get(link)

    timeout = 20
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "js-gal-mob-img-onview", " " ))]')))
    except TimeoutException:
        print('Timed out waiting for page to load')
        driver.quit()

    this_table = driver.find_elements_by_id('gallery-items')
    for this in this_table:
        temp = this.get_attribute('data-images')

    large_urls = []

    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', temp)
    for url in urls:
        if 'large_jpg' in str(url):
            large_urls.append(url)
    i = 1
    for each in large_urls:
        with open('{}.jpg'.format(i), 'wb') as handle:
                response = requests.get(each, stream=True)
                print('Picture number {} downloaded'.format(i))
                time.sleep(2)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)
        i += 1


if __name__ == "__main__":
    project_scraper(driver , project_link)
    project_image_downloader(driver ,project_link)
