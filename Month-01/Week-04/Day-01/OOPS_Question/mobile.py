class Mobile:

    def __init__(self, brand, model, ram, storage, battery, camera, processor, price):
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
        self.battery = battery
        self.camera = camera
        self.processor = processor
        self.price = price

    def call(self):
        print("Calling...")

    def send_message(self):
        print("Message Sent.")

    def take_photo(self):
        print("Photo Captured.")

    def charge(self):
        print("Mobile is Charging.")

    def show_specification(self):
        print("\n----- Mobile Specification -----")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("RAM:", self.ram)
        print("Storage:", self.storage)
        print("Battery:", self.battery)
        print("Camera:", self.camera)
        print("Processor:", self.processor)
        print("Price:", self.price)

mobile1 = Mobile("Samsung","Galaxy S24","8 GB","256 GB","5000 mAh","50 MP","Snapdragon 8 Gen 3",75000)

mobile1.show_specification()
mobile1.call()
mobile1.send_message()
mobile1.take_photo()
mobile1.charge()