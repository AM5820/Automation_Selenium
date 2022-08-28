from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import sys
sys.path.append('Pages')
from bookseat import BookSeat

class BookSeatTC:
    def __init__(self):
        self.website = "https://ksrtc.in/oprs-web/guest/home.do?h=1"
        self.path    ="C:\\Users\\studa\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe"
                
    def launch_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.service = Service(executable_path=self.path)
        self.driver  = webdriver.Chrome(service=self.service , options=self.chrome_options)
        self.driver.set_window_size(1024,768)
        self.driver.get(self.website)
        
    
    
    def book_seat_TC(self):
        bs = BookSeat(self.driver)
        sleep(3)
        bs.locate_journey()
        bs.available_dates()
        bs.select_date()
        self.driver.set_window_size(1180,768)
        WebDriverWait(self.driver, timeout=10).until(bs.search_bus).click()
        self.driver.set_window_size(1024,768)
        bs.make_seat()
        self.driver.execute_script('window.scrollBy(0,1650);')
        WebDriverWait(self.driver, timeout=10).until(bs.drop).click()
        self.driver.implicitly_wait(4)
        WebDriverWait(self.driver, timeout=10).until(bs.drop_choose).click()
        bs.customer_detail(6789125987,'am223@abc.com')
        bs.choose_seat()
        bs.passanger_detail('CHARLIE',1,44)
        bs.make_payment()
        
        
    
    def close_driver(self):
        self.driver.close()