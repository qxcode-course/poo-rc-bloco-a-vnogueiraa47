class Calculator:
    def __init__(self, batteryMax: int):
        self.display: float = 0.00
        self.battery: int = 0
        self.batteryMax: int = batteryMax

    def __str__(self) -> str:
        return f"display = {self.display:.2f}, battery = {self.battery}"
    
    def charge(self, increment: int):
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax
    
    def _has_battery(self) -> bool:
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return False
        return True
    
    def sum(self, a: float, b: float):
        if not self._has_battery():
            return
        
        self.battery -= 1
        self.display = a + b

    def div(self, a: float, b: float):
        if not self._has_battery():
            return
        
        if b == 0:
            print("fail: divisao por zero")
        else:
            self.display = a / b
        
        self.battery -= 1

def main():
    calc: Calculator = None

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] =  line.split()

        command: str = args[0]

        if command == "end":
            break
        elif command == "init":
            battery_max: int = int(args[1])
            calc = Calculator(battery_max)
            
        elif command == "show":
            if calc:
                print(calc)
            else:
                print("fail: calculadora não inicializada")
        elif command == "charge":
            if calc:
                increment: int = int(args[1])
                calc.charge(increment)
            else:
                print("fail: calculadora não inicializada")
        elif command == "sum":
            if calc:
                a: float = float(args[1])
                b: float = float(args[2])
                calc.sum(a, b)
            else:
                print("fail: calculadora não inicializada")
        elif command == "div":
            if calc:
                a: float = float(args[1])
                b: float = float(args[2])
                calc.div(a, b)
            else:
                print("fail: calculadora não inicializada")
        else:
            print("fail: comando não encontrado")

main()