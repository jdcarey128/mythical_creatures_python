class Centaur: 
    def __init__(self, name, breed):
        self.name = name 
        self.breed = breed 
        self.crankiness_level = 0
        self.standing = True

    def shoot(self):
        self.crankiness_level += 1
        if self.is_cranky() or self.is_laying():
            return "NO!" 
        else:
             return "Twang!!!"

    def run(self):
        self.crankiness_level += 1
        if self.is_cranky() or self.is_laying():
            return "NO!" 
        else:
            return "Clop clop clop clop!!!"

    def crankiness_score(self):
        return 2

    def is_cranky(self):
        return self.crankiness_level > self.crankiness_score()

    def is_standing(self):
        return self.standing

    def sleep(self): 
        if self.standing:
            return "NO!"
        else: 
            self.crankiness_level = 0

    def lay_down(self):
        self.standing = False

    def is_laying(self):
        return not self.standing

    def stand_up(self): 
        self.standing = True

    def drink_potion(self): 
        if self.is_laying():
            return "Can't, I'm laying"
        elif self.crankiness_level == 0:
            return "Now I'm sick"
        else: 
            self.crankiness_level = 0
