import streamlit as st
import pandas as pd
import time
from service import Service


class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    @staticmethod
    def listar():
        produtos = Service.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            list_dic = [obj.to_json() for obj in produtos]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição")
        preco = st.number_input("Informe o preço", 0, format="%0.2f")
        estoque = st.number_input("Informe o estoque", 0, step=1,format="%i")
        id_categoria = st.number_input("Informe o id da categoria", 1, step=1,format="%i")
        if st.button("Inserir"):
            Service.produto_inserir(descricao, preco, estoque, id_categoria)
            st.success("Produto inserido com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        produtos = Service.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de Produtos", produtos)
            descricao = st.text_input("Nova descrição", op.descricao)
            preco = st.number_input("Novo preço", 0, value=op.preco, format="%0.2f")
            estoque = st.number_input("Novo estoque", 0, value=op.estoque, step=1,format="%i")
            id_categoria = st.number_input("Novo id de categoria", 1, value=op.id_categoria, step=1,format="%i")
            if st.button("Atualizar"):
                id = op.id
                Service.produto_atualizar(id, descricao, preco, estoque, id_categoria)
                st.success("Produto atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        produtos = Service.produto_listar()
        if len(produtos) == 0: st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de Produtos", produtos)
            if st.button("Excluir"):
                id = op.id
                Service.produto_excluir(id)
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()
