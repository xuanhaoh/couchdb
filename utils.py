import os
import fcntl
import socket
import struct


def get_ip_address(if_name):
    skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    pkt_string = fcntl.ioctl(skt.fileno(), 0x8915, struct.pack('256s', bytes(if_name[:15].encode('utf-8'))))
    ip_string = socket.inet_ntoa(pkt_string[20:24])
    return ip_string

hostname = socket.gethostname()
address = get_ip_address('eth0')

with open('/home/vdb/couchdb/etc/vm.args', mode='w', encoding='utf-8') as f1:
    with open('/home/ec2-user/couchdb-master/vm.args', mode='r', encoding='utf-8') as f2:
        for line in f2.readlines():
            if line.startswith('-name'):
                line = line.rstrip() + address + '\n'
            f1.write(line)
