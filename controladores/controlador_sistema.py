from telas.tela_sistema import TelaSistema
from controladores.controlador_pokemon import ControladorPokemon
from time import sleep
import os


class ControladorSistema:
    def __init__(self):
        self.__tela_sistema = TelaSistema()
        self.__controlador_pokemon = ControladorPokemon(self)

    @property
    def controlador_pokemon(self):
        return self.__controlador_pokemon

    def inicializa_sistema(self):
        print("Bem-vindo(a)!")
        sleep(1)
        os.system("cls")
        self.abre_tela()

    def cadastro_pokemon(self):
        self.__controlador_pokemon.cadastrar_pokemon()

    def listar_pokemons(self):
        self.__controlador_pokemon.listar_pokemons()

    def comparar_pokemons(self):
        self.__controlador_pokemon.comparar_pokemons()

    def encerra_sistema(self):
        print("Até logo!")
        sleep(1)
        exit()

    def abre_tela(self):
        lista_opcoes = {
            1: self.cadastro_pokemon,
            2: self.listar_pokemons,
            0: self.encerra_sistema,
        }

        while True:
            opcao = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao]
            os.system("cls")
            funcao_escolhida()
