class Pokemon:
    def __init__(self, nome: str, tipo: str, raridade: int, codigo:int):
        self.__nome=nome
        self.__tipo=tipo
        self.__codigo=codigo
        self.__raridade=raridade

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome=nome


    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self,tipo):
        self.__tipo=tipo

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,codigo):
        self.__codigo=codigo

    @property
    def raridade(self):
        return self.__raridade
    @raridade.setter
    def raridade(self,raridade):
        self.__raridade=raridade