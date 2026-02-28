class Cars:
    def __init__(self, Brand, Model, Year, Color, Engine):
        self.brand = Brand
        self.model = Model
        self.year = Year
        self.color = Color
        self.engine = Engine

    def showDescription(self):
        print("Brand is {}. Model is {}. Year is {}. Color is {}. Engine is {}." 
              .format(self.brand, self.model, self.year, self.color, self.engine))
        
    def showBrandModel(self):
        print("This car is a {} {}.".format(self.brand, self.model))

    def startEngine(self):
        print("The {} {}'s engine has started.".format(self.brand, self.model))

    def stopEngine(self):
        print("The {} {}'s engine has stopped.".format(self.brand, self.model))

    def showCarInfo(self):
        print("Brand: {}\nModel: {}\nYear: {}\nColor: {}\nEngine: {}"
              .format(self.brand, self.model, self.year, self.color, self.engine))
        
    

car1 = Cars("BMW", "M4", "2022", "Black", "3.0L")
car1.showDescription()
car1.showBrandModel()
car1.startEngine()
car1.stopEngine()
car1.showCarInfo()

car2 = Cars("Audi", "A6", "2021", "White", "2.0L")
car2.showDescription()
car2.showBrandModel()
car2.startEngine()
car2.stopEngine()
car2.showCarInfo()

car3 = Cars("Mercedes", "C-Class", "2020", "Silver", "2.0L")
car3.showDescription()
car3.showBrandModel()
car3.startEngine()
car3.stopEngine()
car3.showCarInfo()

car4 = Cars("Tesla", "Model 3", "2021", "Red", "Electric")
car4.showDescription()
car4.showBrandModel()
car4.startEngine()
car4.stopEngine()
car4.showCarInfo()

car5 = Cars("Lexus", "RX", "2022", "Blue", "3.5L")
car5.showDescription()
car5.showBrandModel()
car5.startEngine()
car5.stopEngine()
car5.showCarInfo()




