import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()   # cần cài chromedriver
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.get("http://localhost:5000/login")   # sửa port theo Lab04
    driver.find_element(By.NAME, "username").send_keys("demo")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    assert "Welcome" in driver.page_source

def test_login_wrong_password(driver):
    driver.get("http://localhost:5000/login")
    driver.find_element(By.NAME, "username").send_keys("demo")
    driver.find_element(By.NAME, "password").send_keys("wrong")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    assert "Invalid" in driver.page_source

def test_login_empty_input(driver):
    driver.get("http://localhost:5000/login")
    driver.find_element(By.NAME, "username").send_keys("")
    driver.find_element(By.NAME, "password").send_keys("")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    assert "Please enter" in driver.page_source
