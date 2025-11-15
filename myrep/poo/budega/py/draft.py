class Person:
    def __init__(self, name: str):
        self.__name = name

    def getName(self):
        return self.__name

    def __str__(self):
        return self.__name
    
class Market:
    def __init__(self, counter_size: int) -> None:
        self.counter: list[Person | None] = []
        for _ in range(counter_size):
            self.counter.append(None)
        self.waiting: list[Person] = []

    def arrive(self, person: Person):
        self.waiting.append(person)

    def leave(self, index: int):
        if index < 0 or index >= len(self.counter):
            print("fail: caixa inexistente")
            return
        if self.counter[index] == None:
            print("fail: caixa vazio")
            return
        aux = self.counter[index]
        self.counter[index] = None
        return aux
    
    def give_up(self, name: str):
        for i, person in enumerate(self.waiting):
            if person.getName() == name:
                del self.waiting[i]
                return

    def call(self, index: int):
        if index < 0 or index >= len(self.counter):
            print("fail: caixa inexistente")
            return
        if self.counter[index] is not None:
            print("fail: caixa ocupado")
            return
        if len(self.waiting) == 0:
            print("fail: sem clientes")
            return
        self.counter[index] = self.waiting.pop(0)

    def __str__(self) -> str:
        caixas = ", ".join([("-----" if x is None else str(x)) for x in self.counter])
        #for person in self.counter:
            #if person is None:
                #saida += "-----"
            #else:
             #   saida += str(person) + " "
        espera = ", ".join([str(x) for x in self.waiting])
        return f"Caixas: [{caixas}]\nEspera: [{espera}]"
    

def main():
    market = Market(0)
    while True:
        line = input().strip()
        if line == "":
            continue
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            qtd = int(args[1])
            market = Market(qtd)
        elif args[0] == "show":
            print(market)
        elif args[0] == "arrive":
            market.arrive(Person(args[1]))
        elif args[0] == "call":
            index = int(args[1])
            market.call(index)
        elif args[0] == "finish":
            index = int(args[1])
            market.leave(index)
        elif args[0] == "giveup":
            market.give_up(args[1])
        else:
            print("fail: comando invalido")

main()