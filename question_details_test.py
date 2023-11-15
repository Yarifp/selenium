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

class question_Details_Test(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = "/home/vboxuser/Descargas/dchrome/chromedriver"
        webdriver.chrome.driver = chrome_driver_path

    def test_Question(self):
        driver = webdriver.Chrome()
        driver.get("https://memo.mrbotcr.com/login")

        # Inicio de sesión
        usuario = driver.find_element(By.NAME, "email")
        usuario.send_keys("yarifp214@gmail.com")
        usuario.send_keys(Keys.ENTER)
        clave = driver.find_element(By.NAME, "passwd")
        clave.send_keys(".Maria25A")
        clave.send_keys(Keys.ENTER)
        driver.get("https://memo.mrbotcr.com/user/yarifp18/questions")

        time.sleep(2)
        select = Select(driver.find_element(By.XPATH, '//*[@id="question_dtype"]'))

        select.select_by_value("4")

        other_element = driver.find_element(By.XPATH, '//*[@id="question_dtype"]')
        other_element.send_keys(Keys.ENTER)

        time.sleep(2)
        # Espera a que el segundo menú desplegable sea visible y pueda interactuar con él
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="question_dtype"]')))

        time.sleep(5)
        # Espera a que el segundo menú desplegable sea visible y pueda interactuar con él

        Idpregunta = driver.find_element(By.ID, "question_code")
        Idpregunta.send_keys("848484")  # Corrected from -0 to "0"
        question_name = driver.find_element(By.NAME, "question_name")
        question_name.send_keys(22)  # Corrected from -0 to "0"
        question_desc = driver.find_element(By.ID, "question_desc")
        question_desc.send_keys(11)  # Corrected from -0 to "0"

        click_derecho = driver.find_element(By.ID, "btn_create_question")
        click_derecho.click()
        time.sleep(20)
        driver.quit()


if __name__ == '__main__':
    unittest.main()

