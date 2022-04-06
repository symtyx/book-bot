from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Book_Scrapper:
    def __init__(self, book_array, driver, department, course):
        self.driver = driver
        self.book_dict = {}
        self.department = department
        self.course = course
        self.book_array = book_array

    def compile_book(self):
        self.get_book_info()

    def get_book_info(self):
        return_value = 1
        book_text = []

        print('get book')
        while(return_value == 1):
            return_value = self.get_books()
        # time.sleep(2)
        # book1 = return_value[0].text
        # book2 = return_value[1].text

        books = return_value

        for book in books:
            while(book.text == ''):
                time.sleep(1)
            book_text.append(book.text)

        for index in range(len(books)):
            return_value = 1
            print('get book')
            while (return_value == 1):
                return_value = self.get_books()
            book = return_value[index]

            text = book_text[index]
            book_info = {}
            seller_info = {}
            return_value = 1

            print('book link')
            while (return_value == 1):
                return_value = self.get_book_link(book)
                time.sleep(1)
                # wait_value = self.wait_for_page_to_load()
                # while(wait_value):
                #     wait_value = self.wait_for_page_to_load()

            seller_info['link'] = return_value
            seller_info['name'] = 'GMU Bookstore'
            seller_info['location'] = 'Fairfax Campus'
            seller_info['verified'] = True

            book_info['department'] = self.department
            book_info['course'] = self.course
            book_info['sellers'] = []

            print("get book price")
            book_info, seller_info = self.get_book_price(book_info, seller_info, text)

            book_info['sellers'].append(seller_info)

            self.book_array.append(book_info)

        print(self.book_array)

        # self.book_info['link'] = link

    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'head')))
        except:
            return 1
        return 0

    def get_books(self):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'bned-cm-item-main-container'))
            )
            children = self.driver.find_elements(By.CLASS_NAME, 'bned-cm-item-main-container')

        except:
            return 1

        return children

    # def get_book_link(self, book):
    #     try:
    #         # element = WebDriverWait(self.driver, 1).until(
    #         #     EC.presence_of_element_located((By.XPATH,
    #         #                                     '/html/body/main/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/h3/a/span'))
    #         # )
    #         # element.click()
    #
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH,
    #                                             '/html/body/main'))
    #         )
    #
    #         link = book.find_elements_by_class_name('js-action-adoption-name')
    #
    #         print("1")
    #         # time.sleep(2)
    #         link[1].click()
    #
    #         WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH,
    #                                             '/html/body/main'))
    #         )
    #
    #         print("2")
    #         # time.sleep(2)
    #         url = self.driver.current_url
    #
    #         print("3")
    #         # time.sleep(1)
    #         self.driver.back()
    #
    #         print("4")
    #
    #     except:
    #         print("it broke")
    #         return 1
    #
    #     return url

    def get_book_link(self, book):
        try:
            # element = WebDriverWait(self.driver, 1).until(
            #     EC.presence_of_element_located((By.XPATH,
            #                                     '/html/body/main/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/h3/a/span'))
            # )
            # element.click()

            link = book.find_elements_by_class_name('js-action-adoption-name')

            print("1")
            time.sleep(2)
            link[1].click()

            print("2")
            time.sleep(2)
            url = self.driver.current_url

            print("3")
            # time.sleep(1)
            self.driver.back()

            print("4")

        except:
            print("it broke")
            return 1

        return url

    def get_book_text_element(self):
        print('text element')
        try:
            # element = WebDriverWait(self.driver, 1).until(
            #     EC.presence_of_element_located((By.ID, 'courseGroup_366_366_366_22_W_270_367_1'))
            # )
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div[4]/div[2]/div/div[2]/div'))
            )

            if(element.text == ''):
                raise Exception
        except:
            return 1

        return element

    def get_book_price(self, book, seller,str):
        first = str.index('\n') + 1
        second = str[first::].index('\n')

        name = str[first:first + second:]

        book['name'] = name

        index = str.find('Print\n$')
        if (index != -1):
            seller['buy'] = True
            seller['buy_price'] = float(str[index + 8:str.find("New Print") - 1:])
        else:
            seller['buy'] = False
            seller['buy_price'] = 0.0

        index = str.find('Rental\n$')
        if (index != -1):
            seller['rent'] = True
            seller['rent_price'] = float(str[index + 8:str.find("New Print Rental") - 1:])
        else:
            seller['rent'] = False
            seller['rent_price'] = 0.0

        index = str.find('Digital\n$')
        if (index != -1):
            seller['digital'] = True
            seller['digital_price'] = float(str[index + 9:str.find("Digital Purchase") - 1:])
        else:
            seller['digital'] = False
            seller['digital_price'] = 0.0

        return book, seller

    def get_book_author(self):
        return 0