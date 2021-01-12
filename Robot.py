import time


class Robot:
    def __init__(self, Name, Color, Weight):
        self.Name = Name
        self.Color = Color
        self.Weight = Weight

    def Say_Hi(self):
        print("Hello World my name is " + self.Name)

    def Say_Weight(self):
        print("Hey I weight " + self.Weight + " Pounds")

    def Say_Color(self):
        print("My Favourite Color is " + self.Color)


Robot1 = Robot("AI_734#20", "Blue", "1_000")

time.sleep(2)
Robot1.Say_Hi()
time.sleep(2)
Robot1.Say_Weight()
time.sleep(2)
Robot1.Say_Color()


time.sleep(5)

quit()