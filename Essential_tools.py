import os
import csv
import pandas as pd
from datetime import datetime

def clear():
    os.system('cls || clear')

def history_belanja(username, keranjang_user, total_pembelian):
    df = pd.read_csv('history_transaksi.csv')