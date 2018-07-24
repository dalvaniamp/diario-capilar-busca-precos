from navegador import *
from selenium import webdriver
from analise_dados import *
from constantes import *
import distance

class PaginaDaLoja():  
    #Classe responsavel por buscar os produtos na loja e retornar seu preco

    @property
    def campoDeBusca(self):
        xpath=self.config['campo_busca']
        return self.driver.find_element_by_xpath(xpath)

    @property
    def botaoPesquisar(self):
        xpath=self.config['botao_pesquisar']
        return self.driver.find_element_by_xpath(xpath)
    
    @property
    def campoDescricaoDosProdutos(self):
        xpath=self.config['resultados_descricao']
        return self.driver.find_elements_by_xpath(xpath)

    @property
    def campoPrecoDosProdutos(self):
        xpath=self.config['resultados_preco']
        return self.driver.find_elements_by_xpath(xpath)

    def __init__(self,configDTO):
        self.driver=Navegador()
        self.config=configDTO        
        url=self.config['url']
        self.driver.get(url)   

    def buscaProduto(self,nomeDoProduto):
        self.__nomeDoProduto=nomeDoProduto
        self.campoDeBusca.clear()
        self.campoDeBusca.send_keys(nomeDoProduto)
        self.botaoPesquisar.click()
    
    def __procuraMelhorProduto(self):
        distanciaMinima=100
        itemSelecionado=0
        numeroDeProdutos=Constantes.NUMERO_PRODUTOS_ITERACAO
        for item in self.campoDescricaoDosProdutos[0:numeroDeProdutos]:
            distancia=AnaliseDeDados.Hamming(item.text,self.__nomeDoProduto)
            if distancia < distanciaMinima:
                itemSelecionado=item
                distanciaMinima=distancia 
        return item      
    
    def procuraPrecoDoProduto(self):
        produtoEscolhido=self.__procuraMelhorProduto()
        produtoEscolhido.click()
        preco = self.spanPreco.text
        print (preco)