import pyshark
import random as rand

def monitor_network(target_sys):
    rand_ip_addrs = ['10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.5'
                     '10.0.0.6', '10.0.0.7', '10.0.0.8', '10.0.0.9', '10.0.0.245']
    
    # Analyze outgoing packets from local host
    capture = pyshark.LiveCapture(interface='Wi-Fi')
    for packet in capture.sniff_continuously():
        src_ip = packet.ip.src
        dest_ip = packet.ip.dst
        print(f"Received packet from {src_ip} to {dest_ip}")
        
        new_src_ip = target_sys['ip']
        new_dest_ip = rand_ip_addrs[rand.randint(0, 9)]
        print(f"New dummy packet information:\nNew Source IP: {new_src_ip}\nNew Destination IP: {new_dest_ip}")
        
        check_whitelist(target_sys, new_dest_ip)
        
        if new_dest_ip == '10.0.0.3':
            print(f"{new_dest_ip}  == 10.0.0.3")
            break
        
        
def check_whitelist(host, dest_ip):
    print(host['whitelist'])