import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------
# 1. Load Argus export
# -------------------
df = pd.read_csv("yahootcprtt2.csv")
print("Columns in dataset:", df.columns)

# -------------------
# 2. Extract valid tcprtt values (convert to ms)
# -------------------
tcprtt_ms = df["tcprtt"].dropna() * 1000
tcprtt_ms = tcprtt_ms[tcprtt_ms > 0]  # filter out non-positive values

print(f"Flows analyzed: {len(tcprtt_ms)}")
print(f"Min RTT: {tcprtt_ms.min():.2f} ms")
print(f"Max RTT: {tcprtt_ms.max():.2f} ms")

# -------------------
# 3. Build CDF
# -------------------
sorted_rtt = np.sort(tcprtt_ms)
cdf = np.arange(1, len(sorted_rtt)+1) / len(sorted_rtt)

# -------------------
# 4. Plot single CDF
# -------------------
plt.figure(figsize=(8,6))

plt.plot(sorted_rtt, cdf, color="blue", label="TCP RTT")

plt.xlabel("Milliseconds")
plt.ylabel("Cumulative probability")
plt.title("CDF of TCP RTT (per flow)")
plt.grid(True, linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.show()
