import streamlit as st

def informacoes():
    st.title("Informações")
    st.write("Bem-vindo à página de informações. Aqui você encontrará detalhes sobre os aplicativos.")

    st.header("Sobre o App 1:")
    st.write(
        "O AtividadeTracker é uma aplicação projetada para simplificar o registro "
        "de atividades individuais de membros de uma equipe. Com essa ferramenta intuitiva, "
        "os usuários podem facilmente monitorar e documentar as atividades realizadas durante um determinado período.\n\n"
        "Principais recursos do AtividadeTracker:\n"
        "- Registro Individual: Permite que cada membro da equipe registre suas atividades de maneira personalizada.\n"
        "- Controle de Tempo: Registra automaticamente o início e o fim de cada atividade, calculando a duração total.\n"
        "Seja para equipes de construção civil, escritórios ou outros setores, "
        "o AtividadeTracker simplifica o processo de rastreamento de atividades, "
        "promovendo uma gestão mais eficiente do tempo e recursos."
    )

    st.header("Sobre o App 2:")
    st.write(
        "O ConstruData Insights é uma aplicação especializada na análise e visualização da distribuição "
        "de pessoas em diferentes atividades no setor da construção civil. Esta ferramenta foi desenvolvida "
        "para oferecer insights valiosos sobre a produtividade da equipe e otimizar a alocação de recursos.\n\n"
        "Principais recursos do ConstruData Insights:\n"
        "- Análise de Atividades: Permite aos usuários selecionar e quantificar diversas atividades com base em critérios específicos.\n"
        "- Tempo Real: Oferece informações em tempo real sobre a distribuição de equipe em diferentes tarefas.\n"
        "Seja para gestores de projeto, supervisores ou tomadores de decisão, "
        "o ConstruData Insights é uma ferramenta valiosa para melhorar a eficiência operacional e a produtividade "
        "na indústria da construção civil."
    )
