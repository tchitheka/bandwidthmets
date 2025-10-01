import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the TSV output from tshark
df = pd.read_csv("/home/takondwa/Desktop/focus/inethi_FOCUS_OV_2024-04-06_11-00-00_rtt.csv", 
                 sep='\t', names=["timestamp", "ack_rtt"], header=None)

# Ensure numeric types
df["timestamp"] = pd.to_numeric(df["timestamp"], errors='coerce')
df["ack_rtt"] = pd.to_numeric(df["ack_rtt"], errors='coerce')
df = df.dropna()

# Convert timestamps to datetime
df["datetime"] = pd.to_datetime(df["timestamp"], unit='s')

# Convert RTT to milliseconds
df["ack_rtt_ms"] = df["ack_rtt"] * 1000

# Bin timestamps into 1-second intervals
df["time_bin"] = df["datetime"].dt.floor("1S")  # floor to nearest second

# Compute span RTT per 1-second bin
binned = df.groupby("time_bin")["ack_rtt_ms"].agg(lambda x: x.max() - x.min()).reset_index()
binned.rename(columns={"ack_rtt_ms": "span_rtt_ms"}, inplace=True)

# Normalize span RTT to 0-1 range
binned["span_rtt_norm"] = (binned["span_rtt_ms"] - binned["span_rtt_ms"].min()) / \
                          (binned["span_rtt_ms"].max() - binned["span_rtt_ms"].min())

# Plot
plt.figure(figsize=(12,5))
plt.plot(binned["time_bin"], binned["span_rtt_norm"], color="green", label="Normalized Span RTT")
plt.xlabel("Time")
plt.ylabel("Normalized Span RTT")
plt.title("Outbound Span RTT over Time (1s bins)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
