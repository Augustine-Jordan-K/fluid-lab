import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fluid Mechanics Virtual Lab", layout="wide")

# Sidebar - Module Selection
st.sidebar.title("Virtual Lab Modules")
module = st.sidebar.radio("Select Module", ("Pitot Tube Flow", "Reynolds Number Visualization"))

# --- Pitot Tube Module ---
if module == "Pitot Tube Flow":
    st.title("Pitot Tube Flow Measurement")
    st.write("This simulation demonstrates how velocity affects pressure difference and manometer levels.")

    # Inputs
    velocity = st.slider("Fluid Velocity (m/s)", 0.0, 20.0, 5.0, 0.1)
    fluid_density = st.slider("Fluid Density (kg/m³)", 800.0, 1200.0, 1000.0, 10.0)
    g = 9.81  # gravity constant

    # Calculations
    delta_p = 0.5 * fluid_density * velocity**2  # Bernoulli Equation
    h_cm = delta_p / (fluid_density * g) * 100  # Convert to cm

    st.markdown(f"**Pressure Difference (ΔP):** {delta_p:.2f} Pa")
    st.markdown(f"**Manometer Height (Δh):** {h_cm:.2f} cm")

    # Visualization
    fig, ax = plt.subplots(figsize=(2, 5))
    ax.bar([0], [h_cm], width=0.5, color='blue')
    ax.set_ylim(0, 50)
    ax.set_ylabel("Manometer Height (cm)")
    ax.set_xticks([])
    ax.set_title("Manometer Reading")
    st.pyplot(fig)

# --- Reynolds Number Module ---
elif module == "Reynolds Number Visualization":
    st.title("Reynolds Number Flow Visualization")
    st.write("Visual representation of flow regimes based on Reynolds number.")

    # Inputs
    diameter = st.slider("Pipe Diameter (m)", 0.01, 0.1, 0.02, 0.005)
    velocity = st.slider("Fluid Velocity (m/s)", 0.1, 5.0, 1.0, 0.1)
    density = st.slider("Fluid Density (kg/m³)", 800.0, 1200.0, 1000.0, 10.0)
    viscosity = st.slider("Fluid Viscosity (Pa·s)", 0.001, 0.01, 0.001, 0.0005)

    # Reynolds Number Calculation
    Re = (density * velocity * diameter) / viscosity

    if Re < 2000:
        flow_type = "Laminar"
        color = "green"
    elif 2000 <= Re <= 4000:
        flow_type = "Transitional"
        color = "orange"
    else:
        flow_type = "Turbulent"
        color = "red"

    st.markdown(f"**Reynolds Number (Re):** {Re:.2f}")
    st.markdown(f"**Flow Type:** {flow_type}")

    # Visualization
    fig, ax = plt.subplots(figsize=(6, 1))
    ax.axhline(0, color='black', linewidth=4)
    ax.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100) * Re/1000), color=color, linewidth=2)
    ax.set_yticks([])
    ax.set_title(f"{flow_type} Flow Visualization", color=color)
    st.pyplot(fig)
