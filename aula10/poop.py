class Personagem:
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




class Guerreiro(Personagem):
     def __init__(self, nome,  vida, escudo=False):
         super().__init__(nome, vida)
         self.__escudo = escudo

     @property
     def escudo(self):
         return self.__escudo
     
     @escudo.setter
     def escudo(self, escudo):
         self.__ = escudo


# sobrescrevendo o metodo da class pai
     def atacar(self, personagem):
         personagem.vida -= 40 
         print(f'{self.nome} atacou {personagem.nome} e tirou 40 pontos de vida.')
         print(f'agora esta com {personagem.vida}')



     def protecao(self):
         self.__vida += 10





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

class Mago(Personagem):
     def __init__(self, nome,  vida):
         super().__init__(nome, vida)

     def curar(self, personagem):
        personagem.vida += 15 
        print(f'{self.nome} usou o poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')

gandof = Mago('Gandof', 100)
aragonr = Guerreiro('Aragorn', 100)
frodo = Guerreiro('Frodo', 100)

gandof.atacar(frodo)




     