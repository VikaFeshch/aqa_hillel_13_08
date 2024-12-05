from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:8000/hw_26.html")
time.sleep(1)

frame_1 = driver.find_element(By.XPATH, '//*[@id="frame1"]')
driver.switch_to.frame(frame_1)

inp_1 = driver.find_element(By.XPATH, '//*[@id="input1"]')



verify_input1 = driver.find_element(By.XPATH, '//button[contains(@onclick, "verifyInput(\'input1\')")]')
driver.switch_to.default_content()



frame_2 = driver.find_element(By.XPATH, '//*[@id="frame2"]')
driver.switch_to.frame(frame_2)
inp_2 = driver.find_element(By.XPATH, '//*[@id="input2"]')

verify_input2 = driver.find_element(By.XPATH, '//button[contains(@onclick, "verifyInput(\'input2\')")]')

driver.switch_to.default_content()