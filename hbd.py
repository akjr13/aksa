import streamlit as st

# Membuat fungsi untuk menghasilkan ucapan ulang tahun untuk pacar
def generate_birthday_message(name, age, wish, future_wish):
    return f"Selamat ulang tahun yang ke-{age}, {name}! Semoga hari ulang tahunmu penuh dengan kebahagiaan dan keceriaan. {wish} {future_wish}"

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Ulang Tahun Firnanda Valen 💖</h1>", unsafe_allow_html=True)

# Input nama pacar
name = st.text_input('Nama Pacar:')

# Input usia pacar
age = st.number_input('Usia Pacar:', min_value=1, max_value=150, value=1)

# Input keinginan dari Anda
wish = st.text_area('Keinginan dari Anda:')

# Input harapan Anda untuk masa depan bersama
future_wish = st.text_area('Harapan Anda untuk Masa Depan:')

# Tombol untuk menampilkan ucapan
if st.button('Tampilkan Ucapan'):
    if name:
        birthday_message = generate_birthday_message(name, age, wish, future_wish)
        st.write(birthday_message)
    else:
        st.error("Mohon masukkan nama pacar untuk menampilkan ucapan ulang tahun.")
