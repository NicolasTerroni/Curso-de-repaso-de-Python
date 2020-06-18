# POO

class TVs:
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
        self.power = False
        self.screen_size = size
        self.brand_name = brand
    def switch_power(self):
        if self.power==False:
            self.power=True
            self.__display_screen()
        else:
            self.power=False
            self.__display_screen()

    def __display_screen(self):
        if self.power==False:
            print( self._STATUS[0])
        else: 
            print( self._STATUS[1])
        
    def show_info(self):
        print(f"Modelo: {self.screen_size}. De pantalla {self.screen_size}.")


plasmaTV = TVs("40x20", "Samsung")

while True:
    command = str(input("""
    You've got the remote.. make a move:
    1) Turn on/off
    2) Show info
    3) Drop the remote
    ---------> """))
    if command == "1":
        plasmaTV.switch_power()
    elif command == "2":
        plasmaTV.show_info()
    else:
        break


