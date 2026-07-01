class Car:

    def __init__(self, speed):
        self.__speed = speed

    def accelerate(self, value):
        self.__speed += value

    def brake(self, value):
        if self.__speed - value >= 0:
            self.__speed -= value
        else:
            print("Speed cannot be negative")

    def get_speed(self):
        return self.__speed


car = Car(50)
print("Speed :", car.get_speed())
car.accelerate(30)
print("Speed :", car.get_speed())
car.brake(40)
print("Speed :", car.get_speed())