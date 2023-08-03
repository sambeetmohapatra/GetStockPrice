import tkinter as tk
import yfinance as yf
from requests import HTTPError
from ttkthemes import themed_tk

def get_stock_value(ticker):
    data = yf.Ticker(ticker).info
    return data["currentPrice"]

def get_current_date():
    import datetime
    return datetime.datetime.today().strftime("%Y-%m-%d")


root = themed_tk.ThemedTk()

root.title("STOCK WIDGET")
root.geometry("500x500")

root.set_theme("aqua")

# Create a frame.
frame = tk.Frame(root)
frame.config(width=400, height=200)
frame.pack()

label = tk.Label(frame, text="Enter the Stock Name")

# Place the label on grid in row 0, column 0.
label.grid(row=0, column=2,padx=10,pady=(50,10))

ticker_entry = tk.Entry(frame,font=("Arial", 12),fg="blue")
ticker_entry.grid(row=1,column=2,padx=10,pady=(30,30))

stock_label= tk.Label(frame,font=("Arial", 16),fg="black",borderwidth=3)
stock_label.grid(row=3,column=2,padx=10,pady=(60,10))

value_label = tk.Label(frame,font=("Arial", 14),fg="green",borderwidth=2)
value_label.grid(row=3,column=2,padx=10,pady=(30,40))

def update_value():
    try:
        ticker = ticker_entry.get()
        date = get_current_date()
        value = get_stock_value(ticker)
        value_label.config(text=value)
        stock_name = yf.Ticker(ticker).info["longName"]
        stock_label.config(text=stock_name)
    except KeyError:
        value = "!! Stock Not found. For Indian stocks use .NS or .BO at the end and retry"
        value_label.config(text=value)
    except HTTPError:
        pass

update_button = tk.Button(frame, text="Get Stock Price", command=update_value)
update_button.grid(row=2, column=2,padx=10,pady=(50,10))

root.mainloop()
