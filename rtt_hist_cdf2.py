import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_latency_analysis(csv_file):
    """
    Reads a CSV file, plots a histogram and a Cumulative Distribution Function (CDF).
    
    Args:
        csv_file (str): The path to the CSV file containing latency data.
    """
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)
        
        # Assume the column with RTT data is named 'tcp.analysis.ack_rtt' based on the tshark command
        rtt_data = df['tcp.analysis.ack_rtt'].dropna()

        if rtt_data.empty:
            print("No valid RTT data found in the CSV file. Please check the tshark command and the pcap file.")
            return

        # Create a figure with two subplots side-by-side
        fig, axes = plt.subplots(1, 2, figsize=(14, 6))
        fig.suptitle('Latency Analysis: Histogram and CDF', fontsize=16)

        # Plot the Histogram on the first subplot
        axes[0].hist(rtt_data, bins=50, color='skyblue', edgecolor='black')
        axes[0].set_title('Histogram of RTT')
        axes[0].set_xlabel('Round-Trip Time (seconds)')
        axes[0].set_ylabel('Frequency')
        axes[0].grid(axis='y', alpha=0.75)

        # Plot the CDF on the second subplot
        sorted_data = np.sort(rtt_data)
        y_vals = np.arange(1, len(sorted_data) + 1) / len(sorted_data)
        axes[1].plot(sorted_data, y_vals, marker='.', linestyle='none', color='orange')
        axes[1].set_title('CDF of RTT')
        axes[1].set_xlabel('Round-Trip Time (seconds)')
        axes[1].set_ylabel('Cumulative Probability')
        axes[1].grid(True)
        
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{csv_file}' was not found.")
    except KeyError:
        print(f"Error: The column 'tcp.analysis.ack_rtt' was not found in the CSV file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# To run the function, call it with your CSV file name
if __name__ == '__main__':
    plot_latency_analysis('uct_lab_tcp_rtt_analysis2.csv')