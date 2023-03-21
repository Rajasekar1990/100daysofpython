class MyClass:
    def __init__(self, seats, wheel, engine_capacity):
        self.seat = seats
        self.wheels = wheel
        self.cc = engine_capacity
        self.torque = 250

    def race_mode(self):
        self.seat = 2
        return self.seat

obj = MyClass(7, 4, 2.0)
print(f"{obj.cc}l engine")
print(f"{obj.torque}")
print(obj.race_mode())
