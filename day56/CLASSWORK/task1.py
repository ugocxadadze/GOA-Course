class Robot:
    def __init__(self):
        self.water_level = 0  

    def fill_water(self, amount):
        """დავსხათ წყალი რობოტის საცავში"""
        if amount > 0:
            self.water_level += amount
            print("წყალი დასხმულია: {} ლიტრი. არსებული დონე: {} ლიტრი.".format(amount, self.water_level))
        else:
            print("არასწორი რაოდენობა წყლის დასხმაში.")

    def fetch_water(self):
        """მოიტანს წყლის რაოდენობას და გააგზავნის პირნიშანს"""
        if self.water_level > 0:
            print("მოიტანე {} ლიტრი წყალი.".format(self.water_level))
            self.water_level = 0  
        else:
            print("წყალი არ არის!")


my_robot = Robot()
my_robot.fill_water(5) 
my_robot.fetch_water()
my_robot.fetch_water()