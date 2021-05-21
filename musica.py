class Musica:

    # --------------------------------- CONSTRUTOR ---------------------------------
    def __init__(self, nome, ano, album, id):
        self._nome = nome
        self._ano = ano
        self._album = album
        self._id = id
        self._esquerda = None
        self._direita = None
        self._fator_bal = 0

    # --------------------------------- PROPRIEDADES ---------------------------------

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def album(self):
        return self._album

    @property
    def id(self):
        return self._id

    @property
    def esquerda(self):
        return self._esquerda

    @esquerda.setter
    def esquerda(self, nova_musica):
        self._esquerda = nova_musica

    @property
    def direita(self):
        return self._direita

    @direita.setter
    def direita(self, nova_musica):
        self._direita = nova_musica

    @property
    def fator_bal(self):
        return self._fator_bal

    @fator_bal.setter
    def fator_bal(self, novo_fator):
        self._fator_bal = novo_fator

    # -------------------------------------------------------------------------------
    def __str__(self):
        return f"Nome: {self._nome} \nAno: {self._ano} \nÁlbum: {self._album} \nID: {self._id}\n"




