from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from book_scrapper import Book_Scrapper
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import json
from csv import reader
import requests

class Website_Scrapper:
    
    # Constructor function which installs web driver for Chrome.
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.headless = True
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # self.driver = webdriver.Chrome("chromedriver.exe")
        # self.driver = webdriver.Chrome("chromedriver.exe", options=options)
        # self.driver = webdriver.Edge('msedgedriver.exe')
        book_array = []
        start = time.time()

        with open("test.csv", "r") as read_obj:
            csv_reader = reader(read_obj)

            for row in csv_reader:
                self.driver.get("https://gmu.bncollege.com/course-material/course-finder")
                args = row[0].split(" ")
                # if (args[1] == "303"):
                #     break
                
                # ACCT 203 3D1 (Hangs)
                # args[0] = Department | args[1] = Course Number | args[2] = Section
                self.fill_textbook_info('spring', args[0], args[1], args[2])
                
                book = Book_Scrapper(book_array, self.driver, args[0], args[1], args[2])
                book_info = book.get_book_info()
                
                # requests.post("http://localhost:8000/book/insert", data=json.dumps(book_array[0], indent=4))
            read_obj.close()


        # read_obj.close()
        print(book_array)

        with open('book_data.json', 'w') as outfile:
            json.dump(book_array, outfile, indent=4, sort_keys=True)

        end = time.time()
        print(end - start)

    # Function that gets chooses a campus to find if a book is available from the GMU bookstore.
    # Returns 1 if a book is not found on a campus. Returns 0 if found successfully.
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

    # Selects a term from a user's command. Returns 1 if not successfully found.
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

    # Function that accepts a user's command for a specific department.
    # Scrapper will search for the department and return 0 if properly executed, otherwise return 1.
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

    # Scrapper looks for a selected course from a command.
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

    # Function that displays textbook information for a course inside the bot.
    # Used while loops because selenium isn't consistent with getting elements on a page
    def fill_textbook_info(self, term, department, course, section):
        
        # Each while loop gets information of the book individually.
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

 
