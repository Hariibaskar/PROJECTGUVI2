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
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.job_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.terminatedbutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.terminationdate_xpath).send_keys('2021-05-17')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dropdown_xpath).click()
        time.sleep(5)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.selectinput_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Contract Not Renewed";',e)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.note_xpath).send_keys('All the very best your future')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.savebutton_xpath).click()
        time.sleep(8)
        assert self.driver.title == 'OrangeHRM'
        print("Successfuly Terminated Employee")
