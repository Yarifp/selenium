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

class form_User_Test(unittest.TestCase):

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
        driver.get("https://memo.mrbotcr.com/user/yarifp18/forms")
        time.sleep(3)
        titulo = driver.find_element(By.NAME, "form_name")
        titulo.send_keys("mrbot")
        Descrip = driver.find_element(By.NAME, "form_desc")
        Descrip.send_keys("848484")
        time.sleep(3)

        #1
        select = Select(driver.find_element(By.XPATH, '//*[@id="multimedia"]'))

        select.select_by_value("4")

        other_element = driver.find_element(By.XPATH, '//*[@id="multimedia"]')
        other_element.send_keys(Keys.ENTER)

        time.sleep(2)
        # Espera a que el segundo menú desplegable sea visible y pueda interactuar con él
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="multimedia"]')))

        # 2
        select1 = Select(driver.find_element(By.XPATH, '//*[@id="form_cloned"]'))

        select1.select_by_value("c96820da-6f5b-11ed-97d2-371f69c2d1de")

        other_element1 = driver.find_element(By.XPATH, '//*[@id="form_cloned"]')
        other_element1.send_keys(Keys.ENTER)

        time.sleep(2)
        # Espera a que el segundo menú desplegable sea visible y pueda interactuar con él
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="form_cloned"]')))

        click_derecho = driver.find_element(By.NAME, "btn_save_form")
        click_derecho.click()
        time.sleep(20)
        driver.quit()

if __name__ == '__main__':
    unittest.main()