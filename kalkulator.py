import streamlit as st

st.header('Aksamala :sparkles:')
st.subheader('Kalkulator')

c1, c2, c3 = st.columns(3)

with c1:
    num1 = st.number_input('Masukkan angka pertama', step=1)

with c2:
    # Pilih operasi
    operation = st.selectbox('Pilih operasi', ('+', '-', 'x', '/'))

with c3:
    num2 = st.number_input('Masukkan angka kedua', step=1)

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

result = calculate(num1, num2, operation)
st.write('Hasil:', result)

st.caption('Aksamala Arfendi')
