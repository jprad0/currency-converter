import requests
import customtkinter as ctk





coin1 = str(input ("Digite a moeda que deseja a conversão: "))

coin2 = str(input("Digite a moeda para ser usado de referencia na conversão: "))

url_api = f'https://economia.awesomeapi.com.br/json/last/{coin1}-{coin2}'

apiGet = requests.get(url_api).json()

print(apiGet)

apiKey = f"{coin1}-{coin2}"

if apiKey in apiGet:
    dados_moeda = apiGet[apiKey]

    coin1Value = float(dados_moeda['bid'])  # Preço de compra
    coin2Value = float(dados_moeda['ask'])  # Preço de venda
    variacao = float(dados_moeda['varBid'])  # Variação
    maximo = float(dados_moeda['high'])     # Máximo do dia
    minimo = float(dados_moeda['low'])      # Mínimo do dia




    # interface initialization
app = ctk.CTk()
app.geometry("400x600")
app.title("Conversos de moedas")

coinSelect = ctk.CTkEntry(app,width= 500,placeholder_text="Selecione a moeda")
coinSelect.pack(pady=10, padx=10)

app.mainloop()