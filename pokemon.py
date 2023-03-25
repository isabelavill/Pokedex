
def meu_repr(self):
    class_name=self.__class__.__name__
    class_dict = self.__dict__
    class_repr=f'{class_name} ({class_dict})'
    return class_repr
def adiciona_repr(cls):
    cls.__repr__=meu_repr
    return cls

@adiciona_repr
class Pokemon:
    def __init__(self):
        self.lista_pokemons=[]
    
    def inserir_pokemon(self,*pokemon):
        self.lista_pokemons.extend(pokemon)
    
    def listar_todos_pokemons(self):
        for pokemon in self.lista_pokemons:
            print(f'Nome:{pokemon.nome} | Raridade:{pokemon.raridade} | Tipo:{pokemon.tipo}')
        print()

        for i in range(len(self.lista_pokemons)):
            print(self.lista_pokemons[i])
            print()

    # def comparar_raridade(self)

@adiciona_repr
class Cadastro:
    def __init__(self,nome,raridade:int, tipo):
        self.nome=nome
        self.raridade=raridade
        self.tipo=tipo

pokemon=Pokemon()
p1,p2,p3=Cadastro('pikachu',50,'fogo'),Cadastro('chiubaka',-20,'grama'), Cadastro('kika',90,'gelo')
pokemon.inserir_pokemon(p1,p2,p3)
pokemon.listar_todos_pokemons()






