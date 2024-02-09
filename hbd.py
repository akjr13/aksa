import streamlit as st
from datetime import datetime

def generate_anniversary_message(years):
    # Daftar ucapan selamat tahun pacar
    anniversary_messages = [
        "Selamat {} tahun bersama! Semoga cinta kita semakin kuat dan abadi.",
        "Wah, sudah {} tahun ya kita bersama! Setiap momen bersamamu sangat berharga.",
        "Hari ini adalah hari spesial, {} tahun bersama! Terima kasih telah menjadi bagian dari hidupku.",
        "Hari ini adalah perayaan {} tahun cinta kita. Aku sangat bersyukur memiliki kamu di sampingku.",
        "Tak terasa sudah {} tahun kita berdua. Semoga cinta kita selalu menyala dan tak pernah pudar.",
        "Happy anniversary yang ke-{}! Semoga tahun ini penuh dengan kebahagiaan dan keberkahan."
    ]
    # Memilih ucapan sesuai dengan tahun pacar
    message = anniversary_messages[min(len(anniversary_messages)-1, years-1)].format(years)
    return message

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Tahun Pacar 💖</h1>", unsafe_allow_html=True)
st.subheader('Masukkan tanggal jadian:')
date = st.date_input('Tanggal Jadian')

# Menghitung tahun dari tanggal jadian hingga sekarang
if date:
    current_date = datetime.now().date()
    years = current_date.year - date.year
    if (current_date.month, current_date.day) < (date.month, date.day):
        years -= 1
    st.write(f"Tahun Pacar: {years} tahun")

    # Tombol untuk menghasilkan ucapan
    if st.button('Generate Ucapan'):
        anniversary_message = generate_anniversary_message(years)
        st.write(anniversary_message)
