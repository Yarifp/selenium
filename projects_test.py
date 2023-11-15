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

class projects_Test(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = "/home/vboxuser/Descargas/dchrome/chromedriver"
        webdriver.chrome.driver = chrome_driver_path

    def test_Projects(self):
        driver = webdriver.Chrome()
        driver.get("https://memo.mrbotcr.com/login")

        # Inicio de sesión
        usuario = driver.find_element(By.NAME, "email")
        usuario.send_keys("yarifp214@gmail.com")
        usuario.send_keys(Keys.ENTER)
        clave = driver.find_element(By.NAME, "passwd")
        clave.send_keys(".Maria25A")
        clave.send_keys(Keys.ENTER)
        driver.get("https://memo.mrbotcr.com/user/yarifp18/projects")
        time.sleep(2)

        Idproyecto = driver.find_element(By.XPATH, '//*[@id="project_cod"]')
        Idproyecto.send_keys("mrbott")
        time.sleep(2)


        Nombre = driver.find_element(By.ID, "project_name")
        Nombre.send_keys("mrbot")
        time.sleep(2)
        Descrip = driver.find_element(By.ID, "project_desc")
        Descrip.send_keys(6364373)


        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="project_cnty"]')))
        select2 = Select(driver.find_element(By.XPATH, '//*[@id="project_cnty"]'))
        select2.select_by_value("CR")

        other_element1 = driver.find_element(By.XPATH, '//*[@id="project_cnty"]')
        other_element1.send_keys(Keys.ENTER)

        click_derecho = driver.find_element(By.NAME, "btn_create_project")
        click_derecho.click()
        driver.quit()

        time.sleep(8)
if __name__ == '__main__':
    unittest.main()