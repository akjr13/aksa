import streamlit as st
from datetime import datetime

# Membuat fungsi untuk menghasilkan ucapan ulang tahun untuk pacar
def generate_birthday_message(name, birthdate, wish):
    return f"Selamat ulang tahun, {name}! Semoga hari ulang tahunmu penuh dengan kebahagiaan dan keceriaan. {wish}"

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Ulang Tahun Firnanda Valen 💖</h1>", unsafe_allow_html=True)

# Input nama pacar
name = st.text_input('Nama Pacar:')

# Batas atas tanggal lahir hingga tahun 2000
max_date = datetime(2000, 12, 31)

# Input tanggal lahir Anda
birthdate = st.date_input('Tanggal Lahir Anda:', max_value=max_date)

# Input keinginan dari Anda
wish = st.text_area('Keinginan dari Anda:')

# Tombol untuk menampilkan ucapan
if st.button('Tampilkan Ucapan'):
    if name:
        birthday_message = generate_birthday_message(name, birthdate, wish)
        st.write(birthday_message)
    else:
        st.error("Mohon masukkan nama pacar untuk menampilkan ucapan ulang tahun.")
