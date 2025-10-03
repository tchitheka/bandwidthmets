import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("packet_loss_wan_lan.csv")

# WAN subset
wan = df[df["type"] == "WAN"]["loss_percent"].values
wan_sorted = np.sort(wan)
wan_cdf = np.arange(1, len(wan_sorted)+1) / len(wan_sorted)

# LAN subset
lan = df[df["type"] == "LAN"]["loss_percent"].values
lan_sorted = np.sort(lan)
lan_cdf = np.arange(1, len(lan_sorted)+1) / len(lan_sorted)

# Plot
plt.figure(figsize=(8,6))
plt.plot(wan_sorted, wan_cdf, label="WAN Traffic", color="red", linestyle="-")
plt.plot(lan_sorted, lan_cdf, label="LAN Traffic", color="blue", linestyle="--")

plt.xlabel("Packet Loss (%)")
plt.ylabel("Cumulative Probability")
plt.title("CDF of Packet Loss (WAN vs LAN)")
plt.legend()
plt.grid(True)
plt.show()
