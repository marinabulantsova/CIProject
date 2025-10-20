from selenium.webdriver.common.by import By

def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.ID, "submit-id-submit").is_displayed()

def test_button_exist_2(driver):
    driver.get("https://www.qa-practice.com/elements/button/like_a_button")
    assert driver.find_element(By.LINK_TEXT, "Click").is_displayed()