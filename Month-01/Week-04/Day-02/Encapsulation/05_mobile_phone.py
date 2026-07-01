class Mobile:
    def __init__(self, battery):
        self.battery_percentage = battery

    def charge(self,amount):
        if self.__battery_percentage + amount <= 100:
            self.__battery_percentage += amount

        else:
            self.__battery_percentage = 100

    def use_phone(self, amount):
        if self.__battery_percentage - amount >= 0:
            self.__battery_percentage -= amount
        else:
            self.__battery_percentage = 0

    def get_battery(self):
        return self.__battery_percentage


mobile = Mobile(60)
print("Battery :", mobile.get_battery())

mobile.charge(20)
print("Battery :", mobile.get_battery())



