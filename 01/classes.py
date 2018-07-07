class Car():
    """an attempt to represent a car"""
    object = "car"

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_name(self):
        return f"{self.year} {self.brand.title()} {self.model.title()}"

my_car = Car("bmw", "x2", "2017")
# print(my_car.get_name())
# print(my_car.object)

class Library():
	class Artists:
		def init(self, artist="all"):
			return bag.get(artist)
		
		bag = {"all":[1,2,3,4]}

lib = Library().Artists("all")
print(lib)
