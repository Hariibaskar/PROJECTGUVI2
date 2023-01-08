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
        print("SUCCESS GET TITLE")

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
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.emergencycontacts_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.addbutton_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.name_xpath).send_keys('kumar r')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.realtionship_xpath).send_keys('friend')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.hometelephone_xpath).send_keys('-')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.mobileno_xpath).send_keys('9566859703')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.worktelephone_xpath).send_keys('-')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Save_xpath).click()
        time.sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print("Successfully tested")