from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import collections
import unittest

collections.Callable = collections.abc.Callable

class FormUserTest(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = "/home/vboxuser/Descargas/dchrome/chromedriver"
        webdriver.chrome.driver = chrome_driver_path

    def test_form(self):
        driver = webdriver.Chrome()
        driver.get("https://memo.mrbotcr.com/login")

        # Inicio de sesión
        usuario = driver.find_element(By.NAME, "email")
        usuario.send_keys("yarifp214@gmail.com")
        usuario.send_keys(Keys.ENTER)
        clave = driver.find_element(By.NAME, "passwd")
        clave.send_keys(".Maria25A")
        clave.send_keys(Keys.ENTER)
        time.sleep(3)
        driver.get("https://memo.mrbotcr.com/user/yarifp18/project/mrbott/details")
        time.sleep(5)
        Nombre = driver.find_element(By.NAME, "cp_name")
        Nombre.send_keys("mrbot")
        time.sleep(4)

        # 1st dropdown
        time.sleep(4)
        select = Select(driver.find_element(By.XPATH, '//*[@id="channel_id"]'))
        select.select_by_value("15aeae6c-8245-11ee-a38e-0242c0a80202")

        other_element = driver.find_element(By.XPATH, '//*[@id="channel_id"]')
        other_element.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="channel_id"]')))

        # 2nd dropdown
        time.sleep(4)
        select2 = Select(driver.find_element(By.XPATH, '//*[@id="form_id"]'))
        select2.select_by_value("4acd4cc6-8299-11ee-a38e-0242c0a80202")

        other_element = driver.find_element(By.XPATH, '//*[@id="form_id"]')
        other_element.send_keys(Keys.ENTER)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form_id"]')))

        try:
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "external-events"))
            )
            element.click()

        except Exception as e:
            print(f"Error: {e}")

        # Handle readonly attribute
        input_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cp_start"))
        )
        driver.execute_script("arguments[0].readOnly = true;", input_element)

        input_element2 = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cp_end"))
        )
        driver.execute_script("arguments[0].readOnly = true;", input_element2)

        # Click on the element using WebDriverWait
        try:
            click_derecho = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "btn_edit_campaign"))
            )
            click_derecho.click()

        except Exception as e:
            print(f"Error clicking on the element: {e}")

        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
