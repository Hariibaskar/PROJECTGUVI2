from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Hari:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS")
    
    def test_login(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_username).send_keys(data.Hari_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_password).send_keys(data.Hari_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.login_xpath).click()
        time.sleep(3)
        assert self.driver.title == 'OrangeHRM'
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.admin_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dropdown_xpath).click()
        time.sleep(5)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.userrole_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Admin";',e)
        time.sleep(5)
        e1=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.status_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Enabled";',e1)      
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dropdown_xpath).click()
        time.sleep(5)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.userrole_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "ESS";',e)
        time.sleep(5)
        e1=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.status_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Disabled";',e1)
        time.sleep(8)
        assert self.driver.title == 'OrangeHRM'
        

        print("success")