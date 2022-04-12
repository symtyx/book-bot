from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Book_Scrapper:
    def __init__(self, book_array, driver, department, course, section):
        self.driver = driver
        self.book_dict = {}
        self.department = department
        self.course = course
        self.section = section
        self.book_array = book_array
        
    def compile_book(self):
        self.get_book_info()

    def get_book_info(self):
        print('get book')
        return_value = 1
        book_text = []
        book_info = {}

        book_info['department'] = self.department
        book_info['course'] = self.course
        book_info['section'] = self.section
        book_info['sellers'] = []

        while(return_value == 1):
            return_value = self.get_books()
            if(self.check_book() == 0):
                book_info['name'] = ''
                self.book_array.append(book_info)
                return

        books = return_value

        for book in books:
            print(book.text)
            while(book.text == ''):
                time.sleep(1)

            book_text.append(book.text)

        print(book_text)
        # for index in range(len(books)):
        index = 0
        print('get book from books')
        return_value = 1


        text = book_text[index]

        return_value = 1
        while (return_value == 1):
            return_value = self.get_book_link(index)
            time.sleep(1)
                # wait_value = self.wait_for_page_to_load()
                # while(wait_value):
                #     wait_value = self.wait_for_page_to_load()

        seller_info = {}
        seller_info['name'] = 'GMU Bookstore'
        seller_info['location'] = 'Fairfax Campus'
        seller_info['verified'] = True
        seller_info['link'] = return_value

        print("get book price")
        book_info, seller_info = self.get_book_price(book_info, seller_info, text)

        book_info['sellers'].append(seller_info)

        self.book_array.append(book_info)

        print(book_info)

    def click_book(self,index):
        try:
            return_value = 1
            while (return_value == 1):
                return_value = self.get_book_element(index)

            # book = return_value[index]
            # book.click()
        except:
            print("couldn't click")
            return 1
        return 0

    def check_book(self):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div[4]')))
            if('Course Materials Selection Pending' not in element.text):
                 raise Exception
        except:
            return 1
        return 0
    def wait_for_page_to_load(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'head')))
        except:
            return 1
        return 0

    def get_book_element(self, index):
        print("get book element")
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'js-bned-item-name-text'))
            )
            children = self.driver.find_elements(by=By.CLASS_NAME, value='js-bned-item-name-text')

            while(self.driver.current_url == 'https://gmu.bncollege.com/course-material-listing-page?bypassCustomerAdoptions=true'):
                children[index].click()
                print('click')
        except:
            return 1

        return 0

    def get_books(self):
        print("get books")
        try:
            # FIXME: Fix it so that courses that don't have any materials
            # doesn't hang and returns null or something
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME,
                                                'bned-cm-item-main-container'))
            )
            children = self.driver.find_elements(by=By.CLASS_NAME, value='bned-cm-item-main-container')
        except:
            return 1

        return children


    def get_book_link(self, index):
        try:
            element = WebDriverWait(self.driver, 1).until(
                EC.presence_of_element_located((By.XPATH,
                                                '/html/body/main/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/h3/a/span'))
            )
            element.click()
            # time.sleep(3)
            # book_element = '//*[@id="courseGroup_366_366_366_22_W_100_203_4"]/div/div[{}]/div[2]/div[2]/div[1]/div/h3/a/span'.format(index + 1)

            # element = WebDriverWait(self.driver, 1).until(
            #     EC.presence_of_element_located((By.XPATH, book_element))
            # )
            # element.click()
            # time.sleep(3)
            # Click on book and then get the current_url
            strUrl = self.driver.current_url
            # time.sleep(3)
            # self.driver.back()
            # time.sleep(3)

        except:
            print("it broke")
            return 1

        return strUrl

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
            # seller['buy_price'] = float(str[index + 8:str.find("Print") - 1:])
            seller['buy_price'] = float(str[index + 7:str.find("New Print") - 1:])
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