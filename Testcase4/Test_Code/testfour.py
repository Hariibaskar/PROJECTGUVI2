from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_HARI:
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
        print("SUCCESSFULLY GET TITLE")
    
    def test_validate(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.HARI_Selectors.input_box_username).send_keys(data.HARI_Data.username)
        self.driver.find_element(by=By.NAME, value=data.HARI_Selectors.input_box_password).send_keys(data.HARI_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.login_xpath).click()
        time.sleep(3)
        assert self.driver.title == 'OrangeHRM'
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.pim_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.emp_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.personal_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.contact_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.emergy_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.dependents_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.immigration_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.job_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.salary_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.tax_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.report_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.quali_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.HARI_Selectors.member_xpath).click()
        time.sleep(5)
        print("SUCCESSFULLY VALIDATE GIVEN TABS")