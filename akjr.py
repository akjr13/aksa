import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Header
st.header('aksamla :sparkles:')
st.subheader('Plot')

# Generating x values from -2 to 2*pi with 1800 points
x = np.linspace(-2*np.pi, 2*np.pi, 1800)

# Calculating sin(x) and cos(x) values
y = np.sin(x)
z = np.cos(x)

# Plotting sin(x) and cos(x)
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(x, y, label='sin(x)', color='b')
ax.plot(x, z, label='cos(x)', color='g')

# Adjusting plot settings
ax.set_ylabel("")
ax.set_xlabel("x")
ax.tick_params(axis='y', labelsize=20)
ax.set_xticklabels(ax.get_xticklabels(), rotation=30, ha='right')
ax.tick_params(axis='x', labelsize=15)

# Displaying the plot in Streamlit
st.pyplot(fig)
