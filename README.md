# Rocket_script-
# Rocket Flight Simulation Using Runge-Kutta Integration

A Python-based physics simulation that models rocket flight dynamics. It utilizes the Runge-Kutta numerical integration method to calculate altitude, velocity, and telemetry logs over time, factoring in aerodynamic drag, gravity, and mass.

## Features

**Numerical Integration:** Implements algorithmic steps to solve ordinary differential equations (ODEs) for state vectors.
**Physics Modeling:** Accounts for dynamic physical variables including dry mass, cross-sectional area, and drag coefficient.
**Data Visualization:** Generates clean telemetry logs using `matplotlib` to chart altitude and velocity changes over time.

## Tech Stack
**Python 3**
**NumPy:** Used for state vector handling and fast mathematical arrays.
**Matplotlib:** Used for visualizing physics simulation outputs.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com
   ```
2. Install dependencies:
   ```bash
   pip install numpy matplotlib
   ```
3. Run the script:
   ```bash
   python runge_kutta.py
   ```
