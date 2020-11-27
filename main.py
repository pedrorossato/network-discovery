import time
import argparse
from macSearch import MacSearch
from network_scanner import NetworkScanner
from writer import Writer
from dispositivo import Dispositivo


def analisaArgs():
    parser = argparse.ArgumentParser(description='--help para mais infos.')
    parser.add_argument('--ip',
                        metavar='i',
                        type=str,
                        help='Recebe o IP.',
                        required=False)
    parser.add_argument('--time',
                        metavar='t',
                        type=float,
                        help='O intervalo de tempo entre scans.',
                        required=True)
    return parser.parse_args()


def analisaDispositivos(clients):
    macSearch = MacSearch()
    dispositivos = []
    for client in clients:
        dispositivos.append(Dispositivo(ip=client['ip'],
                                        mac=client['mac'],
                                        fabricante=macSearch.getFabricante(
                                            client['mac']),
                                        isHost=False))
    return dispositivos


def comparaDispositivos(dispositivos, csv_dispositivos, ip_router):
    for dispositivo in dispositivos:
        if (any(d.mac == dispositivo.mac for d in csv_dispositivos)):
            dispositivo.status = "Online"
        else:
            dispositivo.status = "Novo"
        if (dispositivo.ip.strip() == ip_router.strip()):
            dispositivo.status = "Router"
    return list(set(dispositivos + csv_dispositivos))


def mostraDispositivos(dispositivos):
    for dispositivo in dispositivos:
        print(dispositivo)


def checaIPnosArgumentos(args):
    if not args.ip:
        # descobrir ip
        pass
    return args.ip


def main():
    args = analisaArgs()
    ip = checaIPnosArgumentos(args)
    net = NetworkScanner(ip)
    w = Writer()
    while(True):
        clients = net.scan()
        devices = analisaDispositivos(clients)
        csv_devices = w.dispositivosDoCSV()
        list_to_print = comparaDispositivos(
            devices, csv_devices, net.getRouterIP())
        mostraDispositivos(list_to_print)
        w.escreveCSV(devices)
        time.sleep(args.time)


if __name__ == "__main__":
    main()
