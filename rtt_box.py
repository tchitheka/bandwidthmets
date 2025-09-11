import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
""""
# Example latency dataset (in milliseconds)
latency = np.random.normal(loc=50, scale=10, size=200)  # mean=50ms, std=10ms

plt.figure(figsize=(12,5))

# --- Box Plot ---
plt.subplot(1, 2, 1)
sns.boxplot(y=latency, color="skyblue")
plt.title("Latency Box Plot")
plt.ylabel("Latency (ms)")

# --- Violin Plot ---
plt.subplot(1, 2, 2)
sns.violinplot(y=latency, color="lightgreen")
plt.title("Latency Violin Plot")
plt.ylabel("Latency (ms)")

plt.tight_layout()
plt.show()
"""

df = pd.read_csv("tcp_rtt_analysis.csv")

# Drop missing values (NaN) because not all packets have RTT
df = df.dropna(subset=["tcp.analysis.ack_rtt"])

# Convert RTT to milliseconds
df["rtt_ms"] = df["tcp.analysis.ack_rtt"] * 1000

# Plot box plot
plt.figure(figsize=(8,6))
sns.boxplot(x=df["rtt_ms"], color="skyblue")
plt.ylabel("RTT (ms)")
plt.title("TCP Latency Distribution (Box Plot)")
plt.show()
