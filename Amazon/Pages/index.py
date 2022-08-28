from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class Index:
    def __init__(self,driver):
        self.driver  = driver
        
    def reload_page(self):
        return self.driver.refresh()
        
    
    def click_Todaysdeals(self):
        i=0
        while i<2:
            try:
                el = self.driver.find_element(by=By.LINK_TEXT,value="Today's Deals")
            except:
                el=None
                self.reload_page()
            finally:
                i+=1
        
        if el:
            el.click()
        
    def search(self,keyword):
        search_bar = self.driver.find_element(by='xpath',value='//input[@id="twotabsearchtextbox"]')
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.RETURN)
        
    


    def next_page(self,driver):
        pages = driver.find_elements(by='xpath',value='//*[@id="slot-15"]/div/div/div[3]/div/ul/li')
        return pages[-1].find_element(by='xpath',value='a')
        
    
    
    def wait(self,seconds):
        """wait for some time in seconds"""
        sleep(seconds)
    