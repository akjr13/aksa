import streamlit as st
from datetime import datetime

def generate_anniversary_message(name, years):
    # Daftar ucapan selamat tahun pacar
    anniversary_messages = [
        f"Selamat {years} tahun bersama, {name}! Semoga cinta kita semakin kuat dan abadi.",
        f"Wah, sudah {years} tahun ya kita bersama, {name}! Setiap momen bersamamu sangat berharga.",
        f"Hari ini adalah hari spesial, {years} tahun bersama, {name}! Terima kasih telah menjadi bagian dari hidupku.",
        f"Hari ini adalah perayaan {years} tahun cinta kita, {name}. Aku sangat bersyukur memiliki kamu di sampingku.",
        f"Tak terasa sudah {years} tahun kita berdua, {name}. Semoga cinta kita selalu menyala dan tak pernah pudar.",
        f"Happy anniversary yang ke-{years}, {name}! Semoga tahun ini penuh dengan kebahagiaan dan keberkahan."
    ]
    # Memilih ucapan sesuai dengan tahun pacar
    message = anniversary_messages[min(len(anniversary_messages)-1, years-1)]
    return message

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Tahun Pacar 💖</h1>", unsafe_allow_html=True)
st.subheader('Masukkan informasi pacar dan tanggal jadian:')

# Input nama pacar
pacar_name = st.text_input('Nama Pacar:')
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
        if pacar_name:
            anniversary_message = generate_anniversary_message(pacar_name, years)
        else:
            anniversary_message = generate_anniversary_message("Pacar", years)
        st.write(anniversary_message)
