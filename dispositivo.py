class Dispositivo:
    def __init__(self, ip, mac, fabricante, isHost=True, status="Offline"):
        self.ip = ip
        self.mac = mac
        self.fabricante = fabricante
        self.isHost = isHost
        self.status = status

    def __repr__(self):
        return '\nIP:      {}\nMAC:     {}\nManuf:   {}\nStatus:  {}\n'.format(
            self.ip,
            self.mac,
            self.fabricante,
            self.status
        )

    def __eq__(self, outro):
        return self.mac == outro.mac

    def __hash__(self):
        return hash(('mac', self.mac))
