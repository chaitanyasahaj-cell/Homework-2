class Students:
    def __init__(self, Name, Age, Grade, Height, Weight):
        self.name = Name
        self.age = Age
        self.grade = Grade
        self.height = Height
        self.weight = Weight

    def showDescription(self):
        print("Name is {}. Age is {}. Grade is {}. Height is {}. Weight is {}." .format(self.name, self.age, self.grade, self.height, self.weight))

student1 = Students("Sahaj", "14", "10", "5'9'", "65kg")
student1.showDescription()




# #Objects and Classes

# class Car:
#     #constructor - is a special function that will automatically execute itself
#     #self - refers to the current object
#     #Properies and 
#      def __init__(self, Name, Colour):
#          self.name = Name
#          self.colour = Colour


#      def showTopSpeed(self, topSpeed):
#         print("The top speed of {} is {}mph" .format(self.name, topSpeed))

# car1 = Car('Mercedes', 'Black')
# car1.showTopSpeed(300)

# car2 = Car('Rolls Royce', 'White')
# car2.showTopSpeed(250)