import streamlit as st
from app1 import app1
from app2 import app2
from informacoes import informacoes
from app3 import app3

def main():
    st.sidebar.title("Menu de Navegação")
    app_choice = st.sidebar.radio("Selecione uma opção:", ("AtividadeTracker", "Data Insights", "Informações", "Gráficos"))

    if app_choice == "AtividadeTracker":
        app1()

    elif app_choice == "Data Insights":
        app2()

    elif app_choice == "Informações":
        informacoes()

    elif app_choice == "Gráficos":
        app3()

if __name__ == "__main__":
    main()
