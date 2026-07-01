class Laptop:

    def __init__(self, volume):
        self.__volume = volume

    def increase_volume(self, value):

        if self.__volume + value <= 100:
            self.__volume += value
        else:
            self.__volume = 100

    def decrease_volume(self, value):

        if self.__volume - value >= 0:
            self.__volume -= value
        else:
            self.__volume = 0

    def get_volume(self):
        return self.__volume


laptop = Laptop(50)
print("Volume :", laptop.get_volume())

laptop.increase_volume(30)
print("Volume :", laptop.get_volume())

laptop.decrease_volume(40)
print("Volume :", laptop.get_volume())