import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("throughput_latency_bins.csv")

# Optional: filter a single file or all combined
# df = df[df["file"].str.contains("example.pcap")]

# --- Plot 1: Throughput vs Avg RTT ---
plt.figure(figsize=(10,6))
plt.scatter(df["throughput_mbps"], df["avg_rtt_ms"], alpha=0.6, label="Avg RTT (ms)")
plt.xlabel("Throughput (Mbps)")
plt.ylabel("RTT (ms)")
plt.title("Throughput vs Avg RTT")
plt.legend()
plt.grid(True)
plt.show()

# --- Plot 2: Throughput vs Span RTT ---
plt.figure(figsize=(10,6))
plt.scatter(df["throughput_mbps"], df["span_rtt_ms"], alpha=0.6, color="red", label="Span RTT (ms)")
plt.xlabel("Throughput (Mbps)")
plt.ylabel("Span RTT (ms)")
plt.title("Throughput vs Queuing Delay (Span RTT)")
plt.legend()
plt.grid(True)
plt.show()

# --- Plot 3: Time series of RTT and throughput ---
plt.figure(figsize=(12,6))
plt.plot(df["bin_start"], df["throughput_mbps"], label="Throughput (Mbps)", color="blue")
plt.plot(df["bin_start"], df["avg_rtt_ms"], label="Avg RTT (ms)", color="orange")
plt.plot(df["bin_start"], df["min_rtt_ms"], label="Min RTT (ms)", color="green", linestyle="--")
plt.xlabel("Time bin (s)")
plt.ylabel("Value")
plt.title("Time Series: Throughput vs RTT")
plt.legend()
plt.grid(True)
plt.show()
