from navegador import *
from selenium import webdriver

class PaginaDaLoja():  
    #Classe responsavel por buscar os produtos na loja e retornar seu preco

    @property
    def campoDeBusca(self):
        xpath=self.config['xpath_campo_busca']
        return self.driver.find_element_by_xpath(xpath)

    @property
    def botaoPesquisar(self):
        xpath=self.config['xpath_botao_pesquisar']
        return self.driver.find_element_by_xpath(xpath)
    
    @property
    def gridResultado(self):
        xpath=self.config['xpath_grid_resultados']
        return self.driver.find_element_by_xpath(xpath)

    @property
    def spanPreco(self):
        xpath=self.config['xpath_span_preco']
        return self.driver.find_element_by_xpath(xpath)

    def __init__(self,configDTO):
        self.driver=Navegador()
        self.config=configDTO        
        url=self.config['url']
        self.driver.get(url)   

    def buscaProduto(self,nomeDoProduto):
        self.campoDeBusca.clear()
        self.campoDeBusca.send_keys(nomeDoProduto)
        self.botaoPesquisar.click()
    
    def procuraPrecoDoProduto(self):
        self.gridResultado.click()
        preco = self.spanPreco.text
        print (preco)