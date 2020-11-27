import csv
import os.path
import datetime
from dispositivo import Dispositivo


class Writer():
    def __init__(self):
        self.criaCSV()

    def criaCSV(self):
        if (not os.path.exists('historico.csv')):
            firstRow = ['ID', 'IP', 'MAC', 'Fabricante', 'Hora Descoberta']
            with open('historico.csv', 'a') as h:
                writer = csv.writer(h)
                writer.writerow(firstRow)

    def escreveCSV(self, devices):
        now = datetime.datetime.now()
        with open('historico.csv', 'a') as h:
            writer = csv.writer(h)
            for device in devices:
                row = ['0', device.ip, device.mac,
                       device.manufacturer, now.strftime("%x %Hh%mm")]
                writer.writerow(row)

    def dispositivosDoCSV(self):
        devices = []
        with open('historico.csv', 'r') as h:
            reader = csv.reader(h)
            next(reader)  # pula header
            for row in reader:
                devices.append(Dispositivo(
                    ip=row[1], mac=row[2], fabricante=row[3]))
        return devices
