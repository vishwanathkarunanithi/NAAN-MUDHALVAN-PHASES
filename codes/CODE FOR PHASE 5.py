# Structural Health Monitoring Using Vibration
import numpy as np
from scipy.signal import welch
import matplotlib.pyplot as plt

# Analyze vibration using Welch's method
def analyze_vibration(signal, sampling_rate):
    f, Pxx = welch(signal, fs=sampling_rate)
    return f, Pxx

# Structural Health Monitoring Class
class StructuralHealthMonitor:
    def __init__(self, sampling_rate):
        self.sampling_rate = sampling_rate

    def monitor(self, data):
        f, Pxx = analyze_vibration(data, self.sampling_rate)
        plt.plot(f, Pxx)
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Power Spectral Density (PSD)")
        plt.title("Power Spectral Density Analysis")
        plt.show()

# Example Usage
sampling_rate = 100  # Sampling rate in Hz
signal = np.random.normal(0, 1, 1000)  # Generate random signal
monitor = StructuralHealthMonitor(sampling_rate)
monitor.monitor(signal)
