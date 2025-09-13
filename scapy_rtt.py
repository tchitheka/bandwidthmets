from scapy.all import rdpcap, TCP

packets = rdpcap("uct_lab.pcap")
sent_times = {}
rtts = []

for pkt in packets:
    if TCP in pkt:
        tcp = pkt[TCP]
        if tcp.flags & 0x18:  # PSH or ACK (data packet)
            sent_times[tcp.seq] = pkt.time
        if tcp.flags & 0x10:  # pure ACK
            ack_seq = tcp.ack
            if ack_seq-1 in sent_times:
                rtt = (pkt.time - sent_times[ack_seq-1]) * 1000  # convert to ms
                rtts.append(rtt)

print("Extracted RTT samples (ms):", rtts[:20])