import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x_range = st.slider('Pilih rentang', -10.0, 10.0, (-5.0, 5.0))
st.write('Rentang x:', x_range)

x = np.linspace(x_range[0], x_range[1], 400)
y1 = x**2 + 11*x - 19
y2 = np.sin(x)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y1, label='$x^2 + 11x - 19$', color='b')  # plot fungsi x^2 + 11x - 19
ax.plot(x, y2, label='$\sin(x)$', color='r')  # plot fungsi sinus
ax.set_ylabel("y")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=15)
ax.tick_params(axis='x', labelsize=15)
ax.legend(prop={'size': 15})
plt.grid(color='green', linestyle='-.', linewidth=0.5)
st.pyplot(fig)
