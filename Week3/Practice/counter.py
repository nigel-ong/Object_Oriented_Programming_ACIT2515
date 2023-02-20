class Countdown:
    def __init__ (self, start, step=1):
        self.current = start
        self.step = step
        self.complete

    def down(self):
        self.current -= self.step
        self.complete


    @property
    def complete(self):
        if self.current <= 0:
            return True
        else:
            return False
        


    