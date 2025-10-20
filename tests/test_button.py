from selenium.webdriver.common.by import By

def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    assert driver.find_element(By.ID, "submit-id-submit").is_displayed()

