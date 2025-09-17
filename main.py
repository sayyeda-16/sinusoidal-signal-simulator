# Import the NumPy library for numerical operations
import numpy as np
# Import the MatplotLib library for plotting
import matplotlib.pyplot as plt


# Define a function to calculate the value of a sinusoidal function signal at a given time(t) and distance(x) based on the parameters of a sine wave
def sinusoidal_signal(A, f, phi, t, x): # The parameters A, f, phi, t, x are passed to the function and denote the amplitude, frequency, phase shift, time, and distance of the sine wave respectively

    # Calculate the angular frequency of the sine wave
    omega = 2 * np.pi * f
    # Calculate the wave number of the sine wave
    k = 2 * np.pi * f / 3e8
    # Return the value of the sine wave at the given time(t) and distance(x)
    return A * np.sin(k * x - omega * t + phi)

# Define the main function
def main():
    # Welcome message explaining the program to the user
    print("\nWelcome to the Sinusoidal Signal Interference Simulator!")
    print("\nThis program simulates the interference of two sinusoidal signals in both time and distance domains.")
    print("\nYou will be prompted to enter the parameters for each signal.")
    
    # Get input parameters for signal 1. All values are type float.
    A1 = float(input("Enter amplitude for signal D1 in volts: "))
    f1 = float(input("Enter the fundamental frequency for signal D1 in Hz: "))
    phi1 = float(input("Enter phase for signal D1 in radians: "))
    t1 = float(input("Enter time for signal D1 in seconds: "))
    x1 = float(input("Enter distance for signal D1 in meters: "))

    # Get input parameters for signal 2
    A2 = float(input("\nEnter amplitude for signal D2 in volts: "))
    f2 = float(input("Enter the fundamental frequency for signal D2 in Hz: "))
    phi2 = float(input("Enter phase for signal D2 in radians: "))
    t2 = float(input("Enter time for signal D2 in seconds: "))
    x2 = float(input("Enter distance for signal D2 in meters: "))

    # Beginning Simulation Message
    print("\nBeginning Simulation...You may need to refresh your output screen to see the plot.")

    # Define time and distance ranges for plotting
    t_min = 0.0 # Start time of the simulation
    t_max = 1.0 / min(f1, f2)  # End time of the simulation
    x_min = 0.0 # Start distance of the simulation
    x_max = 3e8 * t_max # End distance of the simulation

    # Create an array of time values from t_min to t_max with a step size of 0.01
    time = np.arange(t_min, t_max, 0.01)
    # Calculate the distance corresponding to each time value, assuming the speed of light is 3e8 m/s
    distance = 3e8 * time  

    # Calculate the time domain signal for signal 1 and 2 by calling the sinusoidal_signal function with the parameters A1, f1, phi1, time, and distance
    signal1_time = sinusoidal_signal(A1, f1, phi1, time, x1) 
    signal2_time = sinusoidal_signal(A2, f2, phi2, time, x2)
    # Calculate the sum of the time domain signals by adding the two signals
    sum_time = signal1_time + signal2_time 

    # Calculate the distance domain signal for signal 1 and 2 by calling the sinusoidal_signal function with the parameters A1, f1, phi1, time, and distance
    signal1_distance = sinusoidal_signal(A1, f1, phi1, t1, distance)
    signal2_distance = sinusoidal_signal(A2, f2, phi2, t2, distance)
    # Calculate the sum of the distance domain signals by adding the two signals
    sum_distance = signal1_distance + signal2_distance

    # Create a new figure
    plt.figure()

    # Create a subplot for the time domain signal
    plt.subplot(2, 1, 1)

    # Plot signal 1 in red, signal 2 in blue, and their sum in green
    plt.plot(time, signal1_time, 'r-', label='Signal 1')
    plt.plot(time, signal2_time, 'b-', label='Signal 2')
    plt.plot(time, sum_time, 'g-', label='Sum')

    # Label the x-axis as time, y-axis as amplitude, and set the title as Time Domain
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (V)')
    plt.title('Time Domain')

    # Show the legend for the plot
    plt.legend()

    # Create a subplot for the distance domain signal
    plt.subplot(2, 1, 2)

    # Plot signal 1 in red, signal 2 in blue, and their sum in green
    plt.plot(distance, signal1_distance, 'r-', label='Signal 1')
    plt.plot(distance, signal2_distance, 'b-', label='Signal 2')
    plt.plot(distance, sum_distance, 'g-', label='Sum')

    # Label the x-axis as distance, y-axis as amplitude, and set the title as Distance Domain
    plt.xlabel('Distance (m)')
    plt.ylabel('Amplitude (V)')
    plt.title('Distance Domain')

    # Show the legend for the plot
    plt.legend()


    plt.tight_layout() # Adjust the layout of the plot to prevent overlapping of the subplots
    plt.show() # Show the plot
    
if __name__ == "__main__": # Check if the script is being run as the main program
    main() # Call the main function