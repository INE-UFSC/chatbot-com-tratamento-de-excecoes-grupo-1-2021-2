# implemente as seguintes classes

from ..SistemaChatBot.Comando import Comando
from abc import ABC, abstractmethod
import random as r


class Bot(ABC):

    def __init__(self, nome):
        self.__nome = nome
        self.__comandos = []

    # nao esquecer o decorator
    def nome(self):
        pass

    # nao esquecer o decorator
    def nome(nome):
        pass

    def mostra_comandos(self):
        pass

    def cria_comando(self, id, msg, respostas):
        return Comando(id, msg, respostas)

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass

    @abstractmethod
    def despedida():
        pass
