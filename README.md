
### Systema de pruebas con un software automatizado
Se desarrolló diferentes pruebas al aplicativo de MeMo para verificar que las validaciones de datos de entrada estuvieran correctos por parte del usuario.


Las pruebas se realizaron con las siguientes herramientas y paquetes:
- Selenium 4.15.2
- pycharm 17.0.8.1+7-b1000.32 amd64
- Python 3.10
- chromedriver 
- from selenium.webdriver.common.by import By
- from selenium.webdriver.support.ui import WebDriverWait
- from selenium.webdriver.support import expected_conditions as EC
- from selenium.webdriver.common.keys import Keys
- from selenium.webdriver.support.ui import Select
- from selenium import webdriver
- import time
- import collections
- import unittest



Para instalar selenium hay que seguir estos pasos:


### Estas pruebas se encuentran en github
    ~$https://github.com/Yarifp/selenium.git


### Instalación de selenium

    ~$pip install selenium
    

### Instalación del webdriver

        Descargar el webdriver en:
       ~$https://chromedriver.chromium.org/downloads
       según la versión de google que se tenga, se debe descargar el chrome que corresponde.



### Verificación de la instalación de selenium levantamiento de la página principal de memo con el webdriver
```
    chrome_driver_path = "/home/vboxuser/Descargas/dchrome/chromedriver"
    webdriver.chrome.driver = chrome_driver_path
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get("https://memo.mrbotcr.com/")



I
