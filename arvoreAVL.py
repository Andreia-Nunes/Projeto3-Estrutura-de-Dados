class ArvoreAVL:

    # ------------------------ INSERÇÃO DE NOVA MÚSICA ------------------------
    def inserir(self, raiz, nova_musica):

        # Inserindo o novo nó
        if raiz is None:
            return nova_musica

        if nova_musica.id < raiz.id:
            raiz.esquerda = self.inserir(raiz.esquerda, nova_musica)
        else:
            raiz.direita = self.inserir(raiz.direita, nova_musica)

        # Calculando o fator de balanceamento do nó pai após a inserção do novo nó
        altura_esq = self.altura(raiz.esquerda)
        altura_dir = self.altura(raiz.direita)

        raiz.fator_bal = altura_esq - altura_dir

        # Rotacionando o nó em caso de desbalanceamento
        if raiz.fator_bal < -1:
            if raiz.direita.fator_bal > 0:
                raiz.direita = self.rotacao_direita(raiz.direita)
            raiz = self.rotacao_esquerda(raiz)
        elif raiz.fator_bal > 1:
            if raiz.esquerda.fator_bal < 0:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
            raiz = self.rotacao_direita(raiz)

        return raiz

    # -------------------------- CALCULO DA ALTURA --------------------------
    def altura(self, node):
        if node is None:
            return 0

        esquerda = self.altura(node.esquerda)
        direita = self.altura(node.direita)

        altura = max(esquerda, direita) + 1

        return altura

    # ---------------------- ROTAÇÃO SIMPLES À ESQUERDA ----------------------
    def rotacao_esquerda(self, node):
        aux = node.direita
        node.direita = aux.esquerda
        aux.esquerda = node

        return aux

    # ---------------------- ROTAÇÃO SIMPLES À DIREITA ----------------------
    def rotacao_direita(self, node):
        aux = node.esquerda
        node.esquerda = aux.direita
        aux.direita = node

        return aux

    # --------------------- PERCURSO EM ORDEM NA ÁRVORE ---------------------
    def percurso_ordem(self, raiz):
        if raiz is None:
            return

        self.percurso_ordem(raiz.esquerda)
        print(raiz.id)
        self.percurso_ordem(raiz.direita)

    # ------------------------- EXIBIÇÃO DA ÁRVORE --------------------------
    def exibe_arvore(self, raiz, espaco = 0):
        contador = 10

        if raiz is None:
            return

        espaco += contador

        self.exibe_arvore(raiz.direita, espaco)
        print(" " * (espaco - contador - 1), "┌────────┤")

        for i in range(contador, espaco):
            print(end=" ")

        print("├─" + str(raiz.id))
        print(" " * (espaco - contador - 1), "└────────┤")

        self.exibe_arvore(raiz.esquerda, espaco)

    # ---------------------------- BUSCA POR ID -----------------------------
    def busca_id(self, node, id):
        if node is None:
            return None

        musica = self.busca_id(node.esquerda, id)

        if node.id == id:
            musica = node

        if musica is None:
            musica = self.busca_id(node.direita, id)

        return musica

    # --------------------------- BUSCA POR ANO -----------------------------
    def busca_ano(self, raiz, ano):
        musicas = []
        self.cria_vetor_musicas(raiz, ano, musicas)

        for i in range(0, len(musicas)):
            print(f"\n{musicas[i]}")

    def cria_vetor_musicas(self, raiz, ano, musicas):
        if raiz is None:
            return

        self.cria_vetor_musicas(raiz.esquerda, ano, musicas)
        if raiz.ano == ano:
            musicas.append(raiz)
        self.cria_vetor_musicas(raiz.direita, ano, musicas)

    # ----------------------- RETORNA ALTURA DA ÁRVORE -----------------------
    def altura_arvore(self, raiz):
        return self.altura(raiz)

    # ---------------------- ORDENA EM ORDEM ALFABÉTICA ----------------------
    def ordenar(self, raiz):
        msc_ordenada = []
        self.musicas_ordenadas(raiz, msc_ordenada)
        msc_ordenada = sorted(msc_ordenada)

        print("NOME"," " * 45, "ANO", " " * 6, "ÁLBUM", " " * 43, "ID")
        print()
        for y in range(0, len(msc_ordenada)):
            print(msc_ordenada[y])

    def musicas_ordenadas(self, raiz, msc):
        if raiz is None:
            return

        self.musicas_ordenadas(raiz.esquerda, msc)
        msc.append(f"{raiz.nome:50} {str(raiz.ano):10} {raiz.album:50} {raiz.id}")
        self.musicas_ordenadas(raiz.direita, msc)