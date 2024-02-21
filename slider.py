import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x_range = st.slider('Pilih rentang', 0.0, 2.0, (0.2, 0.5))
st.write('nilai x:', x_range)
y = st.slider('Set nilai', 0.0, 10.0, 5.0)
st.write('nilai y:', y)

t = np.linspace(x_range[0] * np.pi, x_range[1] * np.pi, 100)
u = np.sin(y * t)

# Plot sin(t)
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.plot(t, u, label='sin(t)', color='b')
ax1.set_ylabel("")
ax1.set_xlabel("t")
ax1.tick_params(axis='y', labelsize=12)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=30, ha='right')
ax1.tick_params(axis='x', labelsize=10)
ax1.grid(color='green', linestyle='-.', linewidth=0.5)
ax1.legend()
st.pyplot(fig1)

# Calculate f(x) = x^2 + 11x - 19
def f(x):
    return x**2 + 11*x - 19

v = f(t)

# Compute integral using trapezoidal rule
integral = np.trapz(v, t)

# Plot f(t) and its integral
fig2, ax2 = plt.subplots(figsize=(8, 6))
ax2.plot(t, v, label='f(t)', color='r')
ax2.fill_between(t, 0, v, alpha=0.2, color='r', label='Integral')
ax2.set_ylabel("")
ax2.set_xlabel("t")
ax2.tick_params(axis='y', labelsize=12)
ax2.set_xticklabels(ax2.get_xticklabels(), rotation=30, ha='right')
ax2.tick_params(axis='x', labelsize=10)
ax2.grid(color='green', linestyle='-.', linewidth=0.5)
ax2.legend()
st.pyplot(fig2)

st.write(f'Integral (using trapezoidal rule): {integral}')
