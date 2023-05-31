from exceptions.valor_invalido_exception import ValorInvalido
from entidades.pokemon import Pokemon
import os

class TelaSistema:
    def tela_opcoes(self):
        print("Escolha um dos Menus:")
        print("[1] Cadastrar novo Pokemon.")
        print("[2] Listar Pokemons cadastrados.")
        print("[3] Comparar Pokemons.")
        print("[0] Finalizar sistema.")
        while True:
            try:
                opcao_escolhida = int(input("Opção: "))
                if 0 > opcao_escolhida or opcao_escolhida > 3:
                    raise ValorInvalido
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
            else:
                break
        os.system("cls")
        return opcao_escolhida
    
    def pega_dados_pokemon(self):
        nome = input('Nome do Pokemon: ')
        tipos = {1:'Normal', 2:'Fogo',3:'Água',4:'Elétrico', 5:'Grama',6:'Gelo',7:'Lutador'}
        print('Tipo:')
        while True:
            print("[1] Normal")
            print("[2] Fogo")
            print("[3] Água")
            print("[4] Elétrico")
            print("[5] Grama")
            print("[6] Gelo")
            print("[7] Lutador")
            try:
                opcao_tipo = int(input("Opção: "))
                if 1 > opcao_tipo or opcao_tipo > 7:
                    raise ValorInvalido
                else:
                    break
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite uma das opções.")
        while True:
            try:
                raridade = int(input("Raridade (-100/100): "))
                if -100 > opcao_tipo or opcao_tipo > 100:
                    raise ValorInvalido
                else:
                    break
            except (ValorInvalido, ValueError):
                print("Valor inválido! Digite um valor entre -100 e 100.")

        return {"nome": nome, "tipo": tipos[opcao_tipo], "raridade": raridade}
    
    def mostra_pokemon(self, pokemon:Pokemon):
        print()
        print(f"{pokemon.codigo}   Nome: {pokemon.nome}")
        print(f'    Tipo: {pokemon.tipo}')
        print(f'    Raridade: {pokemon.raridade}')
        print()


    def mensagem(self, mensagem: str):
        print(mensagem)
