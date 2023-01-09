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
        print("SUCCESSFULLY GET TITLE")


    def test_job(self, booting_function):
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
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.joiningdate_xpath).send_keys('2019-05-16')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.jobtitle_xpath).click()
        time.sleep(4)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.chiefexecutive_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Chief Executive Officer";',e)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.jobcatgory_xpath).click()
        time.sleep(3)
        e1=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.saleswork_xpath)
        time.sleep(4)
        self.driver.execute_script('arguments[0].innerHTML = "Sales Workers";',e1)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.subunit_xpath).click()
        time.sleep(3)
        e2=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.salesmarkting_xpath)
        time.sleep(5)
        self.driver.execute_script('arguments[0].innerHTML = "Sales & Marketing";',e2)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.location_xpath).click()
        time.sleep(3)
        e3=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.newyork_xpath)
        time.sleep(5)
        self.driver.execute_script('arguments[0].innerHTML = "New York Sales Office";',e3)
        time.sleep(3)
        e4=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.fulltime_xpath)
        self.driver.execute_script('arguments[0].innerHTML = "Full-Time Contract";',e4)
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.radiobutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.contractstart_xpath).send_keys('2019-05-16')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.contractend_xpath).send_keys('2021-05-16')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.savebutton_xpath).click()
        time.sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print("Success Fully Update Job Details")
