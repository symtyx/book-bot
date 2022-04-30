from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Book_Scrapper:
    
    # Constructor function that will set self object attributes.
    def __init__(self, book_array, driver, department, course, section):
        self.driver = driver
        self.book_dict = {}
        self.department = department
        self.course = course
        self.section = section
        self.book_array = book_array

    # Function which complies a book's details from self object.
    def compile_book(self):
        self.get_book_info()

    # Function which gets information of a book.
    def get_book_info(self):
        # print('get book')
        return_value = 1
        book_text = []
        book_info = {}

        book_info['department'] = self.department
        book_info['course'] = self.course
        book_info['section'] = self.section
        book_info['sellers'] = []

        # checks if there are textbooks for a course
        # if there are none then it returns with no seller info or book name
        while(return_value == 1):
            return_value = self.get_books()
            if(self.check_book() == 0):
                book_info['name'] = ''
                self.book_array.append(book_info)
                return 0

        # stores the different books
        books = return_value

        # stores the text of the element that holds the textbook info
        for book in books:
            # wait for the text to load on the page
            while(book.text == ''):
                time.sleep(1)
            book_text.append(book.text)

        # loops through each book
        # for index in range(len(books)):
            # print('get book from books')

        index = 0
        book_info = {}
        book_info['department'] = self.department
        book_info['course'] = self.course
        book_info['section'] = self.section
        book_info['sellers'] = []

        text = book_text[index]

        return_value = 1
        while (return_value == 1):
            return_value = self.get_book_link(index)
            time.sleep(1)
        
        seller_info = {}
        seller_info['name'] = 'GMU Bookstore'
        seller_info['location'] = 'Fairfax Campus'
        seller_info['verified'] = True
        seller_info['link'] = return_value

            # gets prices and buy options from the text of the book element
            # print("get book price")
        book_info, seller_info = self.get_book_price(book_info, seller_info, text)

            # add seller to book dictionary
        book_info['sellers'].append(seller_info)

            # add book to book array
        self.book_array.append(book_info)
        print(book_info)
        # return book_info

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
            if('No Course Materials Required' in element.text):
                return 0
            elif('Course Materials Selection Pending' not in element.text):
                 raise Exception
        except:
            return 1
        return 0

    
    def get_books(self):
        # print("get books")
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

    # Function will get a bookstore link for a book inside the inventory.
    # Returns 1 if a link does not exist or any error has occured.
    # If successful, the url string will be returned.
    def get_book_link(self, index):
        try:
            # book_element = '//*[@id="courseGroup_366_366_366_22_W_100_203_4"]/div/div[{}]/div[2]/div[2]/div[1]/div/h3/a/span'.format(index + 1)
    
            book_elem = "/html/body/main/div[3]/div[2]/div[4]/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/h3/a"
            element = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, book_elem))
            )
            element.click()
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

    # Function that gets a book's price from the GMU bookstore.
    # This will be placed underneath the bookstore link to easily compare prices from students.
    def get_book_price(self, book, seller,str):
        first = str.index('\n') + 1
        second = str[first::].index('\n')

        name = str[first:first + second:]

        book['name'] = name

        # for print version
        index = str.find('Print\n$')

        if (index != -1):
            seller['buy'] = True
            # seller['buy_price'] = float(str[index + 8:str.find("Print") - 1:])
            
            # Variable will return -1 if a used print version of the book is not available.
            buy_index = str.find('Used Print')
            if(buy_index != -1):
                
                # Bot will display the used print price.
                buy_str = str[buy_index - 9::]
                dollar_index = buy_str.find('$')
                buy_index = buy_str.find(' Used Print')
                seller['buy_price'] = float(buy_str[dollar_index + 1:buy_index:])
            else:
                seller['buy_price'] = float(str[index + 7:str.find(' New Print'):])
        else:
            seller['buy'] = False
            seller['buy_price'] = 0.0

        # for rental version
        # Variable will return -1 if a rental version of the book is not available.
        index = str.find('Rental\n$')
        if (index != -1):
            # temp_str = str[index + 7]
            # dollar_index = temp_str.find('$')
            
            # Bot will display the used print rental price.
            seller['rent'] = True
            rent_index = str.find('Used Print Rental')
            if(rent_index != -1):
                rent_str = str[rent_index - 9::]
                dollar_index = rent_str.find('$')
                rent_index = rent_str.find(' Used Print Rental')
                seller['rent_price'] = float(rent_str[dollar_index + 1:rent_index:])             
            elif(str.find('Rent Only') != -1):
                
                # If there is not used print rental, a rent only option will be printed.
                rent_str = str[str.find('Rent Only') - 9::]
                dollar_index = rent_str.find('$')
                rent_index = rent_str.find(' Rent Only')
                seller['rent_price'] = float(rent_str[dollar_index + 1:rent_index:])
            else:
                seller['rent_price'] = float(str[index + 8:str.find(' New Print Rental') :])
        else:
            # There is no rent option available for the book. Price is set to 0.0
            seller['rent'] = False
            seller['rent_price'] = 0.0

        # for digital version
        index = str.find('Digital\n$')
        if (index != -1):
            # temp_str = str[index + 9::]
            seller['digital'] = True

            rent_index = str.find('Digital Rental')
            
            # Bot will display the digital rental price if it is currently available.
            if(rent_index != -1):
                rent_str = str[rent_index - 9::]
                dollar_index = rent_str.find('$')
                rent_index = rent_str.find(' Digital Rental')
                seller['digital_price'] = float(rent_str[dollar_index + 1:rent_index:])

            else:
                temp = str[index:str.find('Digital Purchase') - 1:]
                seller['digital_price'] = float(str[index + 9:str.find(' Digital Purchase'):])
        else:
            # Digital version of the book does not exist.
            seller['digital'] = False
            seller['digital_price'] = 0.0

        return book, seller

    def get_book_author(self):
        return 0
