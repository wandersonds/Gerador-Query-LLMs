# SQL Para Análise de Dados e Data Science
# Projeto Query Generator Text-to-SQL

# Imports
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Carrega o arquivo de variáveis de ambiente
load_dotenv()   

# Carrega a variável de ambiente da API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configura a chamada ao modelo via API
genai.configure(api_key=GOOGLE_API_KEY)

# Cria instância do modelo de IA
modelo_ai_dsa = genai.GenerativeModel('gemini-2.0-flash')

# Função para gerar a resposta do modelo de IA
def dsa_gera_resposta_modelo(prompt):

    # Tenta executar o bloco abaixo e capturar possíveis erros
    try:

        # Envia o prompt ao modelo de IA para gerar conteúdo
        response = modelo_ai_dsa.generate_content(prompt)

        # Retorna o texto da resposta, removendo espaços e blocos markdown com ```sql
        return response.text.strip().lstrip("```sql").rstrip("```")

    # Captura qualquer exceção que ocorrer durante a geração do conteúdo
    except Exception as e:

        # Exibe uma mensagem de erro ao usuário com detalhes da exceção capturada
        st.error(f"Erro ao gerar resposta: {str(e)}")

        # Retorna None indicando que houve falha na geração da resposta
        return None

# Função para download do resultado do modelo
def dsa_download_resultado(sql_query, e_output, explicacao):
    
    # Formata o conteúdo a ser baixado, incluindo consulta SQL, saída esperada e explicação
    conteudo = f"Consulta SQL:\n{sql_query}\n\nSaída Esperada:\n{e_output}\n\nExplicação:\n{explicacao}"
    
    # Cria e exibe um botão que permite ao usuário baixar o conteúdo formatado como arquivo .sql
    st.download_button("Baixar Resultado", conteudo, file_name = "dsa_resultado_query.sql", mime = "text/plain")

# Função principal
def main():

    # Configuração da página
    st.set_page_config(page_title="Gerador de Query IM", page_icon=":100:", layout="wide")

    # Sidebar com instruções
    with st.sidebar:
        st.header("Agente de Consulta IM")
        st.header("Instruções")
        st.markdown("""
        - Digite uma descrição clara da query SQL desejada.
        - Clique no botão **"Gerar Query SQL"**.
        - A IA vai gerar:
          - O template da consulta SQL.
          - Um exemplo da saída esperada.
          - Uma explicação da sintaxe da query.
        - Quanto melhor o contexto, melhor a saída.
        - Se você não souber SQL e não souber o que deseja, a IA não terá muita utilidade!
        - IA comete erros. SEMPRE use seu conhecimento para verificar os resultados.
        """)

        if st.button("Suporte"):
            st.write("Dúvidas? Envie um e-mail para: email@suporte.com.br")

    # Título principal
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>IM SQL Query Generator</h1>
            <h2>Text-to-SQL</h2>
            <hr style="margin:20px 0;">
            <h4>Eu Sou Um Assistente de IA Customizado e Vou Gerar Templates de Queries SQL Para Você!</h3>
            <h5>Vou Gerar Também Explicações Sobre a Sintaxe e a Opção de Download do Arquivo .sql.</h4>
            <hr style="margin:20px 0;">
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Input do usuário
    text_input = st.text_area("Descreva, em português, a query SQL que deseja:")

    # Botão de envio
    submit = st.button(label='Gerar Query SQL')

    if submit:
        if len(text_input.strip()) < 10:
            st.warning("Por favor, forneça uma descrição mais detalhada.")
            return

        # Processamento com spinner
        with st.spinner("A IA está gerando o resultado. Aguarde..."):

            # Gera a resposta do modelo
            sql_query = dsa_gera_resposta_modelo(f"Crie de forma clara, objetiva e profissional, uma consulta SQL baseada neste texto: {text_input}")

            # Se a primeira resposta foi gerada, seguimos usando IA para gerar as demais saídas 
            if sql_query:

                # Exemplo de saída da query
                e_output = dsa_gera_resposta_modelo(f"Mostre um exemplo da saída esperada para: {sql_query}")

                # Explicação
                explicacao = dsa_gera_resposta_modelo(f"Avalie e detalhe a explicação da sintaxe desta consulta SQL, descrevendo cada cláusula e função utilizada: {sql_query}")

                # Criar abas para exibir os resultados
                tab1, tab2, tab3 = st.tabs(["Consulta SQL", "Saída Esperada", "Explicação"])

                with tab1:
                    st.code(sql_query, language="sql")

                with tab2:
                    st.markdown(e_output)

                with tab3:
                    st.markdown(explicacao)

                # Opção de download
                dsa_download_resultado(sql_query, e_output, explicacao)

# Executa a aplicação
main()





