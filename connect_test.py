from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import unittest
import collections
collections.Callable = collections.abc.Callable



class Turn_Io_Test(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = "/home/vboxuser/Descargas/dchrome/chromedriver"
        webdriver.chrome.driver = chrome_driver_path

    def test_form_Turn_io(self):
        driver = webdriver.Chrome()
        driver.get("https://memo.mrbotcr.com/login")

        # Inicio de sesión
        usuario = driver.find_element(By.NAME, "email")
        usuario.send_keys("yarifp214@gmail.com")
        usuario.send_keys(Keys.ENTER)
        clave = driver.find_element(By.NAME, "passwd")
        clave.send_keys(".Maria25A")
        clave.send_keys(Keys.ENTER)
        driver.get("https://memo.mrbotcr.com/user/yarifp18/channels")

        time.sleep(4)
        select = Select(driver.find_element(By.XPATH, '//*[@id="cnty_cod"]'))

        select.select_by_value("CR")

        other_element = driver.find_element(By.XPATH, '//*[@id="cnty_cod"]')
        other_element.send_keys(Keys.ENTER)

        # Espera a que el segundo menú desplegable sea visible y pueda interactuar con él
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="connection_id"]')))

        numero = driver.find_element(By.NAME, "channel_number")
        numero.send_keys("MrBot")
        time.sleep(3)
        canal = driver.find_element(By.NAME, "cn_name")
        canal.send_keys("Mrbot software solutions")  # Corrected from -0 to "0"
        Descripcion = driver.find_element(By.ID, "cn_desc")
        Descripcion.send_keys(11)  # Corrected from -0 to "0"
        # Set de instalación y actualización de chromedriver.exe

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="connection_id"]')))
        # Segundo menú desplegable
        select2 = Select(driver.find_element(By.XPATH, '//*[@id="connection_id"]'))
        select2.select_by_value("memo")

        other_element1 = driver.find_element(By.XPATH, '//*[@id="connection_id"]')
        other_element1.send_keys(Keys.ENTER)


        token = driver.find_element(By.NAME, "cn_token")
        token.send_keys("")

        api = driver.find_element(By.NAME, "cn_apikey")
        api.send_keys("8843999kdkdkdmc")
        web = driver.find_element(By.NAME, "webhook-input")
        web.send_keys("webhook")
        time.sleep(8)
        click_derecho = driver.find_element(By.XPATH, '//*[@id="formChannels"]/div[10]/button')
        click_derecho.click()
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    unittest.main()
