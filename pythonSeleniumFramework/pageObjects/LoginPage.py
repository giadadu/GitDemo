# self.driver.find_element(By.ID, "username0").send_keys("gialodadu")
# self.driver.find_element(By.ID, "password1").send_keys("22Aprili")
# self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username0")
    password = (By.ID, "password1")
    loginButton = (By.ID, "accept")
    rememberUserId = (By.XPATH, "//label[@for='rememberuserid']")

    def get_remember_user_id(self):
        return self.driver.find_element(*LoginPage.rememberUserId)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.loginButton)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)
