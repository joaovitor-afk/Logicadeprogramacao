import os
import json
from time import sleep as delay

lista = []

with open("Aula09/livros.json", "r", encoding="utf-8") as f:
                   livro_novo = dict(json.load(f))

def clear(): delay(1); return print('\033[H\033[J')

limpar = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
       print(40*'=','BEM VINDO A BIBLIOTECA', 40*'=')
       print('1 - Cadastrar novo livro.')
       print('2 - listar livros da biblioteca.')
       print('3 - atualizar algum livro da biblioteca.')
       print('4 - excluir livro da biblioteca.')
       opcao = input('Informe a opção desejada: ')
       limpar()
       match opcao:
           case '1':
               livro_novo['nome'].append(input('Informe o nome do livro: ').strip().title())
               livro_novo['idade_indicativa'].append(input('Informe a idade indicativa do livro: '))
               livro_novo['genero'].append(input('Digite o genero do livro: ').strip().lower())
               
               limpar()

               print('livro cadastradado com sucesso! ')

               

               with open("Aula09/livros.json", "w", encoding="utf-8") as f:
                   json.dump(livro_novo, f, ensure_ascii=False, indent=4)

               continue
           case "2":
                if livro_novo:
                    print(f"nome: {livro_novo["nome"]}")
                    print(f"idade: {livro_novo["idade_indicativa"]}")
                    print(f"genero: {livro_novo["genero"]}")
                else:
                       print('nenhum livro encontrado na biblioteca!')
           case '3':
                 nome = input('Informe o nome do livro que deseja atualizar: ').strip().lower()
                 with open("aula09/livros.json", 'r', encoding='utf-8') as f:
                     cadastro = json.load(f)
                
                 encontrado = False
                 for livro in cadastro: 
                     if livro['nome'].lower() == nome:
                         print('Dados atuais:', livro)
                         
                         idade_indicativa = input('Nova idade indicativa (permaneça em branco para não alterar): ').strip()
                         genero = input('Novo gênero (permaneça em branco para não alterar): ').strip()
                
                         if idade_indicativa:
                             livro['idade_indicativa'] = idade_indicativa
                         if genero:
                             livro['genero'] = genero
                
                         encontrado = True
                         break
                        
                 if encontrado:
                     with open('aula09/livros.json', 'w', encoding='utf-8') as f:
                         json.dump(cadastro, f, ensure_ascii=False, indent=4)
                     limpar()
                     print('Livro atualizado com sucesso!')
                 else:
                     print('Livro não encontrado!')

           case '4':
                print(f"nome: {livro_novo["nome"]}")
                print(f"idade: {livro_novo["idade_indicativa"]}")
                print(f"genero: {livro_novo["genero"]}")

                nome = input('digite o nome do livro que deseja deletear: ')
                
                i = livro_novo["nome"].index(nome)

                del livro_novo["nome"][i]
                del livro_novo["idade_indicativa"][i]
                del livro_novo["genero"][i]

                with open('aula09/livros.json', 'w', encoding='utf-8') as f:
                        json.dump(livro_novo, f, ensure_ascii=False, indent=4)

                print('Voce deleteou o livro com sucesso!')
