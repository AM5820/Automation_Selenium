from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import sys
sys.path.append('Pages')
from index import Index
from deals import TodaysDeals

class TodayDealsTC:
    def __init__(self):
        self.website = "https://www.amazon.com/"
        self.path    ="C:\\Users\\studa\\Downloads\\Compressed\\chromedriver_win32\\chromedriver.exe"   
                
    def launch_browser(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument('window-size=1024x768')
        self.service = Service(executable_path=self.path)
        self.driver  = webdriver.Chrome(service=self.service , options=self.chrome_options)
        self.driver.get(self.website)
        
    
    
    def Todays_deals_TC1(self):
        index = Index(self.driver)
        deals = TodaysDeals(self.driver)
        
        
        deals.check_country_panel()
        index.click_Todaysdeals()
        index.wait(2)
        deals.filter_results()
        index.wait(2)
        #navigate from page1 to page4
        for page in range(3):
            #-----------------------
            WebDriverWait(self.driver, timeout=10).until(index.next_page).click()
            index.wait(2)
            #index.next_page()
            #index.wait(3)
        
        # choose item randomly
        deals.choose_item()
        index.wait(2)
        # add to cart
        #--------------------------
        WebDriverWait(self.driver, timeout=10).until(deals.add_item).click()
        #deals.add_item()
    
    def close_driver(self):
        self.driver.close()