import pandas as pd
import matplotlib.pyplot as plt

# Load tshark output
df = pd.read_csv("retransmissions.tsv", sep="\t", names=["time_epoch", "src", "dst", "seq", "retrans"])

# Convert time to seconds (integer) for binning
df['time_bin'] = df['time_epoch'].astype(float).astype(int)

# Count retransmissions per second
retrans_per_sec = df.groupby('time_bin').size()

# Plot time series
plt.figure(figsize=(12,5))
plt.plot(retrans_per_sec.index, retrans_per_sec.values, marker='o')
plt.xlabel("Time (s)")
plt.ylabel("TCP Retransmissions per second")
plt.title("TCP Retransmissions Over Time")
plt.grid(True)
plt.show()