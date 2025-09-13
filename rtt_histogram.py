import pandas as pd
import matplotlib.pyplot as plt

def plot_latency_histogram(csv_file_path):
    """
    Reads a CSV file containing latency data and plots a histogram.

    Args:
        csv_file_path (str): The path to the CSV file.
    """
    try:
        # Read the CSV file into a pandas DataFrame.
        # The column name is assumed to be 'tcp.analysis.ack_rtt' based on the tshark output.
        df = pd.read_csv("rtt_focus_1-14-apr-2024.csv")

        # Check if the required column exists
        if 'tcp.analysis.ack_rtt' not in df.columns:
            print("Error: 'tcp.analysis.ack_rtt' column not found in the CSV file.")
            print("Available columns:", df.columns.tolist())
            return

        # Extract the latency data and drop any rows with missing values
        latency_data = df['tcp.analysis.ack_rtt'].dropna() 
        latency_data = latency_data *1000


        if latency_data.empty:
            print("No valid latency data found in the CSV file after cleaning.")
            return

        # Create a histogram of the latency data
        plt.figure(figsize=(10, 6))
        plt.hist(latency_data, bins=50, color='skyblue', edgecolor='black', alpha=0.7)

        # Set the title and labels for the plot
        plt.title('Distribution of TCP RTT (Latency)', fontsize=16)
        plt.xlabel('Round-Trip Time (ms)', fontsize=12)
        plt.ylabel('Frequency', fontsize=12)

        # Add a grid for better readability
        plt.grid(axis='y', alpha=0.75)

        # Display the plot
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage: Replace 'your_rtt_data.csv' with the actual file name.
if __name__ == '__main__':
    plot_latency_histogram('yrtt_focus_1-14-apr-2024.csv')
