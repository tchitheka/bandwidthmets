import pyshark
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import glob
import os

# === CONFIGURATION ===
PCAP_DIR = "./pcap_files"        # Folder containing .pcap files
OUTPUT_CSV = "loss_rates.csv"    # Where to save summary data
OUTPUT_DIR = "./plots"           # Folder for plots
os.makedirs(OUTPUT_DIR, exist_ok=True)

# === PROCESS ALL PCAP FILES ===
pcap_files = glob.glob(os.path.join(PCAP_DIR, "*.pcap"))
loss_rates = []

print(f"Found {len(pcap_files)} pcap files in {PCAP_DIR}")

for file in pcap_files:
    print(f"\nProcessing {file} ...")

    # Use display_filter to load only TCP packets
    cap = pyshark.FileCapture(file, display_filter="tcp", keep_packets=False)

    total_tcp = 0
    retransmissions = 0
    flows = {}

    try:
        for pkt in cap:
            total_tcp += 1
            src = pkt.ip.src
            dst = pkt.ip.dst
            sport = pkt.tcp.srcport
            dport = pkt.tcp.dstport
            flow_id = (src, dst, sport, dport)

            if flow_id not in flows:
                flows[flow_id] = {'total': 0, 'retrans': 0}

            flows[flow_id]['total'] += 1

            if hasattr(pkt.tcp, 'analysis_retransmission'):
                flows[flow_id]['retrans'] += 1
                retransmissions += 1

    except KeyboardInterrupt:
        print("Processing interrupted by user.")
        break
    except Exception as e:
        print(f"Error while processing {file}: {e}")

    finally:
        cap.close()

    # Calculate loss rates per flow
    for flow, stats in flows.items():
        total = stats['total']
        retrans = stats['retrans']
        loss_rate = retrans / total if total > 0 else 0
        loss_rates.append({
            'pcap_file': os.path.basename(file),
            'src': flow[0],
            'dst': flow[1],
            'sport': flow[2],
            'dport': flow[3],
            'loss_rate': loss_rate
        })

# === SAVE RESULTS ===
df = pd.DataFrame(loss_rates)
df.to_csv(OUTPUT_CSV, index=False)
print(f"\n✅ Saved summary to {OUTPUT_CSV}")
print(df['loss_rate'].describe())

# === PLOTS ===
sns.set_style("whitegrid")

# PDF
plt.figure(figsize=(10,4))
sns.kdeplot(df['loss_rate'], bw_adjust=0.5, color='blue')
plt.title("PDF of Loss Packet Rate of TCP Flows")
plt.xlabel("Loss Rate")
plt.ylabel("PDF")
plt.tight_layout()
pdf_path = os.path.join(OUTPUT_DIR, "pdf_loss_rate.png")
plt.savefig(pdf_path)
plt.show()
print(f"Saved PDF plot to {pdf_path}")

# CDF
plt.figure(figsize=(10,4))
sns.ecdfplot(df['loss_rate'], color='green')
plt.title("CDF of Loss Packet Rate of TCP Flows")
plt.xlabel("Loss Rate")
plt.ylabel("Cumulative Probability")
plt.tight_layout()
cdf_path = os.path.join(OUTPUT_DIR, "cdf_loss_rate.png")
plt.savefig(cdf_path)
plt.show()
print(f"Saved CDF plot to {cdf_path}")

