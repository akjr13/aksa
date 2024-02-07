import streamlit as st

# Menampilkan header di tengah
st.markdown("<h1 style='text-align: center;'>Aksamala 🔥</h1>", unsafe_allow_html=True)
st.subheader('Kalkulator Suhu')

# Membuat empat kolom
c1, c2, c3 = st.columns(3)

with c1:
    temperature = st.number_input('Masukkan suhu', step=1)

with c2:
    # Pilih satuan suhu awal
    from_unit = st.selectbox('Dari', ('Celcius', 'Fahrenheit', 'Kelvin'))

with c3:
    # Pilih satuan suhu yang diinginkan
    to_unit = st.selectbox('Ke', ('Celcius', 'Fahrenheit', 'Kelvin'))

def convert_temperature(temperature, from_unit, to_unit):
    if from_unit == to_unit:
        return temperature
    if from_unit == 'Celcius':
        if to_unit == 'Fahrenheit':
            return (temperature * 9/5) + 32
        elif to_unit == 'Kelvin':
            return temperature + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celcius':
            return (temperature - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (temperature - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celcius':
            return temperature - 273.15
        elif to_unit == 'Fahrenheit':
            return (temperature - 273.15) * 9/5 + 32

# Menghitung hasil konversi suhu
converted_temperature = convert_temperature(temperature, from_unit, to_unit)

# Menampilkan hasil dalam kolom terpisah
st.text_area('Hasil:', value=converted_temperature, height=50)

# Menampilkan keterangan hak cipta
st.caption('Copyright © Aksamala.A/210322607297')
