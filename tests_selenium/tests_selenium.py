import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from pythonProject.pages.login_page import LoginPage

@pytest.fixture()
def browser():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # after test
    sleep(5)

def test_standart_user_login(browser):
    browser.get("https://www.saucedemo.com/")
    login_page=LoginPage(browser)
    username_input=browser.find_element(By.ID,"user-name") # [id="user-name] | #user-name
    username_input.clear()
    username_input.send_keys("standard_user")
    password_input=browser.find_element(By.CSS_SELECTOR,'[data-test="password"]')
    password_input.clear()
    password_input.send_keys("secret_sauce")
    login_button=browser.find_element(By.NAME,"login-button")
    login_button.click()

    assert browser.current_url=="https://www.saucedemo.com/inventory.html"
    product_page_title=browser.find_element(By.XPATH,'//*[@data-test="title"]').text
    assert product_page_title=="Products"