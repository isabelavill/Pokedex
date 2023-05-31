from telas.tela_sistema import TelaSistema
from entidades.pokemon import Pokemon
import os

class ControladorPokemon:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema=controlador_sistema
        self.__tela_sistema=TelaSistema()
        self.__pokemons=[]
        self.__codigo= 0

    @property
    def pokemons(self):
        return self.__pokemons

    @property
    def tela_sistema(self):
        return self.__tela_sistema

    def cadastrar_pokemon(self):
        self.__tela_sistema.mensagem("Cadastro de Pokemon:")
        dados_pokemon=self.__tela_sistema.pega_dados_pokemon()
        self.__codigo+=1
        pokemon=Pokemon(dados_pokemon["nome"], dados_pokemon["tipo"], dados_pokemon["raridade"], self.__codigo)
        self.__pokemons.append(pokemon)
        os.system('cls')
        self.__tela_sistema.mensagem('Pokemon cadastrado com sucesso!')
    
    def listar_pokemons(self):
        if len(self.__pokemons)!=0:
            self.__tela_sistema.mensagem("Lista de Pokemons cadastrados:")
            for pokemon in self.__pokemons:
                self.__tela_sistema.mostra_pokemon(pokemon)
        else:
            self.__tela_sistema.mensagem("Ainda não há pokemons cadastrados no sistema.")
    
    def comparar_pokemons(self):
        pass

