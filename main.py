from scapy import *
from scapy.layers.l2 import ARP


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('PyCharm')
    ARP()



