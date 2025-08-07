# draw_pendulum.py

import numpy as np

def calculate_positions(x_base, L1, L2, theta1, theta2, i):
    """
    Calculates the positions of a double pendulum at a given time step i,
    adding a small time-varying oscillation to the angles to simulate motion.

    Parameters:
        x_base (float): The horizontal base position.
        L1 (float): Length of the first rod.
        L2 (float): Length of the second rod.
        theta1 (float): Angle of the first pendulum arm (in radians).
        theta2 (float): Angle of the second pendulum arm (in radians).
        i (int): Frame index or time step.

    Returns:
        base (tuple): Coordinates of the pendulum base.
        m1 (tuple): Coordinates of the first mass.
        m2 (tuple): Coordinates of the second mass.
        theta1 (float): Updated angle of the first arm.
        theta2 (float): Updated angle of the second arm.
    """

    # Add slight oscillation to simulate dynamic movement
    theta1 = theta1 + 0.2 * np.sin(i * 0.1)
    theta2 = theta2 + 0.2 * np.cos(i * 0.1)

    # First pendulum mass position
    x1 = x_base + L1 * np.sin(theta1)
    y1 = -L1 * np.cos(theta1)

    # Second pendulum mass position
    x2 = x1 + L2 * np.sin(theta2)
    y2 = y1 - L2 * np.cos(theta2)

    return (x_base, 0), (x1, y1), (x2, y2), theta1, theta2
