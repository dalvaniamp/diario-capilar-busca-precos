from setup.navegador import Navegador
from setup import constantes
from utils.analise_dados import AnaliseDeDados
from selenium import webdriver

class PaginaDaLoja():  
    #Classe responsavel por buscar os produtos na loja e retornar seu preco

    @property
    def campo_de_busca(self):
        xpath=self.config['campo_busca']
        return self.driver.find_element_by_xpath(xpath)

    @property
    def botao_pesquisar(self):
        xpath=self.config['botao_pesquisar']
        return self.driver.find_element_by_xpath(xpath)
    
    @property
    def campo_descricao_dos_produtos(self):
        xpath=self.config['resultados_descricao']
        return self.driver.find_elements_by_xpath(xpath)

    @property
    def campo_preco_dos_produtos(self):
        xpath=self.config['resultados_preco']
        return self.driver.find_element_by_xpath(xpath)

    def __init__(self,config_dto):
        self.driver=Navegador()
        self.config=config_dto        
        url=self.config['url']
        self.driver.get(url)   

    def busca_produto(self,nome_do_produto):
        self.__nome_do_produto=nome_do_produto
        self.campo_de_busca.clear()
        self.campo_de_busca.send_keys(self.__nome_do_produto)
        self.botao_pesquisar.click()
    
    def __procura_melhor_produto(self):
        distancia_minima=100
        item_selecionado=0
        numero_de_produtos=constantes.NUMERO_PRODUTOS_ITERACAO
        for item in self.campo_descricao_dos_produtos[0:numero_de_produtos]:
            distancia=AnaliseDeDados.levenshtein(item.text,self.__nome_do_produto)
            if distancia < distancia_minima:
                item_selecionado=item
                distancia_minima=distancia 
        return item_selecionado      
    
    def procura_preco_do_produto(self):
        produto_escolhido=self.__procura_melhor_produto()
        produto_escolhido.click()
        preco = self.campo_preco_dos_produtos.text
        print (preco)