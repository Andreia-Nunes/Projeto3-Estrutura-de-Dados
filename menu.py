from arvoreAVL import *
from musica import *

arvore = ArvoreAVL()
raiz = None

flag = "S"

while flag == "S":
    print('''****************************************

Escolha uma opção:
  1: Inserir música 
  2: Buscar música pelo ID 
  3: Buscar músicas pelo o ano
  4: Listar músicas em ordem alfabética
  5: Altura da árvore
  6: Exibir a árvore
  7: Sair do programa 

****************************************''')

    opcao = int(input("---> "))

    if opcao == 1:
        print()
        nome = str(input('Informe o nome da música -> '))
        ano = int(input('Informe o ano -> '))
        album = str(input('Informe o álbum -> '))
        id = int(input('Informe o ID -> '))
        nova_musica = Musica(nome, ano, album, id)
        raiz = arvore.inserir(raiz, nova_musica)
        print(f"\nMúsica inserida com sucesso!")
        print()

    elif opcao == 2:
        id = int(input('Informe o ID da música que está procurando -> '))
        musica = arvore.busca_id(raiz, id)
        print(f"\n{musica}")

    elif opcao == 3:
        ano = int(input('Informe o ano da música que está procurando-> '))
        arvore.busca_ano(raiz, ano)

    elif opcao == 4:
        arvore.ordenar(raiz)
        print()

    elif opcao == 5:
        print(f"\nAltura: {arvore.altura_arvore(raiz)} nível(is)")
        print()

    elif opcao == 6:
        arvore.exibe_arvore(raiz)
        print()

    elif opcao == 7:
        flag = "N"
        print('Fim do programa.')
        break

    flag = input("Deseja realizar outra operação? (S/N) ").upper()
    print()

else:
    print("Fim do programa")