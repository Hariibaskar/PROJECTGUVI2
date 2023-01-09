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
        print("SUCCESS")    

    def test_salary(self, booting_function):
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
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.salary_xpath).click()
        time.sleep(8)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.addbutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.salarycomponent_xpath).send_keys('basic salary')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dropdown_xpath).click()
        time.sleep(5)
        e=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.selectinput_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Grade 3";',e)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.dropdown2_xpath).click()
        time.sleep(3)
        e1=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.selectinput2_xpath)
        self.driver.execute_script('arguments[0].innerHTML = "Monthly";',e1)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.currencydropdown_xpath).click()
        time.sleep(3)
        e2=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.selectinput3_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Indian Rupee";',e2)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.amount_xpath).send_keys('150000')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.comments_xpath).send_keys('--')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.radiobutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.accountno_xpath).send_keys('122408956894')
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.ACtypedropdown_xpath).click()
        time.sleep(3)
        e3=self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.selectinput4_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Savings";',e3)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.routingnumber_xpath).send_keys('122408956')
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Amount_xpath).send_keys('200000')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Hari_Selectors.Savebutton_xpath).click()
        time.sleep(6)
        print("successfully updates the salary details")


        


        
        
