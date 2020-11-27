class MacSearch:
    def __init__(self):
        self.fabricante = self.parseFabricantes()

    def parseFabricantes(self):
        d = {}
        with open("fabricantes.txt", encoding='utf-8') as f:
            for line in f:
                line_parsed = line.split("\t", 1)
                if (line[0] != '#' and len(line_parsed) > 1):
                    (key, val) = line_parsed
                    d[key] = val.rstrip('\n')
        return d

    def parseMACFabricante(self, mac):
        return mac.replace('-', ':')[:8].upper()

    def getFabricante(self, mac):
        initMac = self.parseMACFabricante(mac)
        return self.fabricante.get(initMac, 'Fabricante não encontrado')
