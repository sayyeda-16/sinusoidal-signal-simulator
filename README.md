# Sinusoidal Signal Interference Simulator

This project is a Python application that simulates the interference of two sinusoidal signals in both the time and distance domains, featuring an **interactive web UI built with Streamlit**. It demonstrates effective use of Python for scientific computing, data visualization, and building accessible, data-driven applications.

***

### Project Description

The application uses the **NumPy** library for efficient numerical calculations and **Matplotlib** for generating the simulation plots. The plots are seamlessly embedded into a user-friendly web interface via **Streamlit**.

Key features include:
* **Interactive Web UI**: All signal parameters (Amplitude, Frequency, Phase, Fixed Time/Distance) are entered via a sidebar in the web application, allowing for real-time adjustments and simulation updates.
* **Real-time Visualization**: The plots for individual signals and their resulting sum are updated instantly as the user modifies any input parameter.
* **Dual Domain Simulation**: It calculates and plots the signal interference in both the **Time Domain** (Signal vs. Time) and the **Distance Domain** (Signal vs. Distance).
* **Problem-Solving**: The project team initially planned to use C++ but transitioned to Python with Streamlit to overcome challenges with C++ plotting library setup, demonstrating adaptability and effective problem-solving skills in delivering a functional UI.

***

### Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Python 3** | Core programming language |
| **Streamlit** | Building the interactive web user interface |
| **NumPy** | Efficient numerical array calculations |
| **Matplotlib** | Generating the 2D plots for visualization |

***

### Installation

To run this application, you will need to have Python 3 installed on your system.

1.  Clone this repository or download the `signal_simulator.py` file.
2.  Install the necessary libraries by running the following command in your terminal:
    ```bash
    pip install streamlit numpy matplotlib
    ```

***

### Usage

The application is run as a Streamlit server, making it accessible through your web browser.

1.  Navigate to the directory containing the `main.py` file.
2.  Run the application from your terminal:
    ```bash
    streamlit run main.py
    ```
3.  A web browser tab will automatically open, displaying the application.
4.  Use the **sidebar inputs** to adjust the parameters for Signal 1 and Signal 2. The plots will update in real-time to show the interference results.

***

### Screenshots
<img width="2559" height="1244" alt="image" src="https://github.com/user-attachments/assets/16e90ff7-6834-4f30-9e46-80da13d57e28" />
<img width="2559" height="1180" alt="image" src="https://github.com/user-attachments/assets/90f8d1a8-a2fc-4fc5-af36-597f840ce80f" />



*A typical view of the application, showing the interactive sidebar and the dual-domain plots.*
