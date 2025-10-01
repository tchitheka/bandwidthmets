import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load RTT per packet
df = pd.read_csv("rtt_per_packet.tsv", sep="\t",
                 names=["src","srcport","dst","dstport","rtt"])

# Filter RTTs ≤ 1000 ms
df = df[df["rtt"] <= 1000]

# Define connection as 4-tuple
df['flow'] = df['src'] + ":" + df['srcport'].astype(str) + "->" + df['dst'] + ":" + df['dstport'].astype(str)

# Compute stddev of RTT per flow
stddevs = df.groupby('flow')['rtt'].std().dropna()

# Sort for empirical CDF
sorted_vals = np.sort(stddevs)
cdf = np.arange(1, len(sorted_vals)+1) / len(sorted_vals)

# Plot
plt.figure(figsize=(7,5))
plt.plot(sorted_vals, cdf, color="black")
plt.xscale("log")
plt.xlabel("Std. Dev. (ms)")
plt.ylabel("Empirical distribution")
plt.title("CDF of RTT Standard Deviation per Connection (RTTs ≤ 1000 ms)")
plt.grid(True, which="both", ls="--")
plt.show()
