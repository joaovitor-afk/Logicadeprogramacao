# classe - Espaço onde vou descrever um objeto 
# metodos - que sao as ações desse objeto 


# nome e vida - atacar
#self - quando quero me referir a algum atributo da class
# construtor - quando quero criar um novo objeto chamo o constrtutor para acessar os atributos
'''class Personagem:
    # construtor
    def __init__(self, nome, vida):
        # emcapsulamento
        self.__nome = nome
        self.__vida = vida

    # deinindo GET
    @property
    def nome(self):
        return self.__nome
    
    # definindo SET
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f'agora esta com {personagem.vida}')


personagem1 = Personagem('Jubirildo', 100)
print(f'Personagem: {personagem1.nome}')
print(f'Vida: {personagem1.vida}')


personagem2 = Personagem('willian', 100)
print(f'Personagem: {personagem2.nome}')
print(f'Vida: {personagem2.vida}')


personagem1.atacar(personagem2)
personagem2.atacar(personagem1)

class Guerreiro:
     def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

     @property
     def nome(self):
        return self.__nome
    
    
     @nome.setter
     def nome(self, novo_nome):
        self.__nome = novo_nome

     @property
     def vida(self):
        return self.__vida
    
     @vida.setter
     def vida(self, vida):
        self.__vida = vida

class Mago:
     def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

        @property
        def nome(self):
            return self.__nome
    
        @nome.setter
        def nome(self, novo_nome):
            self.__nome = novo_nome

        @property
        def vida(self):
            return self.__vida
    
        @vida.setter
        def vida(self, vida):
            self.__vida = vida'''


class Personagem_favorito:
    
    def __init__(self, nome, vida):
        
        self.__nome = nome
        self.__vida = vida

    
    @property
    def nome(self):
        return self.__nome
    
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e tirou 20 pontos de vida.')
        print(f'agora esta com {personagem.vida}')


guerreiro = Personagem_favorito('Jubirildo', 150)
print(f'Personagem: {guerreiro.nome}')
print(f'Vida: {guerreiro.vida}')


mago = Personagem_favorito('willian', 100)
print(f'Personagem: {mago.nome}')
print(f'Vida: {mago.vida}')


guerreiro.atacar(mago)
mago.atacar(guerreiro)
