import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load RTT data from CSV
#df = pd.read_csv("uct_lab_tcp_rtt_analysis.csv")
#df = pd.read_csv("rtt_focus_1-14-apr-2024.csv")
df = pd.read_csv("yahoo_tcp_rtt.csv")


# Replace 'rtt' with your actual column name if different
latency = df['tcp.analysis.ack_rtt'].dropna() * 1000  # Convert to milliseconds

#data cleaning
latency_clean = latency[(latency > 0) & (latency <= 5000)]

# Plot histogram with CDF
fig, ax1 = plt.subplots(figsize=(8,5))

# Histogram
counts, bins, patches = ax1.hist(latency_clean, bins=60, density=True, alpha=0.6,
                                 color="steelblue", edgecolor="black")
ax1.set_xlabel("RTT (ms)")
ax1.set_ylabel("Density (Histogram)", color="steelblue")

ax1.set_xlim(0, 300)

ax1.set_xticks(np.arange(0, 300, 50))  # x-axis ticks every 50 ms

# CDF
ax2 = ax1.twinx()
ax2.plot(bins[1:], np.cumsum(counts)/np.sum(counts), color="darkred", linewidth=2)
ax2.set_ylabel("Cumulative Probability (CDF)", color="darkred")
ax2.set_ylim(0, 1.05)

plt.title("TCP RTT Histogram with Cumulative Distribution Function")
plt.grid(True)
plt.tight_layout()


plt.show()