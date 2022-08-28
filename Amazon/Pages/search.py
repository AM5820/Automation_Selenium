
class Search_Buy:
    def __init__(self,driver):
        self.driver = driver
        
    def select_item(self,item_no):
        item_1 = self.driver.find_element(by='xpath',value=f'//div[@class="sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20"][{1}]')
        self.item_1_name = item_1.find_element(by='xpath',value='//span[@class="a-size-base-plus a-color-base a-text-normal"]').text
        
        item_1.find_element(by='xpath',value='//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]').click()
    
    def add_item(self):
        add_tocart = self.driver.find_element(by='xpath',value='//input[@id="add-to-cart-button"]')
        add_tocart.click()
        
    def view_cart(self):
        view_cart = self.driver.find_element(by='xpath',value='//input[@aria-labelledby="attach-sidesheet-view-cart-button-announce"] | //*[@id="sw-gtc"]/span/a | //*[@id="a-autoid-28-announce"] | //*[@id="nav-cart"]')
        view_cart.click()
    
    def cart_items(self):
        return self.driver.find_elements(by='xpath',value='//div[@class="a-section a-spacing-mini sc-list-body sc-java-remote-feature"]//span[@class="a-truncate-cut"]')
        
    def check_item(self):
        cart = self.cart_items()
        for item in cart:
            if item.text[:-1] in self.item_1_name:
                return 1