import numpy as np
import matplotlib.pyplot as plt

# Simulated vibration data
time = np.linspace(0, 10, 1000)
vibration = np.sin(2 * np.pi * 5 * time) + np.random.normal(0, 0.5, 1000)

# Threshold for anomaly detection
threshold = 1.5
anomalies = np.where(np.abs(vibration) > threshold)[0]

plt.plot(time, vibration, label="Vibration Signal")
plt.scatter(time[anomalies], vibration[anomalies], color='red', label='Anomalies')
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Structural Vibration Monitoring")
plt.legend()
plt.show()
