from re import I


class Ingredients():
    def __init__ (self,name = None,meat = None, vegetables = None, others = None, price = None):
        self.name = input("name: ")

        self.meat = input("Type what kind of meat (If none then don't put anything): ")

        self.vegetables = input("Type what kind of vegetables (If none then don't put anything): ")

        self.others = input("Input anything else: ")

        self.price = input("Put the total price: ")

    def displayIngredients(self):
        print("Name: ", self.name, "Meat:", self.meat, "Vegetables:", self.vegetables, "Others:", self.others, "Total Cost:", self.price)
    

food1 = Ingredients()
print("Your Food:")
food1.displayIngredients()


