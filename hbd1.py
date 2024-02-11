import streamlit as st
from datetime import datetime

def generate_birthday_message(name, age, assistant_name, assistant_wish):
    # Daftar ucapan selamat ulang tahun
    birthday_messages = [
        f"Selamat ulang tahun, {name}! Semoga hari ulang tahunmu penuh dengan kebahagiaan dan keceriaan. - {assistant_name}",
        f"Wah, hari ini ulang tahun {name}! Semoga semua impianmu tercapai di usia yang baru ini. - {assistant_name}",
        f"Happy birthday, {name}! Semoga setiap momen di hari ini menjadi kenangan yang tak terlupakan. - {assistant_name}",
        f"Selamat ulang tahun yang ke-{age}, {name}! Semoga cinta dan kebahagiaan selalu menyertaimu. - {assistant_name}",
        f"Ulang tahun yang penuh kebahagiaan untukmu, {name}! Semoga usiamu semakin berkah dan indah. - {assistant_name}",
        f"Happy birthday, {name}! Semoga tahun ini menjadi awal dari petualangan baru yang menyenangkan. - {assistant_name}",
        f"{assistant_wish} - {assistant_name}"
    ]
    # Memilih ucapan sesuai dengan usia
    message = birthday_messages[min(len(birthday_messages)-1, age-1)]
    return message

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Ucapan Ulang Tahun ke Pacar 🎉</h1>", unsafe_allow_html=True)
st.subheader('Masukkan informasi pacar dan tanggal lahir:')

# Input nama pacar
pacar_name_option = st.radio('Pilih Nama Pacar:', ('aksa ganteng aja ', 'aksa ganteng banget'))
if pacar_name_option == 'Nama Pacar Saya':
    pacar_name = st.text_input('Nama Pacar:')
else:
    pacar_name = 'Nama Pacar Saya'

# Input tanggal lahir pacar
birthdate = st.date_input('Tanggal Lahir')

# Menampilkan input untuk keinginan asisten
st.subheader('Keinginan dari Asisten:')
assistant_wish = st.text_area('Keinginan:', value="Selamat ulang tahun yang indah!")

# Menghitung usia pacar dari tanggal lahir hingga sekarang
if birthdate:
    current_date = datetime.now().date()
    age = current_date.year - birthdate.year
    if (current_date.month, current_date.day) < (birthdate.month, birthdate.day):
        age -= 1
    st.write(f"Usia Pacar: {age} tahun")

    # Tombol untuk menghasilkan ucapan
    if st.button('Generate Ucapan'):
        if pacar_name:
            birthday_message = generate_birthday_message(pacar_name, age, "Asisten", assistant_wish)
        else:
            birthday_message = generate_birthday_message("Pacar", age, "Asisten", assistant_wish)
        st.write(birthday_message)
