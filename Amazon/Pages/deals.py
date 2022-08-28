import random
from index import Index

class TodaysDeals:
    def __init__(self,driver):
        self.driver = driver
        
        
    def check_country_panel(self):
        try:
            x=self.driver.find_element(by='xpath',value='//*[@id="nav-main"]/div[1]/div')
        except:
            x=None
            pass
        if x :
            self.driver.find_element(by='xpath',value='//*[@id="nav-main"]/div[1]/div/div/div[3]/span[1]/span/input').click()
    
    def filter_results(self):
        self.headphone = self.driver.find_element(by='xpath',value='//*[@id="grid-main-container"]/div[2]/span[3]/span/ul/li[20]/label/input')
        self.grocery   = self.driver.find_element(by='xpath',value='//*[@id="grid-main-container"]/div[2]/span[3]/span/ul/li[18]/label/input')
        self.discount  = self.driver.find_element(by='xpath',value='//*[@id="grid-main-container"]/div[2]/span[6]/span/ul/li[2]/div/a')
        
        self.headphone.click()
        self.grocery.click()
        self.discount.click()
    
    
    def choose_item(self):
        """choose item by random"""
        all_items = self.driver.find_elements(by='xpath',value='//*[@id="grid-main-container"]/div[3]/div/div')
        item_selected = random.choice(all_items)
        item_selected.find_element(by='xpath',value='div/div/a[1]').click()
        
        
    def add_item(self,driver):
        return driver.find_element(by='xpath',value='//*[@id="a-autoid-0-announce"]')