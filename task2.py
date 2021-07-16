# Parent Class
class Vehicle():
    def __init__(self, Color, Price, Maximum_Speed):
        self.Color = Color
        self.Price = Price
        self.Maximum_Speed = Maximum_Speed

# Child Class
class Car(Vehicle):
    def __init__(self, Color, Price, Maximum_Speed, Number_of_Tires):

        # Invoking the parent constructor
        super().__init__(Color, Price, Maximum_Speed)

        self.Number_of_Tires = Number_of_Tires
    
    # Instance method to show the desired output
    def  display(self):
        print(f"A {self.Color}-colored car with a maximum speed of {self.Maximum_Speed} km/h is priced at {self.Price} with {self.Number_of_Tires} tires")

# Creating a Car object
a = Car("red","500000","200","4")

# Calling instance method through class object
a.display()
