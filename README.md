# Painel Antirrábico

Painel em Streamlit para monitoramento epidemiológico de notificações antirrábicas.

## O que está neste repositório

- `painel_antirrabico.py` - aplicativo Streamlit
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

4. Crie um arquivo `.env` na raiz do projeto com suas credenciais:

```env
PANEL_USER=vigilanciaepidemiologicadsvii@gmail.com
PANEL_PASS=antirrabica
```

5. Rode o app:

```powershell
.\.venv\Scripts\python.exe -m streamlit run painel_antirrabico.py
```

6. Abra o navegador no link que o Streamlit mostrar, normalmente `http://localhost:8501`.

## Como usar o painel

- Faça upload do arquivo Excel semanal na barra lateral.
- Use a barra lateral para escolher a unidade de saúde e o ano.
- Pesquise por nome do paciente ou número da notificação.
- Veja os gráficos e métricas de casos na unidade selecionada.

## Configuração de credenciais

- O app utiliza variáveis de ambiente definidas em um arquivo `.env`.
- Não inclua o `.env` no repositório; ele já está listado em `.gitignore`.

## Observações importantes

- O app exige upload do arquivo `.xlsx` toda vez que for aberto.
- Não é mais necessário manter `Banco_Dados_Antirrabica.xlsx` na pasta do projeto.
- Se ocorrer erro ao importar `pandas`, execute:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade --force-reinstall pandas
```

## Publicar no GitHub

4. Crie um repositório no GitHub com o nome `painel-antirrabico`.
5. No terminal do projeto, rode:

```powershell
git remote add origin https://github.com/raquelacioli/painel-antirrabico.git
git branch -M main
git push -u origin main
```

Se você já tiver um repositório remoto, apenas faça:

```powershell
git push -u origin main
```

## Deploy no Streamlit Cloud

1. Acesse https://streamlit.io/cloud e conecte sua conta GitHub.
2. Escolha o repositório `raquelacioli/painel-antirrabico`.
3. Configure a branch `main` e verifique se `requirements.txt` está no repositório.
4. O app exige upload do arquivo Excel semanal; não é necessário manter `Banco_Dados_Antirrabica.xlsx` no repositório.

## Dicas úteis

- Se o Streamlit Cloud reclamar de memória ou tamanho de arquivo, você pode mover o Excel para um serviço externo ou simplificar o conjunto de dados.
- Caso queira, posso ajudar você a criar um `README` com imagens, descrições de cada seção do painel e exemplos de uso.