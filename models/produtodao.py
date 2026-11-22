import json
from .produto import Produto


class ProdutoDAO:
    def __init__(self):
        self.__arquivo = "produto.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
        self.__abrir()
        id = 0
        if len(self.__objetos) != 0:
            id = max(self.__objetos, key = lambda x : x.id).id
        obj.id = id + 1
        self.__objetos.append(obj)
        self.__salvar()

    def listar(self):
        self.__abrir()
        return self.__objetos

    def listar_id(self, id):
        self.__abrir()
        for obj in self.__objetos:
            if obj.id == id:
                return obj
        return None

    def atualizar(self, novo_produto):
        self.__abrir()
        for i, produto_atual in enumerate(self.__objetos):
            if novo_produto.id == produto_atual.id:
                self.__objetos[i] = novo_produto
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, produto_atual in enumerate(self.__objetos):
            if produto_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            produtos_json = json.load(arquivo)
            for obj in produtos_json:
                p = Produto.from_json(obj)
                self.__objetos.append(p)

    def __salvar(self):
        produtos_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(produtos_json, arquivo, indent = 2)