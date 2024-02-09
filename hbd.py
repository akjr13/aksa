import streamlit as st
from datetime import datetime

def generate_birthday_message(friend_name, age):
    # Daftar ucapan selamat ulang tahun
    birthday_messages = [
        f"Selamat ulang tahun, {friend_name}! Semoga hari ulang tahunmu penuh dengan kebahagiaan dan keceriaan.",
        f"Wah, hari ini ulang tahun {friend_name}! Semoga semua impianmu tercapai di usia yang baru ini.",
        f"Happy birthday, {friend_name}! Semoga setiap momen di hari ini menjadi kenangan yang tak terlupakan.",
        f"Selamat ulang tahun yang ke-{age}, {friend_name}! Semoga cinta dan kebahagiaan selalu menyertaimu.",
        f"Ulang tahun yang penuh kebahagiaan untukmu, {friend_name}! Semoga usiamu semakin berkah dan indah.",
        f"Happy birthday, {friend_name}! Semoga tahun ini menjadi awal dari petualangan baru yang menyenangkan."
    ]
    # Memilih ucapan sesuai dengan usia
    message = birthday_messages[min(len(birthday_messages)-1, age-1)]
    return message

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Ulang Tahun 🎉</h1>", unsafe_allow_html=True)
st.subheader('Masukkan informasi teman dan tanggal lahir:')

# Input nama teman
friend_name = st.text_input('Nama Teman:')
birthdate = st.date_input('Tanggal Lahir')

# Menghitung usia teman dari tanggal lahir hingga sekarang
if birthdate:
    current_date = datetime.now().date()
    age = current_date.year - birthdate.year
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
    st.write(f"Usia Teman: {age} tahun")

    # Tombol untuk menghasilkan ucapan
    if st.button('Generate Ucapan'):
        if friend_name:
            birthday_message = generate_birthday_message(friend_name, age)
        else:
            birthday_message = generate_birthday_message("Teman", age)
        st.write(birthday_message)
