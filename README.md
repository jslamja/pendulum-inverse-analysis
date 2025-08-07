Pendulum Inverse Analysis Simulation Project
============================================

Overview
--------
This project performs inverse analysis on a simulated double pendulum system.
It estimates physical parameters such as pendulum lengths and angles using only the motion trajectory of the system.

Key Features:
-------------
- Simulates double pendulum motion using predefined parameters.
- Extracts motion frames as position data over time.
- Reconstructs physical quantities (L1, L2, θ1, θ2) via inverse methods.
- Provides a comparison module to evaluate the accuracy of estimated vs actual values.

Objective
---------
To evaluate how reliably inverse physics can reconstruct real physical parameters
when only motion snapshots are available, simulating real-world experimental constraints.

Comparison Module
-----------------
The `compare_inverse_to_actual()` function is used to:
- Quantify the error between estimated and true values.
- Validate the robustness of the inverse analysis process.

File Structure
--------------
- simulate_pendulum_motion(): Runs the simulation.
- extract_frame_data(): Extracts key point data.
- estimate_parameters(): Performs inverse estimation.
- compare_inverse_to_actual(): Performs error comparison.
- visualize_snapshot(): Optional function to display frame images.

How to Run
----------
1. Run the `install_requirements.py` script to install required packages:
   > python install_requirements.py

2. Then run your main analysis file (e.g., `main.py`) to generate and analyze the pendulum motion.

3. Use `compare_inverse_to_actual()` to validate the results.

Dependencies
------------
- Python 3.x
- matplotlib
- numpy

License
-------
MIT License © 2025  
You are free to use, modify, and distribute this software for academic or research purposes,
as long as proper credit is given.

Contact
-------
Author: Islam J. AbuQasem  
Email: islam.g.abuqasem@gmail.com  
See `contact.txt` for more.
