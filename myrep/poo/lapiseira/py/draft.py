class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = calibre
        self.dureza = dureza
        self.tamanho = tamanho

    def gasto_por_folha(self):
        if self.dureza == "HB":
            return 1
        if self.dureza == "2B":
            return 2
        if self.dureza == "4B":
            return 4
        if self.dureza == "6B":
            return 6
        return 1
    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.tamanho}"
    

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None
        self.tambor: list[Grafite] = []

    def insert(self, grafite: Grafite):
        if grafite.calibre != self.calibre:
            print("fail: calibre incompatível")
            return
        self.tambor.append(grafite)

    def pull(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return
        if len(self.tambor) == 0:
            print("fail: tambor vazio")
            return
        self.bico = self.tambor.pop(0)

    def remove(self):
        self.bico = None

    def write(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        gasto = self.bico.gasto_por_folha()
        if self.bico.tamanho <= 10:
            print("fail: tamanho insuficiente")
            return
        if self.bico.tamanho - gasto < 10:
            print("fail: folha incompleta")
            self.bico.tamanho = 10
            return
        self.bico.tamanho -= gasto

    def __str__(self):
        bico_str = "[]" if self.bico is None else f"[{self.bico}]"
        tambor_str = "<" + "".join([f"[{g}]" for g in self.tambor]) + ">"
        return f"calibre: {self.calibre}, bico: {bico_str}, tambor: {tambor_str}"
    

def main():
    lapiseira = Lapiseira(0.5)
    while True:
        line = input().strip()
        if line == "":
            continue
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            lapiseira = Lapiseira(float(args[1]))
        elif args[0] == "show":
            print(lapiseira)
        elif args[0] == "insert":
            cal = float(args[1])
            dur = args[2]
            tam = int(args[3])
            lapiseira.insert(Grafite(cal, dur, tam))
        elif args[0] == "pull":
            lapiseira.pull()
        elif args[0] == "remove":
            lapiseira.remove()
        elif args[0] == "write":
            lapiseira.write()
        else:
            print("fail: comando invalido")

main()