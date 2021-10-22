cast = ["unicast", "multicast"]
available = ["globally unique(OUI enforced)", "locally administered"]

def mac2int(mac):
    return [int(x, 16) for x in mac.split(":")]

def int2mac(addr):
    return ":".join([hex(x)[2:].zfill(2) for x in addr])

def parser(mac):
    mac_addr = mac2int(mac)
    oui = mac_addr[:3]
    nic_specific = mac_addr[3:]

    print("[+] MAC address:", mac)
    print("    OUI:", int2mac(oui))
    print("       -", cast[oui[0]&1])
    print("       -", available[oui[0]>>1&1])
    print("    NIC specific:", int2mac(nic_specific))
    return

macs = ["82:95:e9:09:c0:04", "a4:83:e7:21:86:b3", "14:1c:4e:fa:46:a2", "7a:32:ea:17:a0:84", "00:15:5d:e8:b8:33"]
for mac in macs:
    parser(mac)
