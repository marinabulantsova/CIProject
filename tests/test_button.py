from selenium.webdriver.common.by import By
import allure

@allure.feature("Buttons")
@allure.story("Button")
def test_button_exist(driver):
    driver.get("https://www.qa-practice.com/elements/button/simple")
    with allure.step("Check button exist"):
        assert driver.find_element(By.ID, "submit-id-submit").is_displayed()

@allure.feature("Buttons")
@allure.story("LikeAButton")
def test_button_exist_2(driver):
    driver.get("https://www.qa-practice.com/elements/button/like_a_button")
    with allure.step("Check button exist"):
        assert driver.find_element(By.LINK_TEXT, "Click").is_displayed()

@allure.feature("FailTest")
@allure.story("1 == 0")
def test_fail(driver):
    assert 1 == 0