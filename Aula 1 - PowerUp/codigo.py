# Passos para resolver o problema

import pyautogui
import time  # Importar a biblioteca time que permite fazer pausas no código

# Por padrao, o pyautogui tem uma pausa de 0.1 segundos entre cada ação
# Pode usar quando tiver captcha, para não ser bloqueado pelo site
pyautogui.PAUSE = 0.5  # Definir uma pausa entre as ações do pyautogui

# Criar variavel
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"  # Link do sistema da empresa

# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # Abrir uma nova aba no navegador

pyautogui.press("win")  # Simular a tecla "Win" para abrir o menu iniciar

pyautogui.write("opera")  # Digitar "opera" para abrir o navegador

pyautogui.press("enter")  # Apertar a tecla "Enter" para abrir o navegador

pyautogui.write(link)  # Digitar o link

pyautogui.press("enter")  # Apertar a tecla "Enter" para acessar o link

# Fazer uma pausa de 3 segundos para o site carregar
time.sleep(3)  # Pausa de 3 segundos para o site carregar

    # pyautogui.write -> escrever um texto
    # pyautogui.press -> apertar 1 tecla
    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.hotkey -> combinação de teclas

# Passo 2: Fazer login
# Clicar no campo de login
pyautogui.click(674, 447)  # Clicar no campo de login (coordenadas x=674, y=447)

pyautogui.write("pythonimpressionador@gmail.com")  # Digitar o login

pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de senha

pyautogui.write("sua senha muito muito muito dificilima")  # Digitar a senha

pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o botão de login

pyautogui.press("enter")  # Apertar a tecla "Enter" para fazer o login

time.sleep(4)  # Pausa de 4 segundos para o site carregar após o login

# Passo 3:  Abrir a base de dados (importar o arquivo excel)
# Instalar o pandas que trabalha com a base de dados
    # pip install pandas

import pandas  # Importar a biblioteca pandas para trabalhar com a base de dados

tabela = pandas.read_csv("produtos.csv")  # Ler o arquivo csv

# tabela = pandas.read_excel("produtos.xlsx", sheet_name="Custos")  # Ler o arquivo excel e selecionar a aba "Custos"

print(tabela)  # Imprimir a tabela


for linha in tabela.index:  # Para cada linha (ou nome que quiser) da tabela, executar o código abaixo que esta dentro do for, com identação (espaços no inicio da linha)
# Passo 4:  Cadastrar um produto
    pyautogui.click(682, 301)  # Clicar no campo de login (coordenadas x=682, y=301)

# Codigo

    # pyautogui.write("Código")  # Digitar o nome do produto da primeira linha da tabela

    # loc = localizar o campo de código do produto, clicar nele e digitar o código do produto da primeira linha da tabela, colocando entre colchetes
    codigo = str(tabela.loc[linha, "codigo"])  # Pegar o código da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv). STR = Transformar o numero em string

    pyautogui.write(codigo)

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de marca

# Marca

# pyautogui.write("Marca") # Digitar a marca da primeira linha da tabela

    marca = str(tabela.loc[linha, "marca"])  # Pegar a marca da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv)

    pyautogui.write(marca)

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de tipo

# Tipo

# pyautogui.write("Tipo")  # Digitar o tipo da primeira linha da tabela

    tipo = str(tabela.loc[linha, "tipo"])  # Pegar o tipo da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv)

    pyautogui.write(tipo)

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de categoria

# Categoria

# pyautogui.write("Categoria")  # Digitar a categoria da primeira linha da tabela

    categoria = str(tabela.loc[linha, "categoria"])  # Pegar a categoria da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv)

    pyautogui.write(categoria)

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de preço

# Preço

# pyautogui.write("Preço")  # Digitar o preço da primeira linha da tabela

    preco = str(tabela.loc[linha, "preco_unitario"])  # Pegar o preço da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv)

    pyautogui.write(preco)

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de custo

# Custo

# pyautogui.write("Custo")  # Digitar o custo da primeira linha da tabela

    custo = str(tabela.loc[linha, "custo"])  # Pegar o custo da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv)

    pyautogui.write(custo)

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o campo de obs

# Obs

# pyautogui.write("Obs")  # Digitar a obs da primeira linha da tabela

    obs = str(tabela.loc[linha, "obs"])  # Pegar a obs da primeira linha da tabela (nome igual ao nome da coluna do arquivo excel ou csv)

    if obs != "nan":  # Se a obs não for NaN, digitar a obs da primeira linha da tabela
        pyautogui.write(obs)  # Digitar a obs da primeira linha da tabela

    pyautogui.press("tab")  # Apertar a tecla "Tab" para ir para o botão de enviar

    pyautogui.press("enter")  # Apertar a tecla "Enter" para enviar o formulário

    pyautogui.scroll(5000)  # Voltar para o topo da página para cadastrar o próximo produto (pode colocar um valor muito alto). Positivo para cima, negativo para baixo

# Passo 5:  Repetir o passo 4 até acabar a lista

