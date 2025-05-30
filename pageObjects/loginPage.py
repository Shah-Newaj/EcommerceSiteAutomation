from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username") #2 arguments storing in one variable
        self.password = (By.ID, "password")
        self.signIn_button = (By.ID, "signInBtn")


    def login(self):
        # before self, * is used to break the tuple into 2 arguments as 'find_element' accepts argument
        self.driver.find_element(*self.username_input).send_keys("rahulshettyacademy")
        self.driver.find_element(*self.password).send_keys("learning")
        self.driver.find_element(*self.signIn_button).click()