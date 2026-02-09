import requests
import customtkinter as ctk
from tkinter import messagebox



def currency_converter_button():
    coin1 = currency1.get()

    coin2 = currency2.get()

    try:
        url_api = f'https://economia.awesomeapi.com.br/json/last/{coin1}-{coin2}'

         
        response = requests.get(url_api)
        response.raise_for_status()  
        
        apiGet = response.json()
        print("API Response:", apiGet)  

        
        apiKey = f"{coin1}{coin2}"
        print(f"Searching for: {apiKey}")  
       
        if apiKey in apiGet:
            currency_data = apiGet[apiKey]

            coin2Value = float(currency_data['ask'])  # Sell price
            variation = float(currency_data['varBid'])  # Variation
            max = float(currency_data['high'])     # Max of day
            min = float(currency_data['low'])      # Min of day
            coin1Value = float(currency_data['bid'])  # Buy price

           
            message_text = (f"Buy Price: {coin1Value:.4f}\n"
                           f"Sell price: {coin2Value:.4f}\n"
                           f"Variation: {variation}\n"
                           f"Max of day: {max:.4f}\n"
                           f"Min of day: {min:.4f}")
            
           
            app.update()
            
            messagebox.showinfo(
                title="Currency Converter result", 
                message=message_text,
                parent=app
            )
        else:
            messagebox.showerror(
                "Error",
                f"Currency not found!\nTry search: {apiKey}\nAvailable: {list(apiGet.keys())}",
                parent=app
            )
    except requests.exceptions.RequestException as e:
        messagebox.showerror(
            "connection error",
            f"Unable to connect to the API:\n{e}",
            parent=app
        )
    except KeyError as e:
        messagebox.showerror(
            "Data error",
            f"field not found in the API response: {e}",
            parent=app
        )
    except Exception as e:
        messagebox.showerror(
            "unexpected error",
            f"An error occurred.:\n{type(e).__name__}: {e}",
            parent=app
        )
      




    # interface initialization
app = ctk.CTk()
app.geometry("320x250")
app.title("Currency Converter")

ctk.CTkLabel(app, text="Select Currency to convert").pack(pady=10)
ctk.CTkLabel(app, text="If your currency is not in the options below,\n please type its name.").pack(pady=10)

currency1 = ctk.CTkComboBox(
    app,
    values=["USD", "BRL", "EUR", "JPY", "GBP","CAD"]
)
currency1.set("BRL") 
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



