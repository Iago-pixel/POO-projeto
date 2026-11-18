import json
from .cliente import Cliente


class ClienteDAO:
    def __init__(self):
        self.__arquivo = "cliente.json"
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

    def atualizar(self, novo_cliente):
        self.__abrir()
        for i, cliente_atual in enumerate(self.__objetos):
            if novo_cliente.id == cliente_atual.id:
                self.__objetos[i] = novo_cliente
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, cliente_atual in enumerate(self.__objetos):
            if cliente_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            clientes_json = json.load(arquivo)
            for obj in clientes_json:
                c = Cliente.from_json(obj)
                self.__objetos.append(c)

    def __salvar(self):
        clientes_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(clientes_json, arquivo, indent = 2)
