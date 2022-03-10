from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome("chromedriver.exe")
# driver = webdriver.Chrome("chromedriver.exe", options=options)

# TODO implement feature to select campus
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

# TODO implement feature to select term
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
        element.send_keys(department)
        # print('typed department cs')

        element.send_keys(Keys.ENTER)
        # print('selected department cs')

    except:
        return 1

    return 0

def select_course(course):
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
        element.send_keys(course)
        # print('typed course 321')

        element.send_keys(Keys.ENTER)
        print('selected course 321')

    except:
        return 1

    return 0

def select_section(section):
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[4]/div/div'))
        )
        element.click()
        print('clicked on section drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[4]/div/div/span[2]/span/span[1]/input'))
        )
        element.send_keys(section)
        # print('typed section 002')

        element.send_keys(Keys.ENTER)
        # print('selected section 002')

    except:
        return 1

    return 0

def retrieve_material():
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[3]/div[2]/a'))
        )
        element.click()
        # print('clicked on retrieve materials')

    except:
        return 1

    return 0

# I use while loops because selenium isn't consistent with getting elements on a page
def fill_textbook_info(term, department, course, section):
    while(select_campus_info()):
        print('selecting campus')

    while(select_term(term)):
        print('selecting term')

    while(select_department(department)):
        print('selecting department')

    while(select_course(course)):
        print('selecting course')

    while(select_section(section)):
        print('selecting section')

    while(retrieve_material()):
        print('retrieving material')

def main():
    start = time.time()
    driver.get("https://gmu.bncollege.com/course-material/course-finder")

    fill_textbook_info('summer', 'cs', 310, '002')

    # curUrl = driver.current_url
    # print(curUrl)

    # time.sleep(1000)
    end = time.time()
    print(end - start)

    driver.close()

if __name__ == "__main__":
    main()
