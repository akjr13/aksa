import streamlit as st

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Aksamala 🔥</h1>", unsafe_allow_html=True)
st.subheader('Kalkulator')

# Membuat tiga kolom
c1, c2, c3 = st.columns(3)

with c1:
    x = st.number_input('Masukkan angka pertama', step=1)

with c2:
    # Pilih operasi
    operation = st.selectbox('Pilih operasi', ('+', '-', 'x', '/'))

with c3:
    y = st.number_input('Masukkan angka kedua', step=1)

def calculate(x , y, operation):
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == 'x':
        result = x * y
    elif operation == '/':
        if y != 0:  # Menghindari pembagian dengan nol
            result = x / y
        else:
            result = "Error: Pembagian dengan nol"
    return result

# Menghitung hasil
result = calculate(x, y, operation)

# Menampilkan hasil dalam kotak atau area terpisah
st.text('Hasil: {}'.format(result))

# Menampilkan keterangan hak cipta
st.caption('Copyright © Aksamala.A/210322607297')
