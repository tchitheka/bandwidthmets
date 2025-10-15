import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# === Step 1: Load CSV without headers ===
df = pd.read_csv("rate_clean.csv",
                 sep=",", header=None, names=["timestamp", "rate_mbps"])

# === Step 2: Ensure numeric columns and drop invalid rows ===
df["timestamp"] = pd.to_numeric(df["timestamp"], errors="coerce")
df["rate_mbps"] = pd.to_numeric(df["rate_mbps"], errors="coerce")
df = df.dropna(subset=["timestamp", "rate_mbps"])

# Optional: remove unrealistic timestamps
df = df[df["timestamp"] > 1_000_000]  # keep reasonable Unix times

# === Step 2b: Filter rates to a maximum of 1 Mbps ===
df = df[df["rate_mbps"] <= 2.0]

# === Step 3: Convert timestamp to datetime ===
# Detect if timestamp is in seconds or milliseconds
if df["timestamp"].max() > 1e12:
    df["time"] = pd.to_datetime(df["timestamp"], unit="ms")
else:
    df["time"] = pd.to_datetime(df["timestamp"], unit="s")

# === Step 4: Prepare CDF ===
sorted_rate = np.sort(df["rate_mbps"])
cdf = np.arange(len(sorted_rate)) / float(len(sorted_rate))

# === Step 5: Plot side-by-side ===
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Left: Rate vs Time
axes[0].plot(df["time"], df["rate_mbps"], lw=1, color="steelblue")
axes[0].set_xlabel("Time")
axes[0].set_ylabel("Rate (Mbps)")
plt.setp(axes[0].xaxis.get_majorticklabels(), rotation=45, ha="right")
axes[0].set_title("Instantaneous Outbound Rate Over Time")
axes[0].grid(True)

# Right: CDF as scatter plot
axes[1].scatter(sorted_rate, cdf, color="darkorange", s=10)
axes[1].set_xlabel("Rate (Mbps)")
axes[1].set_ylabel("Cumulative Probability")
axes[1].set_title("CDF of Throughput")
axes[1].grid(True)

plt.tight_layout()
plt.show()
