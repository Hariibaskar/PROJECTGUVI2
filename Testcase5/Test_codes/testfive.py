from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.nickname_xpath).send_keys('surya')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.otherid_xpath).send_keys('0982')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dirverlicense_xpath).send_keys('TN36Z201900256')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.licenseexpiry_xpath).send_keys('2026-05-11')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.ssnnumber_xpath).send_keys('nil')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.sinnumber_xpath).send_keys('nil')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.nationality_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.indian_xpath).send_keys('Indian')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.maritalstatus_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.single_xpath).send_keys('Single')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dob_xpath).send_keys('1997-05-11')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.gender_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.military_xpath).send_keys('No')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.saveI_xpath).click()
        time.sleep(10)
        assert self.driver.title == 'OrangeHRM'