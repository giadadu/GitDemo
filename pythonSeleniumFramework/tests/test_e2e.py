from time import sleep
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass


# ID, NAME, CLASS_NAME, LINK_TEXT, TAG_NAME, PARTIAL_LINK
# XPATH = //tag_name[@attribute_name='value'] ->


class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        trade = TradePage(self.driver)
        login.get_username().send_keys(data_load["username"])
        sleep(1)
        login.get_password().send_keys(data_load["password"])
        sleep(1)
        login.get_login_button().click()

        # self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
        # self.driver.find_element(By.ID, "accept").click()
        # trade.get_trade_button().click()
        trade.get_symbol().send_keys("AAPL")
        trade.get_symbol().send_keys(Keys.RETURN)

        # //button[@data-testid='TradeButton-buy']
        # .send_keys(Keys.COMMAND + "a")
        # .send_keys(Keys.DELETE)

        # This is Buy market order
        trade.get_sell_button().click()
        # self.driver.find_element(By.CSS_SELECTOR, "button[direction='sell']").click() length = str(
        # self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").get_attribute("value"))
        # print(length)
        trade.get_quantity().click()
        # trade.get_quantity_input()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACKSPACE)
        sleep(2)
        trade.get_quantity_input().send_keys(15)
        trade.get_order_type().click()
        # for quantity in range(len(length)):
        #     self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(Keys.BACKSPACE)
        # driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(Keys.COMMAND + "a")
        # driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(Keys.DELETE)
        # self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").send_keys(2)
        # self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Order Type']").click()
        # select = Select(driver.find_element(By.CSS_SELECTOR, "button[aria-label='Order Type']"))
        # select.select_by_visible_text('MARKET')
        # self.driver.find_element(By.CSS_SELECTOR, "li[data-testid='order-type-dropdown:MARKET']").click()
        # self.driver.find_element(By.ID, "review-order-button").click()
        # self.driver.find_element(By.ID, "send-order-button").click()
        # self.driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click()
        trade.get_market_order_element().click()
        sleep(2)
        trade.get_review_order_button().click()
        trade.get_send_order_button().click()

        trade.get_notification().click()
        trade.verification_of_order()
        # original_notification = []
        # original_message = [
        #     trade.get_first_notification().text]
        # print(original_message)
        # print(original_notification)
        # for records in original_message:
        #     original_notification.append(records.strip(" "))

        # print(original_notification)
        # check_message = "AAPL MKT has been submitted"
        # print(check_message)
        # assert check_message in original_message
        # assert original_message == original_notification
        trade.get_logout_button().click()
        print("my 1st change")
        print("my 2nd change")
    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param
