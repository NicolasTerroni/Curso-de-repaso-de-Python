# POO (it doesn't simulate perfecly a tv but it was usefull for practicing heredity and remember how it works on python)

class Electronics:
    def __init__(self):
         self.power = False
    
    def turn_on(self):
            self.power=True
            
    def turn_off(self):
            self.power=False
            
#---------------------------------------------------------------------------------------
class TVs(Electronics):
    _STATUS = [
    """             O         O
                        \\     // 
                         \\   //
                          \\ // 
                      /~~~~~\
            ,----------------------------,
            | ,------------------------ , |
            | |                              | |
            | |                              | |
            | |                              | |
            | |                              | |
            | |_______________| |
            |_________________|
            |_________________| """,
    """              O         O
                        \\     // 
                         \\   //
                          \\ // 
                      /~~~~~\
            ,----------------------------,
            | ,------------------------ , |
            | |                              | |
            | |   TA PRENDIDO   | |
            | |        JAJAJA          | |
            | |                              | |
            | |_______________| |
            |_________________|
            |_________________|"""
]

    def __init__(self, size, brand):
        super().__init__()
        self.screen_size = size
        self.brand_name = brand
        self.power=False

    def display_screen(self):
        if self.power==False:
            print( self._STATUS[0])
        else: 
            print( self._STATUS[1])
        
    def show_info(self):
        print(f"Model: {self.screen_size}. Screen size: {self.screen_size}.")

# --------------------------------------------------------------------------------------------------------------
plasmaTV = TVs("40x20", "Samsung")

while True:
    command = str(input("""
    You've got the remote.. tv is off, make a move:
    1) Turn on
    2) Drop the remote
    ---------> """))
    if command == "1":
        plasmaTV.turn_on()
        plasmaTV.display_screen()
        while True:
            command = str(input("""
            You've got the remote.. make a move:
            1) Turn off
            2) Show info
            3) Drop the remote
            ---------> """))
            if command=="1":
                plasmaTV.turn_off()
                plasmaTV.display_screen()
            elif command=="2":
                plasmaTV.show_info()
            else:
                break
    else:
        break
  

