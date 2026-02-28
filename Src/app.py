class Car:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.color = ""
        self.model = ""
    def information(self):
        print(f"Car name: {self.name}")
        print(f"Car price: {self.price}")
        print(f"Car color: {self.color}")
        print(f"Car model: {self.model}")
    def start(self):
        print("Car started")

car1 = Car()
car1.name = "Toyota"
car1.price = 20000
car1.color = "Red"
car1.model = "Corolla"
car1.information()
car1.start()