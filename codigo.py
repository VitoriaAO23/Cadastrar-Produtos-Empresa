# Passa 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui - pandas

import pyautogui
import time

pyautogui.PAUSE = 1

#pyautogui.pixelMatchesColor -> clicar em algum lugar da tela
#pyautogui.write -> escrever um texto
#pyautogui.press -> pressionar 1 tecla do teclado
# pyautogui.hotkey('ctrl', 'v')

# abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('Enter')

# entrar no site
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('Enter')

# dar uma pausa
time.sleep(2)

# Passo 2: Fazer login
pyautogui.click(x=671, y=466)
pyautogui.write('vitoriaalves71593@gmail.com')

pyautogui.press('Tab')
pyautogui.write('843084')

pyautogui.click(x=948, y=667)
time.sleep(3)

# Passo 3: Importar a base de dados
import pandas 
tabela = pandas.read_csv('produtos.csv')
print(tabela)

# Passo 4: Cadastrar 1 produto
#para cada linha da minha tabela
for linha in tabela.index:
    # clicar no 1 campo
    pyautogui.click(x=616, y=324)
    # codigo do produto 
    codigo = tabela.loc[linha, 'codigo']
    pyautogui.write(codigo)
    pyautogui.press('Tab')

    # marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(marca)
    pyautogui.press('Tab')

    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(tipo)
    pyautogui.press('Tab')

    #categoria

    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)
    pyautogui.press('Tab')

    #preço
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)
    pyautogui.press('Tab')

    #custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)
    pyautogui.press('Tab')

    #obs
    obs = tabela.loc[linha, 'obs']
    #se não tiver vazia 
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press('Tab')

    #enviar
    pyautogui.press('Enter')
    pyautogui.scroll(5000)


# Passo 5: Repetir o processo de cadastro até acabar