import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# =====================================================
# TÍTULO
# =====================================================

st.title("Modelo Lotka-Volterra Interactivo")

st.write("""
Modelo depredador-presa entre peces nativos
y trucha arcoíris.
""")

# =====================================================
# TIEMPO
# =====================================================

t = np.linspace(0, 100, 1000)

# =====================================================
# CONDICIONES INICIALES
# =====================================================

N0 = 80
P0 = 20

# =====================================================
# SLIDERS STREAMLIT
# =====================================================

st.sidebar.header("Parámetros del modelo")

r = st.sidebar.slider(
    "r - crecimiento de peces",
    0.1, 2.0, 0.6, 0.01
)

a = st.sidebar.slider(
    "a - depredación",
    0.001, 0.1, 0.02, 0.001
)

b = st.sidebar.slider(
    "b - eficiencia",
    0.001, 0.05, 0.01, 0.001
)

m = st.sidebar.slider(
    "m - mortalidad de truchas",
    0.1, 1.0, 0.4, 0.01
)

# =====================================================
# MODELO
# =====================================================

def modelo(y, t, r, a, b, m):

    N, P = y

    dNdt = r * N - a * N * P
    dPdt = b * N * P - m * P

    return [dNdt, dPdt]

# =====================================================
# RESOLVER SISTEMA
# =====================================================

def resolver(r, a, b, m):

    y0 = [N0, P0]

    sol = odeint(modelo, y0, t, args=(r, a, b, m))

    return sol[:,0], sol[:,1]

# =====================================================
# SOLUCIÓN
# =====================================================

N, P = resolver(r, a, b, m)

# =====================================================
# GRÁFICA PRINCIPAL
# =====================================================

fig, ax = plt.subplots(figsize=(10,6))

ax.plot(t, N, label='Peces nativos')
ax.plot(t, P, label='Truchas')

ax.set_title('Modelo Depredador-Presa')
ax.set_xlabel('Tiempo')
ax.set_ylabel('Población')

ax.legend()
ax.grid()

st.pyplot(fig)

# =====================================================
# PLANO DE FASES
# =====================================================

fig2, ax2 = plt.subplots(figsize=(8,6))

ax2.plot(N, P)

ax2.set_title('Plano de fases')
ax2.set_xlabel('Peces nativos')
ax2.set_ylabel('Truchas')

ax2.grid()

st.pyplot(fig2)

# =====================================================
# MOSTRAR VALORES
# =====================================================

st.subheader("Parámetros actuales")

st.write(f"r = {r}")
st.write(f"a = {a}")
st.write(f"b = {b}")
st.write(f"m = {m}")