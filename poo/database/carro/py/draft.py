class Car:
    def __init__(self):
        self.passengers: int = 0
        self.km: int = 0
        self.gas: int = 0
        self.passMax: int = 2
        self.gasMax: int = 100

    def __str__(self):
        return f"pass: {self.passengers}, gas: {self.gas}, km: {self.km}"
    
    def enter(self):
        if self.passengers >= self.passMax:
            print("fail: limite de pessoas atingido")
        else:
            self.passengers += 1
    
    def leave(self):
        if self.passengers <= 0:
            print("fail: nao ha ninguem no carro")
        else:
            self.passengers -= 1

    def fuel(self, increment: int):
        self.gas += increment
        if self.gas > self.gasMax:
            self.gas = self.gasMax
    
    def drive(self, distance: int):
        if self.passengers == 0:
            print("fail: nao ha ninguem no carro")
            return

        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if self.gas >= distance:
            self.gas -=distance
            self.km += distance
            
        else:
            km_percorrido = self.gas
            self.km += km_percorrido
            self.gas = 0

            print(f"fail: tanque vazio apos andar {km_percorrido} km")


def main():
    car = Car()

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()

        command: str = args[0]

        if command == "end":
            break
        elif command == "show":
            print(car)
        elif command == "enter":
            car.enter()
        elif command == "leave":
            car.leave()
        elif command == "fuel":
            amount:int = int(args[1])
            car.fuel(amount) 
        elif command == "drive":
            distance: int = int(args[1])
            car.drive(distance)
        else:
            print("fail: comando não encontrado")



main()