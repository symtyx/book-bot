import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pprint import pprint
import sys
import time
import os

# path = '/usr/local/bin/chromedriver'
# sys.path.append(path)
URL = "https://gmu.bncollege.com/course-material/course-finder"
# page = requests.get(URL)

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("--no-sandbox")
# options.add_argument("--disable-extensions")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()
departments = []
courses = []

def select_campus_info():
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[1]/span'))
        )
        element.click()
        # print('found campus button')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[1]/span[2]/span/span[2]/ul/li[3]'))
        )
        element.click()
        # print('selected fairfax campus')

    except:
        return 1

    return 0

def select_term(term):
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div'))
        )
        element.click()
        # print('selected term drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div/span[2]/span/span[2]/ul/li[2]'))
        )
        element.click()
        # print('selected spring 2022')

    except:
        return 1

    return 0

def select_department(department):
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div'))
        )
        element.click()
        # print('selected department drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div/span[2]/span/span[1]/input'))
        )
        selector = Select(driver.find_element(by=By.XPATH, value="/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div/select"))
        options = selector.options
        # print(options)
        # departments = []
        for index in range(0, len(options)):
            if (options[index].text == "Select"):
                continue
            dep_dict = {"department": options[index].text}
            departments.append(dep_dict)
        element.send_keys(department)
        # print('typed department cs')

        element.send_keys(Keys.ENTER)
        # print('selected department cs')

    except:
        return 1

    return 0

def select_course(course, department):
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div'))
        )
        element.click()
        # print('clicked on course drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div/span[2]/span/span[1]/input'))
        )
        # element.send_keys(course)
        # print('typed course 321')
        # FIXME: We need a way to get the course number list on the selected department...
        selector = Select(driver.find_element(by=By.XPATH, value="/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div/select"))
        options = selector.options
        index = 0
        courses = []
        for dep in departments:
            print(dep['department'])
            if dep['department'] == department:
                 break
            index += 1

        for ind in range(0, len(options)):
            if (options[ind].text == "Select"):
                continue
            courses.append(options[ind].text)

        departments[index]['courses'] = courses
        # element.send_keys(Keys.ENTER)
        # print('selected course 321')

    except:
        return 1

    return 0

def fill_textbook_info(term, department, course, section):
    while(select_campus_info()):
        print('selecting campus')

    while(select_term(term)):
        print('selecting term')

    while(select_department(department)):
        print('selecting department')

    while(select_course(course, department)):
        print('selecting course')

    # while(select_section(section)):
    #     print('selecting section')

    # while(retrieve_material()):
    #     print('retrieving material')

def main():
    start = time.time()
    driver.get("https://gmu.bncollege.com/course-material/course-finder")

    fill_textbook_info('summer', 'CS', 310, '002')
    print(departments)

    # curUrl = driver.current_url
    # print(curUrl)

    time.sleep(15)
    end = time.time()
    print(end - start)

    driver.close()

if __name__ == "__main__":
    main()