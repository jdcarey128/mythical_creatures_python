class Werewolf:

    def __init__(self, name, location = "London", human_state=True, hungry=False):
        self.name = name
        self.location = location
        self.human_state = human_state
        self.hunger_state = hungry

    def is_human(self):
        return self.human_state
    
    def change(self):
        self.human_state = not self.human_state
        self.hunger_state = not self.human_state

    def is_wolf(self):
        return not self.human_state

    def is_hungry(self):
        return self.hunger_state
    
    def consume(self, human):
        if self.human_state:
            return "No one was consumed"
        else:
            self.hunger_state = False
            human.kill()
