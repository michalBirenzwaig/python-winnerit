class LoginPage:

    def __init__(self,browser):
        self.browser=browser

    def home_page(self):
        self.browser.get("https://www.saucedemo.com/")

    def fill_username(self):
        username_input=self.browser.find_element(By.ID,"user-name") # [id="user-name] | #user-name
        username_input.clear()
        username_input.send_keys("standard_user")

    def fill_password(self):
        password_input=self.browser.find_element(By.CSS_SELECTOR,'[data-test="password"]')
        password_input.clear()
        password_input.send_keys("secret_sauce")

    def click_ligin_button(self):
        login_button=self.browser.find_element(By.NAME,"login-button")
        login_button.click()