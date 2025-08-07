import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from export_positions import get_positions_sequence
from inverse_analysis import estimate_parameters
import draw_pendulum
import numpy as np

class PendulumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Double Pendulum Visualizer")

        # Memory to store previous frames
        self.sequence_memory = []

        # Input Section
        self.frame_input = ttk.LabelFrame(root, text="1. Enter Real Parameters")
        self.frame_input.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        # Plot Section
        self.frame_plot = ttk.LabelFrame(root, text="2. Animation Snapshot")
        self.frame_plot.grid(row=0, column=1, padx=10, pady=10)

        # Output Section
        self.frame_output = ttk.LabelFrame(root, text="3. Inverse Estimated Parameters")
        self.frame_output.grid(row=0, column=2, padx=10, pady=10, sticky="n")

        # Comparison Section
        self.frame_compare = ttk.LabelFrame(root, text="4. Comparison & Comments")
        self.frame_compare.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

        # Input fields
        self.inputs = {}
        for i, key in enumerate(["x_base", "L1", "L2", "theta1", "theta2"]):
            ttk.Label(self.frame_input, text=key).grid(row=i, column=0, sticky="e")
            entry = ttk.Entry(self.frame_input)
            entry.grid(row=i, column=1)
            entry.bind("<KeyRelease>", lambda event: self.update_plot())  # Live update on key release
            self.inputs[key] = entry

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots(figsize=(4, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame_plot)
        self.canvas.get_tk_widget().pack()

        # Output area
        self.output_text = tk.Text(self.frame_output, height=15, width=40)
        self.output_text.pack()

        # Comparison area
        self.compare_text = tk.Text(self.frame_compare, height=10, width=120)
        self.compare_text.pack()

    def update_plot(self):
        try:
            # Read real (input) parameters
            real_params = {
                "x_base": float(self.inputs["x_base"].get()),
                "L1": float(self.inputs["L1"].get()),
                "L2": float(self.inputs["L2"].get()),
                "theta1": float(self.inputs["theta1"].get()),
                "theta2": float(self.inputs["theta2"].get()),
            }
        except ValueError:
            return  # Skip update if input is invalid

        # Calculate positions
        self.ax.clear()
        base, m1, m2, _, _ = draw_pendulum.calculate_positions(
            real_params["x_base"], real_params["L1"], real_params["L2"],
            real_params["theta1"], real_params["theta2"], i=0
        )

        # Save snapshot to memory
        self.sequence_memory.append((base, m1, m2))

        # Plot the pendulum
        self.ax.plot([base[0], m1[0]], [base[1], m1[1]], 'b-', linewidth=3)
        self.ax.plot([m1[0], m2[0]], [m1[1], m2[1]], 'g-', linewidth=3)
        self.ax.plot(m1[0], m1[1], 'bo')
        self.ax.plot(m2[0], m2[1], 'go')
        self.ax.set_xlim(-5, 5)
        self.ax.set_ylim(-5, 1)
        self.ax.grid()
        self.ax.set_title("Double Pendulum Snapshot")
        self.canvas.draw()

        # Estimate inverse parameters
        estimated = estimate_parameters(self.sequence_memory)

        # Display estimated values
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"📸 Number of Frames: {estimated['num_frames']}\n\n")
        for key, value in estimated.items():
            if key != 'num_frames' and not key.endswith("_std"):
                std = estimated.get(f"{key}_std", 0)
                self.output_text.insert(tk.END, f"{key}: {value:.4f} ± {std:.4f}\n")

        # Compare with real values
        self.compare_text.delete(1.0, tk.END)
        self.compare_text.insert(tk.END, "📊 Comparison Between Real & Estimated Parameters:\n\n")
        for key in real_params:
            est_value = estimated.get(key, None)
            std = estimated.get(f"{key}_std", None)
            if est_value is not None:
                diff = abs(real_params[key] - est_value)
                percent_error = 100 * diff / (abs(real_params[key]) + 1e-8)
                comment = "✅ Accurate" if percent_error < 5 else "⚠️ Needs Review"
                self.compare_text.insert(
                    tk.END,
                    f"{key}: Real = {real_params[key]:.4f}, Estimated = {est_value:.4f} ± {std:.4f} → Δ = {diff:.4f} ({percent_error:.2f}%) {comment}\n"
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = PendulumApp(root)
    root.mainloop()
