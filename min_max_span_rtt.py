import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# 1. Load CSV
# -------------------------
df = pd.read_csv("rtt_stats.csv")

# Convert to ms
df["min_rtt"] = df["min_rtt"] * 1000
df["max_rtt"] = df["max_rtt"] * 1000
df["span"]    = df["span"] * 1000

# -------------------------
# 2. Truncate > 1000ms
# -------------------------
df = df[(df["min_rtt"] <= 1000) & (df["max_rtt"] <= 1000) & (df["span"] <= 1000)]

# -------------------------
# 3. Function to compute empirical CDF
# -------------------------
def empirical_cdf(series):
    sorted_vals = np.sort(series)
    cdf = np.arange(1, len(sorted_vals) + 1) / len(sorted_vals)
    return sorted_vals, cdf

# Compute CDFs
x_min, cdf_min = empirical_cdf(df["min_rtt"])
x_max, cdf_max = empirical_cdf(df["max_rtt"])
x_span, cdf_span = empirical_cdf(df["span"])

# -------------------------
# 4. Plot smooth curves
# -------------------------
plt.figure(figsize=(8,6))

plt.plot(x_span, cdf_span, color="green", linestyle="-", label="RTT span")
plt.plot(x_min, cdf_min, color="orange", linestyle="--", label="Minimum RTT")
plt.plot(x_max, cdf_max, color="blue", linestyle=":", label="Maximum RTT")

plt.xlabel("Milliseconds")
plt.ylabel("Cumulative probability")
plt.title("CDF of RTT Min, Max, and Span (≤ 1000ms)")
plt.xlim(0, 1000)
plt.ylim(0, 1.05)
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
