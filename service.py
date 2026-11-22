from models.cliente import Cliente
from models.categoria import Categoria
from models.produto import Produto
from models.clientedao import ClienteDAO
from models.categoriadao import CategoriaDAO
from models.produtodao import ProdutoDAO


class Service:
    @staticmethod
    def cliente_inserir(nome, email, fone):
        obj = Cliente(1, nome, email, fone)
        ClienteDAO().inserir(obj)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone):
        obj = Cliente(id, nome, email, fone)
        ClienteDAO().atualizar(obj)

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def categoria_inserir(descricao):
        obj = Categoria(1, descricao)
        CategoriaDAO().inserir(obj)

    @staticmethod
    def categoria_listar():
        return CategoriaDAO().listar()

    @staticmethod
    def categoria_listar_id(id):
        return CategoriaDAO().listar_id(id)

    @staticmethod
    def categoria_atualizar(id, descricao):
        obj = Categoria(id, descricao)
        CategoriaDAO().atualizar(obj)

    @staticmethod
    def categoria_excluir(id):
        CategoriaDAO().excluir(id)

    @staticmethod
    def produto_inserir(descricao, preco, estoque, id_categoria):
        obj = Produto(1, descricao, preco, estoque, id_categoria)
        ProdutoDAO().inserir(obj)

    @staticmethod
    def produto_listar():
        return ProdutoDAO().listar()

    @staticmethod
    def produto_listar_id(id):
        return ProdutoDAO().listar_id(id)

    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, id_categoria):
        obj = Produto(id, descricao, preco, estoque, id_categoria)
        ProdutoDAO().atualizar(obj)

    @staticmethod
    def produto_excluir(id):
        ProdutoDAO().excluir(id)

    @classmethod
    def produto_reajustar(cls, percentual):
        porcentagem_do_preco = 100 + percentual
        produtos = ProdutoDAO().listar()
        for produto in produtos:
            preco = produto.preco * (porcentagem_do_preco/100)
            cls.produto_atualizar(produto.id, produto.descricao, preco, produto.estoque, produto.id_categoria)
