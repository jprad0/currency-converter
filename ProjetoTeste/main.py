import requests
import customtkinter as ctk
from tkinter import messagebox

def currency_converter_button():
    coin1 = currency1.get()

    coin2 = currency2.get()


    url_api = f'https://economia.awesomeapi.com.br/json/last/{coin1}-{coin2}'

    apiGet = requests.get(url_api).json()

    print(apiGet)

    apiKey = f"{coin1}-{coin2}"

    if apiKey in apiGet:
        dados_moeda = apiGet[apiKey]

        coin1Value = float(dados_moeda['bid'])  # Buy price
        coin2Value = float(dados_moeda['ask'])  # Sell price
        variacao = float(dados_moeda['varBid'])  # Variation
        maximo = float(dados_moeda['high'])     # Max of day
        minimo = float(dados_moeda['low'])      # Min of day



    # interface initialization
app = ctk.CTk()
app.geometry("400x400")
app.title("Currency Converter")

ctk.CTkLabel(app, text="Select Currency to convert").pack(pady=10)

currency1 = ctk.CTkComboBox(
    app,
    values=["USD", "BRL", "EUR", "JPY", "GBP","CAD"]
)
currency1.set("USD") 
currency1.pack(pady=10)

currency2 = ctk.CTkComboBox(
    app,
    values=["USD", "BRL", "EUR", "JPY", "GBP","CAD"]
)
currency2.set("USD") 
currency2.pack(pady=10)

button = ctk.CTkButton(app, text="Result", command=currency_converter_button)
button.pack(pady=10)



app.mainloop()
