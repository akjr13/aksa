import streamlit as st

# Header
st.header('Calculator')

# Membuat dua kolom
c1, c2 = st.columns(2)

# Kolom pertama
with c1:
    num1 = st.number_input('Masukkan angka pertama')

# Kolom kedua
with c2:
    num2 = st.number_input('Masukkan angka kedua')

# Pilih operasi
operation = st.selectbox('Pilih operasi', ('+', '-', 'x', '/'))

# Fungsi untuk melakukan operasi
def calculate(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == 'x':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:  # Menghindari pembagian dengan nol
            result = num1 / num2
        else:
            result = "Error: Pembagian dengan nol"
    return result

# Tombol untuk menghitung hasil
if st.button('Hitung'):
    result = calculate(num1, num2, operation)
    st.write('Hasil:', result)
