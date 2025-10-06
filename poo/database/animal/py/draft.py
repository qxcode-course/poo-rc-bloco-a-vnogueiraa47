class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.age: int = 0
        self.sound: str = sound
    
    def __str__(self):
        return f"{self.species}:{self.age}:{self.sound}"
    
    def ageBy(self, increment: int):
        if self.age == 4:
            print(f"warning: {self.species} morreu")
            return
        
        self.age += increment
        if self.age >= 4 :
            self.age = 4
            print(f"warning: {self.species} morreu")

    def makeSound(self):
        if self.age == 0:
            return "---"
        elif self.age == 4:
            return "RIP"
        else:
            return self.sound


def main():
    animal: Animal = None

    while True:
        line: str = input()
        print("$" + line)
        args: list[str] = line.split()

        command: str = args[0]

        if command == "end":
            break
        elif command == "init":
            species: str = args[1]
            sound: str = args[2]
            animal = Animal(species, sound)
        elif command == "show":
            if animal:
                print(animal)
            else:
                print("fail: animal não inicialiazdo")
        elif command == "grow":
            if animal:
                increment: int = int(args[1])
                animal.ageBy(increment)
            else:
                print("fail: animal não inicializado")
        elif command == "noise":
            if animal:
                print(animal.makeSound())
            else:
                print("fail: animal não inicializado")
        else:
            print("fail: comando não encontradp")

main()