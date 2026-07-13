# Painel Antirrábico

Painel em Streamlit para monitoramento epidemiológico de notificações antirrábicas.

## O que está neste repositório

- `painel_antirrabico.py` - aplicativo Streamlit
- `Banco_Dados_Antirrabica.xlsx` - base de dados usada pelo painel
- `requirements.txt` - dependências Python
- `.gitignore` - arquivos e pastas ignorados pelo Git

## Pré-requisitos

- Python 3.14 instalado
- Conexão com internet para instalar pacotes
- Conta GitHub para envio do repositório

## Configuração local

1. Abra o PowerShell no diretório do projeto:

```powershell
cd "C:\Users\raque\OneDrive\Área de Trabalho\Antirrabica"
```

2. Crie o ambiente virtual:

```powershell
python -m venv .venv
```

3. Instale as dependências:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

4. Rode o app:

```powershell
.\.venv\Scripts\python.exe -m streamlit run painel_antirrabico.py
```

5. Abra o navegador no link que o Streamlit mostrar, normalmente `http://localhost:8501`.

## Como usar o painel

- Use a barra lateral para escolher a unidade de saúde e o ano.
- Pesquise por nome do paciente ou número da notificação.
- Veja os gráficos e métricas de casos na unidade selecionada.

## Observações importantes

- Mantenha o arquivo `Banco_Dados_Antirrabica.xlsx` na mesma pasta do `painel_antirrabico.py`.
- O arquivo de dados não deve ser renomeado ou movido.
- Se ocorrer erro ao importar `pandas`, execute:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade --force-reinstall pandas
```

## Publicar no GitHub

1. Crie um repositório no GitHub com o nome `Antirrabica`.
2. No terminal do projeto, rode:

```powershell
git remote add origin https://github.com/raquelacioli/Antirrabica.git
git branch -M main
git push -u origin main
```

Se você já tiver um repositório remoto, apenas faça:

```powershell
git push -u origin main
```

## Deploy no Streamlit Cloud

1. Acesse https://streamlit.io/cloud e conecte sua conta GitHub.
2. Escolha o repositório `raquelacioli/Antirrabica`.
3. Configure a branch `main` e verifique se `requirements.txt` está no repositório.
4. Se o app não encontrar o arquivo de dados, mantenha `Banco_Dados_Antirrabica.xlsx` no repositório ou use um caminho externo suportado.

## Dicas úteis

- Se o Streamlit Cloud reclamar de memória ou tamanho de arquivo, você pode mover o Excel para um serviço externo ou simplificar o conjunto de dados.
- Caso queira, posso ajudar você a criar um `README` com imagens, descrições de cada seção do painel e exemplos de uso.