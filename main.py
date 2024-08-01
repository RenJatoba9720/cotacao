from tkinter import *
import requests

def limpar():
    texto_resposta["text"] = ""
def pegar_cotacoes():
    requisica = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    rqs = requisica.json()

    dolarAtual = rqs['USDBRL']['bid']
    euroAtual = rqs['EURBRL']['bid']
    btcAtual = rqs['BTCBRL']['bid']

    texto = f'''
    DOLAR: {dolarAtual}
    EURO: {euroAtual}
    BTC: {btcAtual}'''

    #print(texto)
    texto_resposta["text"] = texto

wd = Tk()
wd.geometry("400x400")
wd.title("Cotação Atual de Moedas")

texto = Label(wd, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(wd, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

botaoLimpar = Button(wd, text="Limpar cotações", command=limpar)
botaoLimpar.grid(column=1, row=1, padx=10, pady=10)

texto_resposta = Label(wd, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

wd.mainloop()