# 📌AI SQL Query Generator

Este projeto é um **gerador de queries SQL** baseado em IA, que utiliza o modelo **Google Gemini** para converter descrições em linguagem natural em consultas SQL. O aplicativo é construído com **Streamlit** e permite visualizar e baixar as queries geradas, incluindo uma explicação detalhada sobre a sintaxe SQL utilizada.

---

## 🚀 **Instalação e Configuração**

### 📌 **1. Instalar o Anaconda**
Baixe e instale o **Anaconda Python** de acordo com seu sistema operacional:

- [Windows](https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Windows-x86_64.exe)
- [MacOS Apple Silicon](https://repo.anaconda.com/archive/Anaconda3-2024.10-1-MacOSX-arm64.pkg)
- [MacOS Intel](https://repo.anaconda.com/archive/Anaconda3-2024.10-1-MacOSX-x86_64.pkg)
- [Linux](https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh)

### 📌 **2. Criar um ambiente virtual**
Abra o terminal ou prompt de comando e execute:
```bash
conda create --name sqlaigenerator python=3.12
```

### 📌 **3. Ativar o ambiente virtual**
```bash
conda activate sqlaigenerator
```
Ou, dependendo da versão do Conda:
```bash
source activate sqlaigenerator
```

### 📌 **4. Instalar dependências**
```bash
conda install pip
pip install -r requirements.txt
```

### 📌 **5. Executar a aplicação**
```bash
streamlit run query_ai_app.py
```
Acesse o link gerado no terminal para abrir a interface no navegador.

---

## 🛠️ **Como Usar**
1. **Digite uma descrição** da consulta SQL que deseja gerar.
2. Clique no botão **"Gerar Query SQL"**.
3. A IA gerará:
   - A consulta SQL correspondente.
   - Um exemplo da **saída esperada**.
   - Uma **explicação** detalhada sobre a query.
4. Os resultados serão exibidos em abas.
5. **Baixe a consulta** em formato `.sql`, se desejar.

---

## 📌 **Exemplos de Descrição para Geração de Queries**

- **Crie uma query SQL para calcular a média de uma coluna com base em duas outras colunas de uma tabela.**
- **Crie uma query SQL utilizando CTE (Common Table Expressions) e funções Window. O objetivo da query é calcular a média móvel de vendas por mês.**

---

## 🛑 **Como Desativar e Remover o Ambiente Virtual (Opcional)**
Para **desativar** o ambiente:
```bash
conda deactivate
```
Para **removê-lo** completamente:
```bash
conda remove --name sqlaigenerator --all
```

---

## 📝 **Sobre**
Este projeto foi desenvolvido para gestores que não têm familiaridade com SQL e precisam realizar análises na base **inteligência de mercado e análise de dados**.

---

**🔗 Autor:** Wanderson

Se gostou do projeto, dê uma estrela ⭐ no repositório!

