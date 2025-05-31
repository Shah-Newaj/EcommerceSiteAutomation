from selenium.webdriver.common.by import By

from pageObjects.shopPage import ShopPage


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        # 2 arguments storing in one variable. Packed in one variable so in action method unpacking will be needed.
        self.username_input = (By.ID, "username")
        self.password = (By.ID, "password")
        self.signIn_button = (By.ID, "signInBtn")


    def login(self):
        # before self, * is used to break/unpack the tuple into 2 arguments as 'find_element' accepts argument
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.signIn_button).click()
        # shopPage Object creation got encapsulated here
        shopPage = ShopPage(self.driver)
        return shopPage