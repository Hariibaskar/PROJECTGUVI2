from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Hari:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("Successfull get title")

    def test_login(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_username).send_keys(data.Hari_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_password).send_keys(data.Hari_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.pim_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.add_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_firstName).send_keys(data.Hari_Data.firstName)
        self.driver.find_element(by=By.NAME, value=data.Hari_Selectors.input_box_lastName).send_keys(data.Hari_Data.lastName)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.save_xpath).click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.taxbutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.fedaraldropdown_xpath).click()
        time.sleep(5)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.textinput_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Single";',e)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.exemption_xpath).send_keys('15')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.statedrop_xpath).click()
        time.sleep(5)
        e1=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Indiana_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = " Indiana ";',e1)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.statusdropdown_xpath).click()
        time.sleep(5)
        e2=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.singleinput_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = " Single ";',e2)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Exemption_xpath).send_keys('20')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Workdropdown_xpath).click()
        time.sleep(5)
        e3=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.indiana_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = " Indiana ";',e3)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Savebutton_xpath).click()
        time.sleep(8)
        assert self.driver.title == 'OrangeHRM'
        print("Successfully Update the Tax Exemptions")


        

        


