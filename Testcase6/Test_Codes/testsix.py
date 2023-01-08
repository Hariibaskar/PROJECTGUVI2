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
        time.sleep(8)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.contactdetails_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.street1_xpath).send_keys('55a/21')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.street2_xpath).send_keys('anna nagar')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.city_xpath).send_keys('chennai')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.state_xpath).send_keys('Tamilnadu')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.postalcode_xpath).send_keys('600028')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Country_xpath).click
        time.sleep(5)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.india_xpath)
        time.sleep(5)
        self.driver.execute_script('arguments[0].innerHTML = " India ";',e)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.telephone_xpath).send_keys('0428-225336')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.mobile_xpath).send_keys('9566857115')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.work_xpath).send_keys('-')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.workemail_xpath).send_keys('haribaskarmnw@gmail.com')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.othermail_xpath).send_keys('haribaskarsurya@gmail.com')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Save_xpath).click()
        time.sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print("Successfully tested")

  