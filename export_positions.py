# export_positions.py

import draw_pendulum
import config

def get_positions_sequence(num_frames=100):
    """
    Generates a sequence of pendulum positions for a given number of frames.
    It calculates the base and masses positions for each frame using the
    `draw_pendulum.calculate_positions` function.

    Parameters:
        num_frames (int): The number of frames to simulate and calculate.

    Returns:
        sequence (list): A list of tuples, each containing the positions of 
                         the base and two masses at each time step.
    """
    sequence = []
    for i in range(num_frames):
        # Calculate positions for the current frame
        base, m1, m2, t1, t2 = draw_pendulum.calculate_positions(
            config.x_base, config.L1, config.L2, config.theta1, config.theta2, i
        )
        # Append the positions to the sequence list
        sequence.append((base, m1, m2))
    
    return sequence
