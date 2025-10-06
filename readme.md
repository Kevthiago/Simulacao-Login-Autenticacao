# Simulação de Sistema de Login com Análise Estatística e IA

Este projeto realiza uma simulação estatística de um sistema de autenticação de login para avaliar seu desempenho. O objetivo é estimar métricas cruciais como o tempo médio de autenticação, a taxa de sucesso e o throughput (vazão) do sistema.

Ao final da simulação, o script gera automaticamente um relatório técnico completo em formato `.docx`, utilizando a IA da Groq para redigir a análise textual e interpretar os gráficos gerados.

## 📋 Índice

- [Visão Geral do Projeto](#-visão-geral-do-projeto)
- [Funcionalidades](#-funcionalidades)
- [Metodologia da Simulação](#-metodologia-da-simulação)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Como Executar](#-como-executar)
- [Estrutura do Código](#-estrutura-do-código)
- [Saídas Geradas](#-saídas-geradas)
- [Autor](#-autor)

## 🎯 Visão Geral do Projeto

O script simula o comportamento de múltiplos usuários tentando acessar um sistema. Ele utiliza modelos estatísticos para gerar eventos de chegada de usuários e tempos de autenticação, tornando a simulação mais próxima da realidade. Com base nos dados gerados, são calculadas métricas de desempenho e violações de SLA (Acordo de Nível de Serviço).

O grande diferencial deste projeto é a automação da análise e da geração de relatórios. A IA da Groq é utilizada para interpretar os resultados numéricos e visuais, produzindo um documento profissional pronto para ser compartilhado com equipes técnicas e gestores.

## ✨ Funcionalidades

- **Simulação Estatística:** Utiliza distribuições de Poisson para a chegada de usuários e Exponencial para o tempo de autenticação.
- **Cálculo de Métricas:** Calcula automaticamente métricas de desempenho como:
  - Throughput (requisições por segundo)
  - Taxa de Sucesso de Login
  - Tempo Médio de Autenticação
  - Número de Violações de SLA
- **Geração de Gráficos:** Cria 5 visualizações de dados para facilitar a análise:
  1.  Distribuição do Tempo de Autenticação (Histograma)
  2.  Análise Estatística do Tempo de Autenticação (Boxplot)
  3.  Comparativo de Sucessos vs. Falhas (Gráfico de Barras)
  4.  Variação do Throughput ao Longo do Tempo (Gráfico de Linha)
  5.  Contagem de Violações de SLA (Gráfico de Barras)
- **Relatório Automatizado com IA:** Gera um relatório completo em `.docx`, contendo:
  - Resumo executivo e análise das métricas (texto gerado pela IA).
  - Todos os gráficos gerados.
  - Análise interpretativa dos gráficos (texto gerado pela IA).

## 🎲 Metodologia da Simulação

1.  **Parâmetros Iniciais:** O script é configurado com parâmetros base, como o número de simulações, tempo médio de autenticação esperado, taxa de sucesso e a taxa de chegada de usuários (`lambda`).
2.  **Geração de Eventos:** Em um loop, o script simula a chegada de usuários a cada minuto, usando a **distribuição de Poisson**. Para cada usuário, o tempo de autenticação é gerado a partir de uma **distribuição Exponencial**.
3.  **Coleta de Dados:** Cada evento (tentativa de login) é armazenado com seu tempo de chegada, tempo de autenticação e resultado (sucesso ou falha).
4.  **Análise e Visualização:** Após a simulação, os dados são processados com o `Pandas` para calcular as métricas. O `Matplotlib` e o `Seaborn` são usados para criar os gráficos.
5.  **Geração de Relatório:** As métricas e um prompt estruturado são enviados para a API da Groq, que gera o texto analítico. Em seguida, a biblioteca `python-docx` monta o documento final, unindo o texto da IA com as imagens dos gráficos.

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas Principais:**
  - `numpy`: Para cálculos numéricos e geração de dados estatísticos.
  - `pandas`: Para manipulação e análise dos dados da simulação.
  - `matplotlib` & `seaborn`: Para a criação dos gráficos.
  - `python-docx`: Para a criação e manipulação do arquivo `.docx`.
  - `groq`: Para interagir com a API de geração de texto da Groq (através do conector `groq_Connect`).

## ⚙️ Pré-requisitos

Antes de executar, você precisa ter o Python 3 instalado e as seguintes bibliotecas. Você pode instalá-las com pip:

```bash
pip install numpy pandas matplotlib seaborn python-docx groq
```

Além disso, você precisará de um arquivo auxiliar `groq_Connect.py` que contenha a função `gerar_texto_groq` para se conectar à API da Groq. Este arquivo deve ser configurado com sua chave de API.

## 🚀 Como Executar

1.  **Clone o repositório** ou salve o arquivo do projeto em um diretório local.
2.  **Crie o arquivo `groq_Connect.py`** no mesmo diretório e configure sua chave de API da Groq.
3.  **Instale as dependências** conforme listado na seção de pré-requisitos.
4.  **Execute o script** principal via terminal:
    ```bash
    python nome_do_seu_script.py
    ```
5.  Aguarde a execução. Ao final, você verá a seguinte mensagem no console:
    ```
    ✅ Relatório completo gerado com sucesso: relatorio_simulacao_login_completo.docx
    ```

## 📂 Estrutura do Código

O script é organizado nas seguintes seções:

- **Configuração Inicial:** Importação de bibliotecas e configuração de encoding.
- **Parâmetros da Simulação:** Definição de todas as variáveis que controlam a simulação (ex: `num_simulacoes`, `lambda_users`).
- **Geração da Simulação:** Loop principal que cria os eventos de login.
- **Cálculo das Métricas:** Processamento dos dados simulados para extrair os resultados.
- **Relatório Principal (IA):** Formulação do prompt e chamada à API da Groq para gerar o texto do relatório.
- **Criação do Documento DOCX:** Inicialização do documento e inserção do texto gerado pela IA.
- **Geração e Inserção dos Gráficos:** Criação, salvamento e inserção dos 5 gráficos no documento.
- **Análise dos Gráficos (IA):** Segunda chamada à IA para interpretar as visualizações.
- **Finalização:** Salvamento do documento `.docx`.

## 📄 Saídas Geradas

Ao executar o script, os seguintes arquivos serão criados no diretório:

- `relatorio_simulacao_login_completo.docx`: O relatório final contendo toda a análise textual e visual.
- `grafico_tempo_autenticacao.png`
- `grafico_boxplot_tempo_autenticacao.png`
- `grafico_sucessos_falhas.png`
- `grafico_throughput.png`
- `grafico_sla_violacoes.png`

## 👨‍💻 Autor

- **Kevin Thiago dos Santos** - *Estudante de Ciência da Computação*
