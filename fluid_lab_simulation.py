import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Fluid Mechanics Virtual Lab", layout="wide")

# Sidebar - Module Selection
st.sidebar.title("Virtual Lab Modules")
module = st.sidebar.radio("Select Module", ("Pitot Tube Flow", "Reynolds Number Visualization"))

# --- PITOT TUBE MODULE ---
if module == "Pitot Tube Flow":
    st.title("Pitot Tube Flow Measurement Virtual Lab")

    # Educational content
    with st.expander("🎯 Aim"):
        st.markdown("To determine the fluid velocity by measuring the pressure difference using a Pitot tube and manometer.")

    with st.expander("🧪 Apparatus Required"):
        st.markdown("- Pitot Tube\n- Manometer\n- Fluid Tank\n- Measuring scale\n- Stopwatch")

    with st.expander("📘 Theory"):
        st.markdown("""
        The Pitot tube measures the fluid flow velocity by converting the kinetic energy into potential energy.
        The pressure difference (ΔP) measured using a manometer is related to the velocity using Bernoulli’s equation:
        \n\n**ΔP = 0.5 × ρ × V²**\n\n
        where ρ is fluid density and V is velocity.
        """)

    with st.expander("🧪 Procedure"):
        st.markdown("""
        1. Insert the Pitot tube into the flow stream.
        2. Note the rise in manometer levels.
        3. Vary the fluid velocity and observe changes in Δh.
        4. Use Bernoulli’s equation to compute velocity.
        """)

    with st.expander("🖼️ Schematic Diagram"):
        st.image("https://me.iitp.ac.in/Virtual-Fluid-Laboratory/pitot/images/pitot_tube_labelled.png", caption="Pitot Tube Setup\nCredit: IIT Patna", use_column_width=True)  # Replace with actual schematic URL

    # Simulation
    st.header("🔬 Simulation")
    velocity = st.slider("Fluid Velocity (m/s)", 0.0, 20.0, 5.0, 0.1)
    fluid_density = st.slider("Fluid Density (kg/m³)", 800.0, 1200.0, 1000.0, 10.0)
    g = 9.81

    delta_p = 0.5 * fluid_density * velocity**2
    h_cm = delta_p / (fluid_density * g) * 100

    st.markdown(f"**Pressure Difference (ΔP):** {delta_p:.2f} Pa")
    st.markdown(f"**Manometer Height (Δh):** {h_cm:.2f} cm")

    fig, ax = plt.subplots(figsize=(2, 5))
    ax.bar([0], [h_cm], width=0.5, color='blue')
    ax.set_ylim(0, 50)
    ax.set_ylabel("Manometer Height (cm)")
    ax.set_xticks([])
    ax.set_title("Manometer Reading")
    st.pyplot(fig)

# --- REYNOLDS NUMBER MODULE ---
elif module == "Reynolds Number Visualization":
    st.title("Reynolds Number Flow Visualization Virtual Lab")

    # Educational content
    with st.expander("🎯 Aim"):
        st.markdown("To study different flow regimes by calculating Reynolds Number using pipe flow data.")

    with st.expander("🧪 Apparatus Required"):
        st.markdown("- Flow channel setup\n- Measuring pipe\n- Stopwatch\n- Fluid of known density and viscosity")

    with st.expander("📘 Theory"):
        st.markdown("""
        Reynolds Number (Re) characterizes flow type:
        \n\n**Re = (ρ × V × D) / μ**
        \n\n
        - Laminar: Re < 2000\n
        - Transitional: 2000 ≤ Re ≤ 4000\n
        - Turbulent: Re > 4000
        """)

    with st.expander("🧪 Procedure"):
        st.markdown("""
        1. Select a pipe and fluid type.
        2. Adjust flow velocity and note parameters.
        3. Compute Reynolds number.
        4. Identify the flow regime from Re.
        """)

    with st.expander("🖼️ Schematic Diagram"):
        st.image("https://me.iitp.ac.in/Virtual-Fluid-Laboratory/images/reynolds_labelled.png", caption="Flow Regimes in Pipe\nCredit: IIT Patna", use_column_width=True)  # Replace with actual schematic URL

    # Simulation
    st.header("🔬 Simulation")
    diameter = st.slider("Pipe Diameter (m)", 0.01, 0.1, 0.02, 0.005)
    velocity = st.slider("Fluid Velocity (m/s)", 0.1, 5.0, 1.0, 0.1)
    density = st.slider("Fluid Density (kg/m³)", 800.0, 1200.0, 1000.0, 10.0)
    viscosity = st.slider("Fluid Viscosity (Pa·s)", 0.001, 0.01, 0.001, 0.0005)

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

    fig, ax = plt.subplots(figsize=(6, 1))
    ax.axhline(0, color='black', linewidth=4)
    ax.plot(np.linspace(0, 10, 100), np.sin(np.linspace(0, 10, 100) * Re/1000), color=color, linewidth=2)
    ax.set_yticks([])
    ax.set_title(f"{flow_type} Flow Visualization", color=color)
    st.pyplot(fig)
