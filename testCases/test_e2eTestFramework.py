import os
import sys
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from pageObjects.loginPage import LoginPage
from pageObjects.shopPage import ShopPage


def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    loginPage = LoginPage(driver)
    shopPage = loginPage.login()    #shopPage Object creation got encapsulated in loginPage.login()
    shopPage.add_product_to_cart("Blackberry")
    # checkout_confirmation Object creation encapsulated in shopPage.goToCart()
    checkout_confirmation = shopPage.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ban")
    checkout_confirmation.validate_order()

    print(driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)

    time.sleep(3)
