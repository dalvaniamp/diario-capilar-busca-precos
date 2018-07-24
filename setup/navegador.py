from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Navegador():
    # Classe singleton que instancia o navegador 

    __driver = None

    def __new__(self):
        if Navegador.__driver is None:
            self.__iniciaNavegador(self)
        return Navegador.__driver
    
    def __iniciaNavegador(self):
        chrome_options = Options()  
        #chrome_options.add_argument("--headless") 
        self.__driver = webdriver.Chrome(chrome_options=chrome_options)

    def init(self):
        pass