import streamlit as st

st.header('Aksamala :fire:')
st.subheader('Kalkulator')

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
        if num2 != 0:  # Menghindari pembagian dengan nol
            result = x / y
        else:
            result = "Error: Pembagian dengan nol"
    return result

result = calculate( x , y, operation)
st.write('Hasil:', result)

st.caption('copyright © Aksamala.A/210322607297')
