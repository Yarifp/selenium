from selenium import webdriver
import unittest
from selenium.webdriver.common.by import By
import collections
collections.Callable = collections.abc.Callable


#pruebas unitarias utilizando unittest
class UsandoUnittest(unittest.TestCase):

    def setUp(self):
        chrome_driver_path = "/home/vboxuser/Descargas/dchrome/chromedriver"
        # Esto informa a selenium sobre la ubicacion de chrome
        webdriver.chrome.driver = chrome_driver_path

    def test_usando_implicit_wait(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.get("https://memo.mrbotcr.com/")
        driver.find_element(By.ID,"open_menu")


if __name__ == '__main__':
    unittest.main()