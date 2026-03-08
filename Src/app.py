class Car:

    def __init__(self, name, price, color, model):
        self.name = name
        self.price = price
        self.color = color
        self.model = model

    def __del__(self):
        print(f"The {self.name} is being scrapped. Goodbye!")

    def information(self):
        print(f"Car name: {self.name}")
        print(f"Car price: {self.price}")
        print(f"Car color: {self.color}")
        print(f"Car model: {self.model}")

    def start(self):
        print("Car started. Vroom vroom!")


car1 = Car("Toyota", 20000, "Red", "Corolla")
car1.information()
car1.start()