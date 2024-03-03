import pandas as pd
import streamlit as st
from datetime import datetime

df = pd.read_excel("Laporan Keuangan.xlsx")
st.title("Laporan Keuangan")

tanggal = st.date_input("Masukkan Tanggal")
tanggal_input = pd.to_datetime(tanggal)
omset = st.number_input("Masukkan Total Omset")
penegeluaran_op = st.number_input("Masukkan Total Pengeluaran Operasional")
penegeluaran_non_op = st.number_input("Masukkan Total Pengeluaran Non Operasional")
Laba_Kotor = st.number_input("Masukkan Total Laba Kotor")
pituang = st.number_input("Masukkan Total Piutang")
piutang_ket = st.text_input("Masukkan Ketrangan Piutang")


new_data = {'Tanggal': tanggal_input, 'Omset':omset, 'Pengeluaran Operasional': penegeluaran_op, 'Pengeluaran Non Operasional':penegeluaran_non_op, 'Laba Kotor':Laba_Kotor, "Piutang":pituang,'Keterangan Piutang': piutang_ket}
if st.button("Input Data"):
    df = df.append(new_data, ignore_index=True)
    df["Laba Bersih"] =  df["Laba Kotor"] - df["Pengeluaran Operasional"] - df["Pengeluaran Non Operasional"] - df["Piutang"]
    df
    with pd.ExcelWriter('Laporan Keuangan.xlsx') as writer:
        df.to_excel(writer, sheet_name='Input Keuangan', index=False)
