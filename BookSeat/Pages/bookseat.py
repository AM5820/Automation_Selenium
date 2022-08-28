import random
import datetime

class BookSeat:
    def __init__(self,driver):
        self.driver = driver
        self.dates  = []
        
    def locate_journey(self):
        while True:
            try:
                cb = self.driver.find_element(by='xpath',value='//*[@id="routeSlider"]/div/div[2]/div/div/ul/li[1]/a')
                cb.click()
                break

            except: 
                swap_right = self.driver.find_element(by='xpath',value='//*[@id="routeSlider"]/div/a[2]')
                swap_right.click()
    
    
    
    def available_dates(self):
        trows = self.driver.find_elements(by='xpath',value='//*[@id="ui-datepicker-div"]/table/tbody/tr')
        for row in trows:
            days = row.find_elements(by='xpath',value='td')
            for day in days:
                av_day = None
                try: 
                    av_day = day.find_element(by='xpath',value='a')
                except:
                    pass
                finally:
                    if av_day:
                        self.dates.append(av_day.text)
    
    
    
    def select_date(self):
        today = datetime.datetime.now().day
        dates = [i for i in self.dates if abs(int(i)-today)>1]
        selected_date = random.choice(self.dates)
        self.driver.find_element(by='link text',value=selected_date).click()
        
    def search_bus(self,driver):
        search_bus = driver.find_element(by='xpath',value='//*[@id="bookingsForm"]/div[1]/div/div[2]/div[3]/button')
        return search_bus
        
    def make_seat(self):
        make_seat = self.driver.find_element(by='xpath',value='//*[@id="ForwardResults"]/div[2]/div[1]/div[1]/div[5]/div//input[@id="SrvcSelectBtnForward0"]')
        make_seat.click()
    
    def drop(self,driver):
        return driver.find_element(by='xpath',value='//*[@id="Forwarddroping-tab"]')

    
    def drop_choose(self,driver):
        return driver.find_element(by='xpath',value='//*[@id="Forwarddroping"]/div/div/ul/li[1]')
        
    def customer_detail(self,mobile_no,email_address):
        customer_detail = self.driver.find_element(by='xpath',value='//*[@id="Forwardprofile-tab"]')
        customer_detail.click()
        
        mobile = self.driver.find_element(by='xpath',value='//*[@id="mobileNo"]')
        email = self.driver.find_element(by='xpath',value='//*[@id="email"]')

        mobile.send_keys(mobile_no)
        email.send_keys(email_address)
    
    def choose_seat(self):
        seats = self.driver.find_elements(by='xpath',value='//div[@class="bus-seat-layout-revamp  bus-seat-layout-main active"]//li')
        for seat in seats:
            try:
                if seat.get_attribute('class') == 'availSeatClassS':
                    seat.click()
                    break
            except:
                pass
    
    def passanger_detail(self,pass_name,pass_gender,pass_age):
        """pass_gender= {0:MALE ,1:FEMALE}"""
        dropdown_detail = self.driver.find_element(by='xpath',value='//*[@id="passenger-details"]/div/p/a')
        dropdown_detail.click()
        
        name = self.driver.find_element(by='xpath',value='//*[@id="passengerNameForward0"]')
        name.send_keys(pass_name)
        

        gender_select = self.driver.find_element(by='xpath',value='//*[@id="genderCodeIdForward0"]')
        gender_select.click()

        sex_type = self.driver.find_element(by='xpath',value=f'//*[@id="genderCodeIdForward0"]/option[{pass_gender+1}]')
        sex_type.click()
        
        age = self.driver.find_element(by='xpath',value='//*[@id="passengerAgeForward0"]')
        age.send_keys(pass_age)
        
        
        concession_select = self.driver.find_element(by='xpath',value='//*[@id="concessionIdsForward0"]')
        concession_select.click()

        general = self.driver.find_element(by='xpath',value='//*[@id="concessionIdsForward0"]/option[2]')
        general.click()
        
        
        country_india = self.driver.find_element(by='xpath',value='//*[@id="nationalityForward0"]/option[1]')
        country_india.click()

        
    def make_payment(self):
        payment = self.driver.find_element(by='xpath',value='//*[@id="PgBtn"]')
        payment.click()