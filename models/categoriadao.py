import json
from .categoria import Categoria


class CategoriaDAO:
    def __init__(self):
        self.__arquivo = "categoria.json"
        self.__objetos = []

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

    def atualizar(self, nova_categoria):
        self.__abrir()
        for i, categoria_atual in enumerate(self.__objetos):
            if nova_categoria.id == categoria_atual.id:
                self.__objetos[i] = nova_categoria
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, categoria_atual in enumerate(self.__objetos):
            if categoria_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            categorias_json = json.load(arquivo)
            for obj in categorias_json:
                c = Categoria.from_json(obj)
                self.__objetos.append(c)

    def __salvar(self):
        categorias_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(categorias_json, arquivo, indent = 2)