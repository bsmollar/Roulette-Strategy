class RouletteTable:
    def __init__(self):
        #constructor
        #initializes numbers, a dictionary containing numbers as keys and their corresponding colors as values
        #initializes past spins, a list containing the dictionary keys previously spun, up to the last 10 spins
        self.numbers = self.build_wheel()
        self.pastSpins = []

    def build_wheel(self):
        #builds roulette wheel and adds each number to dictionary
        #returns dictionary of numbers
        wheel = {}
        for number in range(37):
            if number == 0:
                color = 'green'
            elif number % 2 == 0:
                color = 'black'
            else:
                color = 'red'
            wheel[number] = color
        wheel[37] = 'green'  # Representing '00' as 37
        return wheel

    def get_color(self, number):
        #gets color of the key passed into the function
        #Parameter: number - dictionary key you want the color of
        #returns color
        return self.numbers.get(number, None)
    
    def is_valid_number(self, number):
        #checks if the number passed is on the roulette wheel
        #Parameter: number - number you want to see if it is on the wheel
        #returns true or false
        return number in self.numbers

    def spin(self):
        #selects random element from the dictionary, which is a number and color pair
        #no return
        import random
        result = random.choice(list(self.numbers.keys()))
        self.pastSpins.append(self.numbers[result])
        if len(self.pastSpins) > 10:
            self.pastSpins.pop(0)
    
    def get_last_spin(self):
        #returns last spun number
            if not self.pastSpins:
                return None
            else:
                return self.pastSpins[len(self.pastSpins) - 1]