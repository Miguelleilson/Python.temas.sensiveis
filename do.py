lista = []
class Inscryption:
    Name: str
    City: str
    Age: int
        
    def __init__(self, Name: str, City: str, Age: int):
        self.Name = Name
        self.City = City
        self.Age = Age
while True:

    option = int(input("selecione a option: "))

    match option: 
        
        case 1:
        
            print("Nova Inscrição")
            Name = input("digita seu nome pa nóis: ")
            Name = Name.strip()
            Name = Name.title()
            City = input("Digite sua cidade: ")
            City = City.strip().title()
            
            Age = int(input("IDADE: "))
            inscryption = Inscryption(Name, City, Age)
            lista.append(inscryption)
        case 2:
            print("Consultar Inscrição")
            for inscription in lista:
                print(inscryption.Name)
                print(inscryption.City)
                print(inscryption.Age)
            
            
        case 3:
            print("Alterar Nome")
            np = input("digite um nome para alterar: ")
            for inscryption in lista:
                if inscryption.Name == np:
                    new_name = input("digite o novo nome: ")
                    inscription.Name = new_name
               
            
        case 4:
            print("sair")
            break
            
        case _: 
            print("invalid data annotation XD ")
            