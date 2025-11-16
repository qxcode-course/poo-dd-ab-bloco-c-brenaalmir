class Client:
    def __init__(self, id: str, phone: int):
        self.id = id
        self.phone = phone

    def __str__(self):
        return f"{self.id}:{self.phone}"
    
class Theater:
    def __init__(self, size: int):
        self.seats: list[Client | None] = []
        for _ in range(size):
            self.seats.append(None)

    def search(self, name: str):
        for i, cli in enumerate(self.seats):
            if cli is not None and cli.id == name:
                return i
        return -1
    
    def verifyIndex(self, index: int):
        if index < 0 or index >= len(self.seats):
            print("fail: cadeira nao existe")
            return False
        return True
    
    def reserve(self, id: str, phone: int, index: int):
        if not self.verifyIndex(index):
            return
        if self.seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return
        if self.search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return
        self.seats[index] = Client(id, phone)

    def cancel(self, id: str):
        pos = self.search(id)
        if pos == -1:
            print("fail: cliente nao esta no cinema")
            return
        self.seats[pos] = None

    def getSeats(self):
        return self.seats
    
    def __str__(self):
        saida = "["
        for seat in self.seats:
            if seat is None:
                saida += "- "
            else:
                saida += str(seat) + " "
        saida = saida.strip()
        saida += "]"
        return saida
    

def main():
    theater = Theater(0)
    while True:
        line = input().strip()
        if line == "":
            continue
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            n = int(args[1])
            theater = Theater(n)
        elif args[0] == "show":
            print(theater)
        elif args[0] == "reserve": 
            name = args[1]
            phone = int(args[2])
            index = int(args[3])
            theater.reserve(name, phone, index)
        elif args[0] == "cancel":
            name = args[1]
            theater.cancel(name)
        else:
            print("fail: comando invalido")

main()