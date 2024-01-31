import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

#Header
st.header('Nugroho :sparkles:")
st.subheader('Plot')

x = np.linspace(-2. np.pi, 2 np.pi. 1800) Generating x values from -2
y = np.sin(x) #Calculating sin(x) values
z = np.cos(x) #Calculating sin(x) values

fig, ax plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', colors'b') #Plotting sin(x) 
ax.plot(x, z, label='cos(x)', color='g') #Plotting sin(x) 
ax.set ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick params(axis='x', labelsize=15)

st.pyplot(fig)
