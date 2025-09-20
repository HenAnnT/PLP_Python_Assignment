#  Assignment 1
# 
#  Base class: Device
class Device:
    def __init__(self, brand, model):
        self._brand = brand   # protected (convention: for internal use)
        self._model = model

    def device_info(self):
        return f"{self._brand} {self._model}"


# Child class: Smartphone (inherits from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand, model)  # call parent constructor
        self.__storage = storage        # private (encapsulation)
        self.__battery = battery        # private (encapsulation)

    # Getter and Setter using encapsulation
    def get_storage(self):
        return self.__storage

    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("⚠️ Storage must be positive!")

    def use_battery(self, percent):
        if 0 < percent <= self.__battery:
            self.__battery -= percent
            print(f"🔋 Used {percent}%. Battery left: {self.__battery}%")
        else:
            print("⚠️ Not enough battery!")

    def charge(self):
        self.__battery = 100
        print("⚡ Phone fully charged!")


# Create smartphone objects
phone1 = Smartphone("Apple", "iPhone 14", 256, 100)
phone2 = Smartphone("Samsung", "Galaxy S23", 128, 80)

print(phone1.device_info())   # Apple iPhone 14
phone1.use_battery(20)        # 🔋 Used 20%. Battery left: 80%
phone1.charge()               # ⚡ Phone fully charged!



#  Assignment 2


class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method!")


class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")


class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")


class Boat(Vehicle):
    def move(self):
        print("🛳️ Sailing on the water")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
