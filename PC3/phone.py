# phone.py
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = ""  # Nuevo atributo

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

    def new_method(self, attribute):
        print(f"New method with attribute: {attribute}")

    def mostrar_informacion(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}, Color: {self.color}")
