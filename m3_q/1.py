class Car:
    def __init__(self,regno,no_gears):
        self.regno=regno
        self.no_gears=no_gears
    def start(self):
        print(f"car with regno {regno} started...")
    def stop(self):
        print(f"car with regno{regno} stopped...")
    def change_gear(self):
        print(f"{regno} changed gear...")