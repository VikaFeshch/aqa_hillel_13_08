from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/hw_26.html")
    yield driver
    driver.quit()

def test_frame_positive(driver):

    frame_1 = driver.find_element(By.XPATH, '//*[@id="frame1"]')
    frame_2 = driver.find_element(By.XPATH, '//*[@id="frame2"]')

    driver.switch_to.frame(frame_1)

    inp_1 = driver.find_element(By.ID, "input1")
    inp_1.send_keys("Frame1_Secret")
    verify_input1 = driver.find_element(By.XPATH, '//button[contains(@onclick, "verifyInput(\'input1\')")]')
    verify_input1.click()
    alert = Alert(driver)
    try:
        assert alert.text == "Верифікація пройшла успішно!"
        alert.accept()
    except AssertionError:
        print("Error: The text of the alert is not as expected")
        raise

    driver.switch_to.default_content()

    driver.switch_to.frame(frame_2)

    inp_2 = driver.find_element(By.ID, "input2")
    inp_2.send_keys("Frame2_Secret")
    verify_input2 = driver.find_element(By.XPATH, '//button[contains(@onclick, "verifyInput(\'input2\')")]')
    verify_input2.click()
    alert = Alert(driver)
    try:
        assert alert.text == "Верифікація пройшла успішно!"
        alert.accept()
    except AssertionError:
        print("Error: The text of the alert is not as expected")
        raise

    driver.switch_to.default_content()

def test_frame_negative(driver):

    frame_1 = driver.find_element(By.XPATH, '//*[@id="frame1"]')
    frame_2 = driver.find_element(By.XPATH, '//*[@id="frame2"]')

    driver.switch_to.frame(frame_1)

    inp_1 = driver.find_element(By.ID, "input1")
    inp_1.send_keys("Frame2_Secret")
    verify_input1 = driver.find_element(By.XPATH, '//button[contains(@onclick, "verifyInput(\'input1\')")]')
    verify_input1.click()
    alert = Alert(driver)
    try:
        assert alert.text == "Введено неправильний текст!"
        alert.accept()
    except AssertionError:
        print("Error: The text of the alert is not as expected")
        raise

    driver.switch_to.default_content()

    driver.switch_to.frame(frame_2)

    inp_2 = driver.find_element(By.ID, "input2")
    inp_2.send_keys("Frame1_Secret")
    verify_input2 = driver.find_element(By.XPATH, '//button[contains(@onclick, "verifyInput(\'input2\')")]')
    verify_input2.click()
    alert = Alert(driver)
    try:
        assert alert.text == "Введено неправильний текст!"
        alert.accept()
    except AssertionError:
        print("Error: The text of the alert is not as expected")
        raise

    driver.switch_to.default_content()

