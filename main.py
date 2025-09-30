import matplotlib
# MUST be set before importing matplotlib.pyplot
matplotlib.use('Agg') 
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# --- Signal Function ---
# Define a function to calculate the value of a sinusoidal function signal at a given time(t) and distance(x)
def sinusoidal_signal(A, f, phi, t, x):
    # The speed of light is used for calculating the wave number (k)
    c = 3e8

    # Calculate the angular frequency of the sine wave (omega)
    omega = 2 * np.pi * f

    # Calculate the wave number of the sine wave (k)
    # k = omega / c = 2 * pi * f / c
    k = 2 * np.pi * f / c

    # Return the value of the sine wave at the given time(t) and distance(x)
    return A * np.sin(k * x - omega * t + phi)


# --- Main Streamlit App Function ---
def main():
    st.title("Sinusoidal Signal Interference Simulator")
    st.markdown("Simulate the interference of two sinusoidal signals in time and distance domains.")

    # --- Sidebar for Input Parameters ---
    st.sidebar.header("Signal Parameters")

    # --- Input for Signal 1 (D1) ---
    st.sidebar.subheader("Signal 1 ($D_1$)")
    A1 = st.sidebar.number_input("Amplitude $A_1$ (V)", value=1.0, min_value=0.01)
    f1 = st.sidebar.number_input("Frequency $f_1$ (Hz)", value=10.0, min_value=0.01)
    phi1 = st.sidebar.number_input("Phase $\phi_1$ (rad)", value=0.0)

    # Only need *one* pair of fixed time/distance for the cross-domain plots
    # For the TIME domain plot, we fix the distance x:
    x_fixed_time = st.sidebar.number_input("Fixed Distance for Time Plot $x_1$ (m)", value=0.0, key='x1_fixed')
    # For the DISTANCE domain plot, we fix the time t:
    t_fixed_distance = st.sidebar.number_input("Fixed Time for Distance Plot $t_1$ (s)", value=0.0, key='t1_fixed')

    st.sidebar.markdown("---")

    # --- Input for Signal 2 (D2) ---
    st.sidebar.subheader("Signal 2 ($D_2$)")
    A2 = st.sidebar.number_input("Amplitude $A_2$ (V)", value=1.0, min_value=0.01)
    f2 = st.sidebar.number_input("Frequency $f_2$ (Hz)", value=10.0, min_value=0.01)
    phi2 = st.sidebar.number_input("Phase $\phi_2$ (rad)", value=np.pi)

    # Use the same fixed time/distance variables for simplicity, as they define the *viewing point*
    x_fixed_time_2 = st.sidebar.number_input("Fixed Distance for Time Plot $x_2$ (m)", value=0.0, key='x2_fixed')
    t_fixed_distance_2 = st.sidebar.number_input("Fixed Time for Distance Plot $t_2$ (s)", value=0.0, key='t2_fixed')

    # --- Simulation and Plotting ---

    # Define time and distance ranges for plotting
    t_min = 0.0  # Start time of the simulation
    # Determine the max time based on the lower frequency for at least one full cycle
    try:
        f_min = min(f1, f2)
        if f_min <= 0:
            t_max = 1.0
        else:
            # Plot for 2 cycles of the slowest wave
            t_max = 2.0 / f_min
    except:
        t_max = 1.0  # Fallback

    c = 3e8  # Speed of light
    x_min = 0.0  # Start distance of the simulation
    # The max distance corresponds to the distance light travels in t_max
    x_max = c * t_max

    # Create an array of time values for plotting
    time = np.linspace(t_min, t_max, 500)  # Use linspace for a fixed number of points

    # Create an array of distance values for plotting
    distance = np.linspace(x_min, x_max, 500)

    # --- Time Domain Calculation ---
    # Signal 1 and 2 at the fixed distance points (x_fixed_time, x_fixed_time_2) over time
    signal1_time = sinusoidal_signal(A1, f1, phi1, time, x_fixed_time)
    signal2_time = sinusoidal_signal(A2, f2, phi2, time, x_fixed_time_2)
    sum_time = signal1_time + signal2_time

    # --- Distance Domain Calculation ---
    # Signal 1 and 2 at the fixed time points (t_fixed_distance, t_fixed_distance_2) over distance
    signal1_distance = sinusoidal_signal(A1, f1, phi1, t_fixed_distance, distance)
    signal2_distance = sinusoidal_signal(A2, f2, phi2, t_fixed_distance_2, distance)
    sum_distance = signal1_distance + signal2_distance

    # --- Plotting ---

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Time Domain Plot
    ax1.plot(time, signal1_time, 'r-', label='$D_1$')
    ax1.plot(time, signal2_time, 'b-', label='$D_2$')
    ax1.plot(time, sum_time, 'g-', label='Sum ($D_1 + D_2$)', linewidth=2)
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude (V)')
    ax1.set_title(f'Time Domain Signal Interference (at $x_1={x_fixed_time}$m, $x_2={x_fixed_time_2}$m)')
    ax1.legend()
    ax1.grid(True)

    # Distance Domain Plot
    ax2.plot(distance, signal1_distance, 'r-', label='$D_1$')
    ax2.plot(distance, signal2_distance, 'b-', label='$D_2$')
    ax2.plot(distance, sum_distance, 'g-', label='Sum ($D_1 + D_2$)', linewidth=2)
    ax2.set_xlabel('Distance (m)')
    ax2.set_ylabel('Amplitude (V)')
    ax2.set_title(f'Distance Domain Signal Interference (at $t_1={t_fixed_distance}$s, $t_2={t_fixed_distance_2}$s)')
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()  # Adjust the layout of the plot to prevent overlapping of the subplots

    st.header("Simulation Results")
    st.pyplot(fig)  # Display the Matplotlib figure in Streamlit

    # --- Summary of Results ---
    st.markdown("---")
    st.subheader("Signal Value at Fixed Points")

    # Calculate and display the instantaneous value of the summed signal
    # We'll use the user-defined fixed time/distance for this

    # We need a single time and single distance for the final value.
    t_instant = t_fixed_distance
    x_instant = x_fixed_time

    val1 = sinusoidal_signal(A1, f1, phi1, t_instant, x_instant)
    val2 = sinusoidal_signal(A2, f2, phi2, t_instant, x_instant)
    val_sum = val1 + val2

    st.markdown(f"""
    At **$t={t_instant}$ seconds** and **$x={x_instant}$ meters**:
    * Signal $D_1$ Value: **{val1:.4f} V**
    * Signal $D_2$ Value: **{val2:.4f} V**
    * Sum ($D_1 + D_2$) Value: **{val_sum:.4f} V**
    """)


if __name__ == "__main__":
    main()
