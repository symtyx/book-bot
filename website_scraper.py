from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from book_scrapper import Book_Scrapper
from webdriver_manager.chrome import ChromeDriverManager
import json

class Website_Scrapper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.headless = True
        # self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # self.driver = webdriver.Chrome("chromedriver.exe")
        # self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        self.driver = webdriver.Edge('msedgedriver.exe')
        book_array = []
        file = open('catalog_data.json')
        data = json.load(file)

        while (1):

            
            start = time.time()
            for i in data:
                # i['name'] for department name
                # print(i['name'])
                for j in i['courses']:
                    # j['name'] to get each course number
                    # print("\n=&= Course Number =&=")
                    # print(j['name'])
                    # print("=&= Section Numbers =&=")
                    for z in j['sections']:
                        if (z['name'] == "3D1"):
                            break
                        self.driver.get("https://gmu.bncollege.com/course-material/course-finder")
                        # z['name'] to get each section number of course
                        # print(z['name'])
                        self.fill_textbook_info('spring', i['name'], j['name'], z['name'])
                        # self.fill_textbook_info('spring', 'cs', 367, '001')
                        book = Book_Scrapper(book_array, self.driver, i['name'], j['name'], z['name'])
                        # book = Book_Scrapper(book_array, self.driver, 'cs', 367, '001')
                        book_info = book.get_book_info()
                    break  
                break

            # self.driver.get("https://gmu.bncollege.com/course-material/course-finder")
            # self.fill_textbook_info('spring', 'acct', '203', '3D1')
            # book = Book_Scrapper(book_array, self.driver, 'acct', '203', '3D1')
            # book_info = book.get_book_info()
            with open('book_data.json', 'w') as outfile:
                json.dump(book_array, outfile, indent=4, sort_keys=True)
            # time.sleep(1000)
            file.close()
            end = time.time()
            print(end - start)

    # TODO implement feature to select campus
    def select_campus_info(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[1]/span'))
            )
            element.click()
            # print('found campus button')

            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[1]/span[2]/span/span[2]/ul/li[3]'))
            )
            element.click()
            # print('selected fairfax campus')

        except:
            return 1

        return 0

    # TODO implement feature to select term
    def select_term(self, term):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div'))
            )
            element.click()
            # print('selected term drop down')

            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[1]/div/div/span[2]/span/span[2]/ul/li[2]'))
            )
            element.click()
            # print('selected spring 2022')

        except:
            return 1

        return 0

    def select_department(self, department):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div'))
            )
            element.click()
            # print('selected department drop down')

            element = WebDriverWait(self.driver, 1).until(
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

    def select_course(self, course):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div'))
            )
            element.click()
            # print('clicked on course drop down')

            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[3]/div/div/span[2]/span/span[1]/input'))
            )
            element.send_keys(course)
            # print('typed course 321')

            element.send_keys(Keys.ENTER)
            # print('selected course 321')

        except:
            return 1

        return 0

    def select_section(self, section):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[2]/div[2]/div[4]/div/div'))
            )
            element.click()
            # print('clicked on section drop down')

            element = WebDriverWait(self.driver, 1).until(
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

    def retrieve_material(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div/div/div/div[4]/div[2]/form/div/div[3]/div[2]/a'))
            )
            element.click()
            # print('clicked on retrieve materials')

        except:
            return 1

        return 0

    # I use while loops because selenium isn't consistent with getting elements on a page
    def fill_textbook_info(self, term, department, course, section):
        return_value = 1
        while(return_value):
            return_value = self.select_campus_info()
            # print('select_campus_info')

        return_value = 1
        while(return_value):
            return_value = self.select_term(term)
            # print('select_term')

        return_value = 1
        while(return_value):
            return_value = self.select_department(department)
            # print('select_department')

        return_value = 1
        while(return_value):
            return_value = self.select_course(course)
            # print('select_course')

        return_value = 1
        while(return_value):
            return_value = self.select_section(section)
            # print('select_section')

        return_value = 1
        while(return_value):
            return_value = self.retrieve_material()
            # print('retrieve_material')

    # def main():
    #     while(1):
    #         start = time.time()
    #         driver.get("https://gmu.bncollege.com/course-material/course-finder")
    #
    #         book_array = []
    #         fill_textbook_info('summer', 'cs', 367, '001')
    #         book = Book_Scrapper(book_array, driver, 'cs', '367')
    #         book_info = book.get_book_info()
    #
    #         # curUrl = driver.current_url
    #         # print(curUrl)
    #
    #         # time.sleep(1000)
    #         end = time.time()
    #         print(end - start)
    #
    #         driver.close()
    #         driver = webdriver.Chrome("chromedriver.exe")


    # if __name__ == "__main__":
    #     main()