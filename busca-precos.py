from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from configparser import ConfigParser

class PaginaDaLoja():  
    @property
    def campoDeBusca(self):
        xpath=self.config['xpath_campo_busca']
        return self.driver.find_element_by_xpath(xpath)

    @property
    def botaoPesquisar(self):
        xpath=self.config['xpath_botao_pesquisar']
        return self.driver.find_element_by_xpath(xpath)

    def __init__(self,configDTO):
        self.config=configDTO
        chrome_options = Options()  
        #chrome_options.add_argument("--headless") 
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        url=self.config['url']
        self.driver.get(url)   

    def buscaProduto(self,nomeDoProduto):
        self.campoDeBusca.clear()
        self.campoDeBusca.send_keys(nomeDoProduto)
        self.botaoPesquisar.click()
    
    def procuraPrecoDoProduto(self):
        print ("abc")  

class IniciaBuscaDePrecos():
    def __init__(self):
        config = ConfigParser()
        config.read('config.ini')
        secoes= config.sections()        
        for cada_secao in secoes:
            configDTO=dict()
            for (cada_chave, cada_valor) in config.items(cada_secao):
                configDTO[cada_chave]=cada_valor            
            pagina=PaginaDaLoja(configDTO)
            pagina.buscaProduto("creme")

t=IniciaBuscaDePrecos()




 