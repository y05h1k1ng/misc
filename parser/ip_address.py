def ip2int(ip):
    return list(map(int, ip.split(".")))

def int2ip(addr):
    return ".".join(map(str, addr))

def sep_net_host(addr, network_len):
    bin_addr = "".join([bin(x)[2:].zfill(8) for x in addr])
    network = bin_addr[:network_len].ljust(32, '0')
    host = bin_addr[network_len:]

    network_addr = ".".join(map(str, [int(x, 2) for x in [network[i:i+8] for i in range(0, 32, 8)]]))
    return network_addr, host

def parser(ip):
    addr, network_len = ip.split("/")
    addr = ip2int(addr)
    network_len = int(network_len)

    network_addr, host = sep_net_host(addr, network_len)
    
    print("[+] IP Address:", ip)
    print("    network address:", network_addr)
    return

ip = "192.168.34.5/28"
parser(ip)
