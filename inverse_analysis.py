import numpy as np

def estimate_parameters(sequence):
    """
    Takes multiple snapshots (base and mass positions), calculates the average to estimate the parameters.

    Parameters:
        sequence (list): A list of tuples containing the positions of the base and two masses.

    Returns:
        dict: A dictionary containing the estimated parameters and their standard deviations.
    """
    if len(sequence) == 0:
        return {"error": "No data in sequence"}

    # Initialize results dictionary to store values for each parameter
    results = {
        "x_base": [],
        "L1": [],
        "theta1": [],
        "L2": [],
        "theta2": []
    }

    # Iterate over all the snapshots in the sequence to calculate parameters
    for base, m1, m2 in sequence:
        # Calculate the distance and angle for the first pendulum
        x_base = base[0]
        dx1 = m1[0] - x_base
        dy1 = m1[1]
        L1 = np.hypot(dx1, dy1)
        theta1 = np.arctan2(dx1, -dy1)

        # Calculate the distance and angle for the second pendulum
        dx2 = m2[0] - m1[0]
        dy2 = m2[1] - m1[1]
        L2 = np.hypot(dx2, dy2)
        theta2 = np.arctan2(dx2, -dy2)

        # Append calculated values to the results
        results["x_base"].append(x_base)
        results["L1"].append(L1)
        results["theta1"].append(theta1)
        results["L2"].append(L2)
        results["theta2"].append(theta2)

    # Prepare a summary of the results, including the average and standard deviation
    summary = {
        "num_frames": len(sequence),  # Number of frames used
    }

    # Calculate the mean and standard deviation for each parameter
    for key in results:
        values = np.array(results[key])
        summary[key] = round(np.mean(values), 3)
        summary[key + "_std"] = round(np.std(values), 4)  # Optional: Standard deviation

    return summary
