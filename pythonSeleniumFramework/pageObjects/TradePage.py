from selenium.webdriver.common.by import By


class TradePage:

    def __init__(self, driver):
        self.driver = driver

    # (By.CSS_SELECTOR, "input[id='navigation-symbol-search']")
    search = (By.CSS_SELECTOR, "input[id='navigation-symbol-search']")
    trade = (By.XPATH, "//button[@data-testid='trade-page-buttonn']")
    sell = (By.CSS_SELECTOR, "button[direction='sell']")
    quantity = (By.CSS_SELECTOR, "input[aria-label='Quantity Input']")
    order_type = (By.CSS_SELECTOR, "button[aria-label='Order Type']")
    market_order = (By.CSS_SELECTOR, "li[data-testid='order-type-dropdown:MARKET']")
    review_order_button = (By.ID, "review-order-button")
    send_order_button = (By.ID, "send-order-button")
    notification = (By.XPATH, "//div[text()= 'Notifications']")
    first_notification = (By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]")
    logout_button = (By.XPATH, "//div[text()='Log out']")
    def get_symbol(self):
        return self.driver.find_element(*TradePage.search)

    def get_trade_button(self):
        return self.driver.find_element(*TradePage.trade)

    def get_sell_button(self):
        return self.driver.find_element(*TradePage.sell)

    def get_quantity(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_quantity_input(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_order_type(self):
        return self.driver.find_element(*TradePage.order_type)

    def get_market_order_element(self):
        return self.driver.find_element(*TradePage.market_order)

    def get_review_order_button(self):
        return self.driver.find_element(*TradePage.review_order_button)

    def get_send_order_button(self):
        return self.driver.find_element(*TradePage.send_order_button)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_first_notification(self):
        return self.driver.find_element(*TradePage.first_notification)

    def verification_of_order(self):
        original_notification = []
        original_message = [
            self.driver.find_element(*TradePage.first_notification).text
        ]
        # print(original_message)

        for records in original_message:
            original_notification.append(records)
            print(original_notification)
        assert original_message == original_notification
        return original_message

    def get_logout_button(self):
        return  self.driver.find_element(*TradePage.logout_button)
    # for quantity in range(len(length)):
    #     self.driver.find_element(By.CSS_SELECTOR, "input[aria-label='Quantity Input']").\
    #         send_keys(Keys.BACKSPACE)
    # By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]"
