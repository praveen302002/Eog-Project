import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load CSV files
def load_csv_files(file_paths):
    signals = []
    for file_path in file_paths:
        # Skip metadata rows (first 8 rows) and specify column names
        df = pd.read_csv(file_path, delimiter=',', skiprows=8, names=['Time', 'Channel_3', 'Channel_4'])  
        signal_values = df[['Channel_3', 'Channel_4']].values  # Extract signal values from specific columns
        signals.append(signal_values)  
    return signals

# Step 2: Combine the signals
def combine_signals(signals):
    combined_signal = np.sum(signals, axis=0)  # Summing the signals instead of taking the mean
    return combined_signal

# Step 3: Visualize the results
def visualize_results(combined_signal):
    plt.figure(figsize=(10, 6))
    plt.plot(combined_signal[:, 0], label='Channel 3')  # Plotting Channel 3
    plt.plot(combined_signal[:, 1], label='Channel 4')  # Plotting Channel 4
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Combined EOG Signals')
    plt.legend()
    plt.show()

# Main function
def main():
    # Step 1: Load CSV files
    file_paths = ["signal11.csv", "signal57.csv"]  # Example file paths, replace with your actual file paths
    signals = load_csv_files(file_paths)

    # Step 2: Combine the signals
    combined_signal = combine_signals(signals)

    # Step 3: Visualize the results
    visualize_results(combined_signal)

if  __name__ == "__main__":
     main()