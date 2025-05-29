import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

def test_e2e(browserInstance):
    driver = browserInstance
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()
    driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    driver.find_element(By.ID, "password").send_keys("learning")
    driver.find_element(By.ID, "signInBtn").click()

    # //a[contains(@href,'shop')]   a[href*='shop']
    driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()

    elements = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
    # element_names = [ele.text for ele in elements]

    for element in elements:
        element_names = element.find_element(By.XPATH, "div/h4/a").text  # Chaining Used in the locator here
        if element_names == "Blackberry":
            element.find_element(By.XPATH, "div/button").click()  # Chaining Used in the locator here

    # ------------------------ Click on checkout on product page ----------------------------
    driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    # ------------------------ Click on Checkout on Cart Page --------------------------------
    driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

    driver.find_element(By.ID, "country").send_keys("ban")
    wait = WebDriverWait(driver, 10)  # initializing Explicit wait
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Bangladesh")))  # Applying Explicit Wait
    driver.find_element(By.LINK_TEXT, "Bangladesh").click()
    driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

    purchase = driver.find_element(By.XPATH, "//input[@value='Purchase']")
    purchase.click()

    successText = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
    assert "Success! Thank you!" in successText

    print(driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)

    time.sleep(3)
    # driver.close()
