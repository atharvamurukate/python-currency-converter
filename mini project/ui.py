import tkinter as tk
from tkinter import ttk
from converter import CurrencyConverter
from graph import CurrencyGraph

class CurrencyConverterUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("400x300")

        self.converter = CurrencyConverter(api_url="https://api.exchangerate-api.com/v4")
        self.graph = CurrencyGraph(api_url="https://api.exchangerate-api.com/v4")

        self.create_widgets()

    def create_widgets(self):
        self.from_currency_label = ttk.Label(self, text="From Currency:")
        self.from_currency_label.pack()
        self.from_currency_entry = ttk.Entry(self)
        self.from_currency_entry.pack()

        self.to_currency_label = ttk.Label(self, text="To Currency:")
        self.to_currency_label.pack()
        self.to_currency_entry = ttk.Entry(self)
        self.to_currency_entry.pack()

        self.amount_label = ttk.Label(self, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.pack()

        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_currency)
        self.convert_button.pack()

        self.result_label = ttk.Label(self, text="")
        self.result_label.pack()

        self.graph_button = ttk.Button(self, text="Show Graph", command=self.show_graph)
        self.graph_button.pack()

    def convert_currency(self):
        from_currency = self.from_currency_entry.get()
        to_currency = self.to_currency_entry.get()
        amount = float(self.amount_entry.get())
        result = self.converter.convert(amount, from_currency, to_currency)
        self.result_label.config(text=f"Converted Amount: {result:.2f} {to_currency}")

    def show_graph(self):
        from_currency = self.from_currency_entry.get()
        to_currency = self.to_currency_entry.get()
        self.graph.plot_graph(from_currency, to_currency)
