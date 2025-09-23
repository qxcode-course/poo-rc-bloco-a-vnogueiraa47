class Towel:
    def __init__(self, color: str, size: str): # construtor
        self.color: str = color # atributos
        self.size: str = size
        self.wetness: int = 0
    
    def dry(self, amount: int) -> None:
        self.wetness += amount
        if self.wetness > self.isMaxWetness():
            self.wetness = self.isMaxWetness()
            print("Toalha molhada!")
    
    def wrigOut(self):...



    def isMaxWetness(self) -> int:
        if self.size == "P": # early return
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0 # default return

    def __str__(self) -> str: # toString
        return f"Color:{self.color}, Size:{self.size}, Wet:{self.wetness}"
    
def main():  
  
    towel: Towel = Towel("", "")
    while True:
        
        line: str = input()
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "new":
            color: str = args[1]
            size: str = args[2]
            towel = Towel(color, size)
        elif args[0] == "dry":
            amount: int = int(args[1])
            towel.dry(amount)
        elif args[0] == "show":
            print(towel)
        else:
            print("fail: comando não encontrado")

main()