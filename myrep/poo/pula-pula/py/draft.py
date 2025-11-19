class Crianca:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}:{self.idade}"

class PulaPula:
    def __init__(self):
        self.fila: list[Crianca] = []      
        self.pulando: list[Crianca] = []   

    def arrive(self, nome: str, idade: int):
        crianca = Crianca(nome, idade)
        i = 0
        while i < len(self.fila) and self.fila[i].idade <= idade:
            i += 1
        self.fila.insert(i, crianca)

    def enter(self):
        if len(self.fila) == 0:
            print("fail: fila vazia")
            return
        crianca = self.fila.pop()  
        self.pulando.insert(0, crianca)

    def leave(self):
        if len(self.pulando) == 0:
            return
        crianca = self.pulando.pop() 
        self.fila.insert(0, crianca)

    def remove(self, nome: str):
        for i, c in enumerate(self.fila):
            if c.nome == nome:
                self.fila.pop(i)
                return
        for i, c in enumerate(self.pulando):
            if c.nome == nome:
                self.pulando.pop(i)
                return
        print(f"fail: {nome} nao esta no pula-pula")

    def __str__(self):
        fila_str = "[" + ", ".join(str(c) for c in self.fila) + "]"
        pulando_str = "[" + ", ".join(str(c) for c in self.pulando) + "]"
        return f"{fila_str} => {pulando_str}"

def main():
    pula = PulaPula()

    while True:
        line = input().strip()
        if line == "":
            continue

        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "arrive":
            nome = args[1]
            idade = int(args[2])
            pula.arrive(nome, idade)
        elif args[0] == "enter":
            pula.enter()
        elif args[0] == "leave":
            pula.leave()
        elif args[0] == "remove":
            nome = args[1]
            pula.remove(nome)
        elif args[0] == "show":
            print(pula)
        else:
            print("fail: comando invalido")
        

main()