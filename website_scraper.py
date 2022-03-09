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


def get_textbook_info():
    print("hi")

# WebDriverWait waits for the element to load before it's clicked o
def fill_textbook_info(term, department, course, section):
    try:
        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[1]/span'))
        )
        element.click()
        print('found campus button')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[1]/span[2]/span/span[2]/ul/li[3]'))
        )
        element.click()
        print('selected fairfax campus')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div'))
        )
        element.click()
        print('selected term drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div/span[2]/span/span[2]/ul/li[2]'))
        )
        element.click()
        print('selected spring 2022')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div'))
        )
        element.click()
        print('selected department drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div/span[2]/span/span[1]/input'))
        )
        element.send_keys(department)
        print('typed department cs')

        element.send_keys(Keys.ENTER)
        print('selected department cs')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div'))
        )
        element.click();
        print('clicked on course drop down')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div/span[2]/span/span[1]/input'))
        )
        element.send_keys(course)
        print('typed course 321')

        element.send_keys(Keys.ENTER)
        print('selected course 321')

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
        print('typed section 002')

        element.send_keys(Keys.ENTER)
        print('selected section 002')

        element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH,
                                            '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[3]/div[2]/a'))
        )
        element.click()
        print('clicked on retrieve materials')

    except:
        print("failed to fill in textbook info")
        return 1

    return 0

def main():
    driver.get("https://gmu.bncollege.com/course-material/course-finder")

    while(fill_textbook_info('summer', 'cs', 321, '') == 1):
        print('loop')

    # curUrl = driver.current_url
    # print(curUrl)

    time.sleep(1000)

if __name__ == "__main__":
    main()