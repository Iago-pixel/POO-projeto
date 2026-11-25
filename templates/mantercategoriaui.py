import streamlit as st
import pandas as pd
import time
from service import Service


class ManterCategoriaUI:
    @staticmethod
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()

    @staticmethod
    def listar():
        categorias = Service.categoria_listar()
        if len(categorias) == 0: st.write("Nenhum categoria cadastrada")
        else:
            list_dic = [obj.to_json() for obj in categorias]
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descrição")
        if st.button("Inserir"):
            Service.categoria_inserir(descricao)
            st.success("Categoria inserida com sucesso")
            time.sleep(2)
            st.rerun()

    @staticmethod
    def atualizar():
        categorias = Service.categoria_listar()
        if len(categorias) == 0: st.write("Nenhum categoria cadastrada")
        else:
            op = st.selectbox("Atualização de Categorias", categorias)
            descricao = st.text_input("Novo nome", op.descricao)
            if st.button("Atualizar"):
                id = op.id
                Service.categoria_atualizar(id, descricao)
                st.success("Categoria atualizada com sucesso")
                time.sleep(2)
                st.rerun()

    @staticmethod
    def excluir():
        categorias = Service.categoria_listar()
        if len(categorias) == 0: st.write("Nenhum categoria cadastrada")
        else:
            op = st.selectbox("Exclusão de Categorias", categorias)
            if st.button("Excluir"):
                id = op.id
                Service.categoria_excluir(id)
                st.success("Categoria excluída com sucesso")
                time.sleep(2)
                st.rerun()
