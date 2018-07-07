from pagina_loja import *
from configparser import ConfigParser

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
            pagina.buscaProduto("Milagre Lola")
            pagina.procuraPrecoDoProduto()
            
            
IniciaBuscaDePrecos()


 