from pagina_loja import *
from configparser import ConfigParser
from email_utils import *

class IniciaBuscaDePrecos():
    def __init__(self):
        configDTO=self.__serializaConfig()
        for loja in configDTO:       
            pagina=PaginaDaLoja(configDTO[loja])
            pagina.buscaProduto("Milagre Lola")
            pagina.procuraPrecoDoProduto()    

    def __serializaConfig(self):                
        configDTO=dict()
        config = ConfigParser()
        config.read('config.ini')
        for cada_secao in config.sections():         
            if self.__verificaSecaoDoConfig(config,cada_secao):
                tempDTO=dict()               
                for (cada_chave, cada_valor) in config.items(cada_secao):
                    tempDTO[cada_chave]=cada_valor 
                configDTO[cada_secao]=tempDTO
        return configDTO

    def __verificaSecaoDoConfig(self,config,secao):
        listaDeCamposDoConfig=['url','xpath_campo_busca','xpath_botao_pesquisar','xpath_grid_resultados','xpath_span_preco']
        secaoValida=True
        for campo in listaDeCamposDoConfig:
            if not config.has_option(secao, campo):
                secaoValida=False
                EmailUtils.enviaEmail('o config ta zoado lol')
                break
        return secaoValida
            
IniciaBuscaDePrecos()


 
