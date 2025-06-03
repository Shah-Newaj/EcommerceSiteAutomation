from selenium.webdriver.common.by import By
from pageObjects.checkout_confirmation import Checkout_Confirmation


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.shop_link = (By.XPATH, "//a[contains(@href,'shop')]")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")



    def add_product_to_cart(self, productName):
        # //a[contains(@href,'shop')]   a[href*='shop']
        self.driver.find_element(*self.shop_link).click()

        products = self.driver.find_elements(*self.product_cards)
        # product_names = [product.text for product in products]

        for product in products:
            product_names = product.find_element(By.XPATH, "div/h4/a").text  # Chaining Used in the locator here
            if product_names == productName:
                product.find_element(By.XPATH, "div/button").click()  # Chaining Used in the locator here

    def goToCart(self):
        # ------------------------ Click on checkout on product page ----------------------------
        self.driver.find_element(*self.checkout_button).click()
        # checkout_confirmation Object creation got encapsulated here
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation
