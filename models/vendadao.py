import json
from .venda import Venda


class VendaDAO:
    def __init__(self):
        self.__arquivo = "venda.json"
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

    def atualizar(self, nova_venda):
        self.__abrir()
        for i, venda_atual in enumerate(self.__objetos):
            if nova_venda.id == venda_atual.id:
                self.__objetos[i] = nova_venda
                self.__salvar()
                return

    def excluir(self, id):
        self.__abrir()
        for i, venda_atual in enumerate(self.__objetos):
            if venda_atual.id == id:
                self.__objetos.pop(i)
                self.__salvar()
                return

    def __abrir(self):
        self.__objetos = []
        with open(self.__arquivo, mode="r") as arquivo:
            vendas_json = json.load(arquivo)
            for obj in vendas_json:
                v = Venda.from_json(obj)
                self.__objetos.append(v)

    def __salvar(self):
        vendas_json = [obj.to_json() for obj in self.__objetos]
        with open(self.__arquivo, mode="w") as arquivo:
            json.dump(vendas_json, arquivo, indent = 2)