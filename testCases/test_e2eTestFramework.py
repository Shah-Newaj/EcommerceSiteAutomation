import json
import os
import sys
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage


test_data_path = './/testData/test_e2eTestFramework.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance

    loginPage = LoginPage(driver)
    shopPage = loginPage.login(test_list_item["userEmail"], test_list_item["userPassword"])    #shopPage Object creation got encapsulated in loginPage.login()
    shopPage.add_product_to_cart(test_list_item["productName"])
    # checkout_confirmation Object creation encapsulated in shopPage.goToCart()
    checkout_confirmation = shopPage.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("Ban")
    checkout_confirmation.validate_order()

    print(driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)

    time.sleep(3)
