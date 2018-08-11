from utils.email_utils import EmailUtils
from configparser import ConfigParser
from setup import constantes
from pagina_loja import PaginaDaLoja

class IniciaBuscaDePrecos():
    def __init__(self):
        lojas=self.__serializa_config()
        for loja in lojas: 
            pagina=PaginaDaLoja(lojas[loja])
            pagina.busca_produto("Milagre Lola")
            pagina.procura_preco_do_produto() 
        PaginaDaLoja.fecha_navegador()

    def __serializa_config(self):                
        lojas = dict()
        config = ConfigParser()
        try:
            config.read(constantes.NOME_ARQUIVO_CONFIG)            
        except IOError:
            EmailUtils.enviaEmail(constantes.MENSAGEM_CONFIG_NAO_ENCONTRADO)
            exit()
        for cada_secao in config.sections():         
                if self.__verifica_secao_do_config(config,cada_secao):
                    dados_da_loja=dict()               
                    for (cada_chave, cada_valor) in config.items(cada_secao):
                        dados_da_loja[cada_chave]=cada_valor 
                    lojas[cada_secao]=dados_da_loja
        return lojas

    def __verifica_secao_do_config(self,config,secao):        
        secao_valida=True        
        for campo in constantes.LISTA_CAMPOS_ARQUIVO_CONFIG:
            if not config.has_option(secao, campo):
                secao_valida=False
                EmailUtils.enviaEmail(constantes.MENSAGEM_CONFIG_INVALIDO.format(secao,campo))
                break
        return secao_valida
            
IniciaBuscaDePrecos()


 
