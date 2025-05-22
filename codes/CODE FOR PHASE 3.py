import numpy as np
import matplotlib.pyplot as plt

# Simulated vibration data
time = np.linspace(0, 10, 500)
vibration = np.sin(time) + np.random.normal(0, 0.1, len(time))
vibration[300:310] += 3  # Simulated anomaly

# Threshold for anomaly detection
threshold = 2.0
anomalies = np.where(np.abs(vibration) > threshold)[0]

# Plotting the data
plt.figure(figsize=(10, 4))
plt.plot(time, vibration, label='Vibration Signal')
plt.scatter(time[anomalies], vibration[anomalies], color='red', label='Anomaly')
plt.axhline(y=threshold, color='gray', linestyle='--')
plt.axhline(y=-threshold, color='gray', linestyle='--')
plt.title("Structural Vibration Monitoring")
plt.xlabel("Time (s)")
plt.ylabel("Vibration Amplitude")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()