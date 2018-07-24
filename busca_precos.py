from utils import email_utils
from configparser import ConfigParser
from setup import constantes

class IniciaBuscaDePrecos():
    def __init__(self):
        lojas=self.__serializaConfig()
        for loja in lojas:       
            pagina=PaginaDaLoja(lojas[loja])
            pagina.buscaProduto("Milagre Lola")
            pagina.procuraPrecoDoProduto()    

    def __serializaConfig(self):                
        lojas = dict()
        config = ConfigParser()
        try:
            config.read(Constantes.NOME_ARQUIVO_CONFIG)            
        except IOError:
            EmailUtils.enviaEmail(Constantes.MENSAGEM_CONFIG_NAO_ENCONTRADO)
            exit()
        for cada_secao in config.sections():         
                if self.__verificaSecaoDoConfig(config,cada_secao):
                    dadosDaLoja=dict()               
                    for (cada_chave, cada_valor) in config.items(cada_secao):
                        dadosDaLoja[cada_chave]=cada_valor 
                    lojas[cada_secao]=dadosDaLoja
        return lojas

    def __verificaSecaoDoConfig(self,config,secao):        
        secaoValida=True
        for campo in Constantes.LISTA_CAMPOS_ARQUIVO_CONFIG:
            if not config.has_option(secao, campo):
                secaoValida=False
                EmailUtils.enviaEmail(Constantes.MENSAGEM_CONFIG_INVALIDO.format(secao,campo))
                break
        return secaoValida
            
IniciaBuscaDePrecos()


 
