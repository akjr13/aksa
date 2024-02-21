import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

x = st.slider('Select range', 0.0, 2.0, (0.2, 0.6))
st.write('nilai x:', x)

y = st.slider('Set nilai', 0.0, 100.0, 25.0)
st.write('nilai y:', y)

t = np.linspace(x[0]*np.pi, x[1]*np.pi, 100)
st.write('nilai t:', t)

u = np.sin(t)

fig, ax = plt.subplots(figsize=(16, 8))

ax.set_ylabel("")
ax.plot(t, u, label='sin(t)', color='b') # Plotting sin(t) curve
ax.set_xlabel("t")
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
plt.grid(color='green', linestyle='.', linewidth=.5)

st.pyplot(fig)
