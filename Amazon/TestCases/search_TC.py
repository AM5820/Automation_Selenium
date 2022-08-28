from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append('Pages')
from index import Index
from search import Search_Buy

class SearchBuyTC:
    def __init__(self):
        self.website = "https://www.amazon.com/"
        self.path    ="C:\\Users\\studa\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe"   
                
    def launch_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('window-size=1024x768')
        self.service = Service(executable_path=self.path)
        self.driver  = webdriver.Chrome(service=self.service , options=self.chrome_options)
        self.driver.get(self.website)
        
    
    
    def search_buy_TC1(self):
        index = Index(self.driver)
        sb    = Search_Buy(self.driver)
        
        # search website
        index.search('car accessories')
        # select item x
        sb.select_item(1)
        # add item to cart
        sb.add_item()
        # view cart
        sb.view_cart()
        # check item in cart
        if sb.check_item():
            print("item added successfully")
        
        
    def close_driver(self):
        self.driver.close()