import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x_range = st.slider('Pilih rentang', -10.0, 10.0, (-5.0, 5.0))
st.write('Rentang x:', x_range)

x = np.linspace(x_range[0], x_range[1], 400)
y1 = x**2 + 11*x - 19
y2 = np.sin(x)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

ax1.plot(x, y1, label='$x^2 + 11x - 19$', color='b')  # plot fungsi x^2 + 11x - 19
ax1.set_ylabel("y")
ax1.legend(prop={'size': 12})
ax1.grid(color='green', linestyle='-.', linewidth=0.5)

ax2.plot(x, y2, label='$\sin(x)$', color='r')  # plot fungsi sinus
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.legend(prop={'size': 12})
ax2.grid(color='green', linestyle='-.', linewidth=0.5)

plt.tight_layout()
st.pyplot(fig)
