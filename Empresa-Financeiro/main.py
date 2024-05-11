import tkinter as tk
from tkinter import Toplevel, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Módulos customizados
from modules.api_integration import get_real_time_price, get_historical_data
from modules.security import authenticate_user

def plot_stock_history():
    symbol = entry_symbol.get().strip().upper()
    if not symbol:
        messagebox.showinfo("Input Error", "Please enter a stock symbol.")
        return
    df = get_historical_data(symbol)
    if df is not None and not df.empty:
        top = Toplevel()
        top.title(f"Stock History for {symbol}")
        fig, ax = plt.subplots()
        df.plot(ax=ax, title=f'Historical Close Prices of {symbol}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (USD)')
        canvas = FigureCanvasTkAgg(fig, master=top)
        canvas.draw()
        canvas.get_tk_widget().pack()
        top.mainloop()
    else:
        messagebox.showerror("Error", "Failed to retrieve historical data.")

def login():
    password = entry_password.get()
    if authenticate_user(password):
        login_frame.pack_forget()
        main_frame.pack()
    else:
        messagebox.showerror("Authentication Failed", "The password is incorrect.")

def fetch_and_display_price():
    symbol = entry_symbol.get().strip().upper()
    if not symbol:
        messagebox.showinfo("Input Error", "Please enter a stock symbol.")
        return
    price = get_real_time_price(symbol)
    if price is not None:
        label_price.config(text=f"Current Price: ${price:.2f}")
    else:
        label_price.config(text="Failed to retrieve price.")

root = tk.Tk()
root.title("Investor System")

# Configuração da tela de login
login_frame = tk.Frame(root)
login_frame.pack(padx=20, pady=20)

label_password = tk.Label(login_frame, text="Enter Password:")
label_password.pack()

entry_password = tk.Entry(login_frame, show="*")
entry_password.pack()

button_login = tk.Button(login_frame, text="Login", command=login)
button_login.pack(pady=10)

# Configuração do layout principal
main_frame = tk.Frame(root)

label_symbol = tk.Label(main_frame, text="Enter Stock Symbol:")
label_symbol.pack()

entry_symbol = tk.Entry(main_frame, width=20)
entry_symbol.pack()

button_fetch = tk.Button(main_frame, text="Get Price", command=fetch_and_display_price)
button_fetch.pack(pady=10)

label_price = tk.Label(main_frame, text="Current Price: $0.00")
label_price.pack()

button_plot_history = tk.Button(main_frame, text="Plot Stock History", command=plot_stock_history)
button_plot_history.pack(pady=10)

root.mainloop()


