import streamlit as st

# Membuat fungsi untuk menghasilkan ucapan ulang tahun untuk pacar
def generate_birthday_message(name, age):
    return f"Selamat ulang tahun yang ke-{age}, {name}! Semoga hari ulang tahunmu penuh dengan kebahagiaan dan keceriaan."

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Ulang Tahun Firnanda valen 💖</h1>", unsafe_allow_html=True)

# Input nama kamu sayang
name = st.text_input('Nama Pacar:')

# Input usia kamu sayang
age = st.number_input('Usia Pacar:', min_value=1, max_value=150, value=1)

# Tombol untuk menampilkan ucapan
if st.button('Tampilkan Ucapan'):
    if name:
        birthday_message = generate_birthday_message(name, age)
        st.write(birthday_message)
    else:
        st.error("Mohon masukkan nama pacar untuk menampilkan ucapan ulang tahun.")
