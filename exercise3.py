# Modelar un objeto, con estado y comportamiento
STATUS = ["""
-----ON-----
""","""
-----OFF-----
""","""
-----LOOKING FOR DEVICE-----
""","""
-----CHARGING-----
""","""
-----CONECTED-----
""","""
-----DISCONECTED-----
"""]

class Bluethoot_speaker:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.battery = 70
        self.volume = 50
        self.power = False
        self.conect = False

    def on_off(self):
        if self.power == False:
            self.power = True
            print(STATUS[0])
        else:
            self.power = False
            print(STATUS[1])
    
    def searching(self):
        if self.conect == False:
            print(STATUS[2])
            self.conect = True
            print(STATUS[4])
        else:
            self.conect = False
            print(STATUS[5])
# if this finds and match a device it starts playing its audio

    def charging(self):
        if self.battery != 100:
            print(STATUS[3])
            self.battery = 100

    def decrease_vol(self):
        if self.volume > 0:
            self.volume -= 10
            print(self.volume)
        else:
            print(self.volume)

    def increase_vol(self):
        if self.volume < 100:
            self.volume += 10
            print(self.volume)
        else:
            print(self.volume)


speaker = Bluethoot_speaker("JBL_GO","black")
