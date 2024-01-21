import streamlit as st
import pandas as pd
import datetime
import os
import base64

class AnaliseAtividades:
    def __init__(self, user_id):
        self.user_id = user_id
        self.arquivo_dados = f'analise_atividades_{self.user_id}.xlsx'
        self.iniciar_arquivo_excel()
        self.iniciar_sessao()

    def iniciar_arquivo_excel(self):
        if not os.path.exists(self.arquivo_dados):
            df = pd.DataFrame(columns=['Atividade', 'Início', 'Fim', 'Quantidade'])
            df.to_excel(self.arquivo_dados, index=False)

    def iniciar_sessao(self):
        if 'analise' not in st.session_state:
            st.session_state.analise = {
                'df': pd.DataFrame(columns=['Atividade', 'Início', 'Fim', 'Quantidade'])
            }

    def iniciar_analise(self):
        st.write("Iniciando análise...")

    def selecionar_atividades(self):
        opcoes_atividades = [
            "Andando sem ferramenta", "Ao Celular / Fumando", "Aguardando Almoxarifado",
            "À disposição", "Necessidades Pessoais (Água/Banheiro)", "Operando",
            "Auxiliando", "Ajustando Ferramenta ou Equipamento", "Deslocando com ferramenta em mãos",
            "Em prontidão", "Conversando com Encarregado/Operários (Informações Técnicas)"
        ]

        atividades_quantidades = {}

        for atividade in opcoes_atividades:
            quantidade = st.number_input(f"Quantidade de pessoas fazendo '{atividade}':", min_value=0, step=1, value=0)
            if quantidade > 0:
                atividades_quantidades[atividade] = quantidade

        return atividades_quantidades

    def registrar_atividades_quantidades(self, atividades_quantidades):
        df = st.session_state.analise['df']

        for atividade, quantidade in atividades_quantidades.items():
            novo_registro = {
                'Atividade': atividade,
                'Início': datetime.datetime.now().strftime("%H:%M:%S"),
                'Fim': '',
                'Quantidade': quantidade
            }

            df = pd.concat([df, pd.DataFrame([novo_registro])], ignore_index=True)
            st.session_state.analise['df'] = df

            st.success(f"Atividade '{atividade}' registrada com {quantidade} pessoa(s).")

    def gerar_relatorio_excel(self):
        st.write(f"Dados salvos em '{self.arquivo_dados}'")

        df = st.session_state.analise['df']

        if not df.empty:
            df.to_excel(self.arquivo_dados, index=False)
            st.markdown(get_binary_file_downloader_html(self.arquivo_dados, 'Relatório Atividades'), unsafe_allow_html=True)
        else:
            st.warning("Nenhum dado disponível para exportação.")

# Função auxiliar para criar botão de download
def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">{file_label}</a>'
    return href
