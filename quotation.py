# Import requests to connect to the API
import requests
# Import datetime to check the date and time the information was given
from datetime import datetime
# Import tkinter in order to create a window to execute the code
from tkinter import *


# Configuring a function to consume the API and gather the information regarding the Dollar/Euro/BTC Quotation
def get_quotation():
    requisition = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisition_dic = requisition.json()
    dolar_quotation = float(requisition_dic["USDBRL"]["bid"])
    euro_quotation = float(requisition_dic["EURBRL"]["bid"])
    btc_quotation = float(requisition_dic["BTCBRL"]["bid"])

    # Text to be showed to the end user as soon as they hit the button
    text_quote = f'''
    Updated Quotation: {datetime.now()}
    
    Dollar: R${dolar_quotation:.2f}
    Euro: R${euro_quotation:.2f}
    BTC: R${btc_quotation}.00'''
    # Quotation text that will replace the initial text (which is in blank).
    quotation_text['text'] = text_quote


# Invoke the Window
window = Tk()
# Window Title
window.title('Dollar/Euro/BitCoin Quotation')
# Label it is just a text
text = Label(window, text='Click in the button to check the Dollar, Euro and BitCoin quotation')
# Every single item to the window must be placed a grid to be showed in the window
text.grid(column=0, row=0, padx=10, pady=10)

# Created a button be hit by the end user
button = Button(window, text='Update Quotation', command=get_quotation)
button.grid(column=0, row=1, padx=10, pady=10)

# The button will invoke the 'quotation_text' which will show the updated quotation
quotation_text = Label(window, text='')
quotation_text.grid(column=0, row=2, padx=10, pady=10)

# without the mainloop() the code will run and then the window will disappear
window.mainloop()
