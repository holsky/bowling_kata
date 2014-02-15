class Game(object):

    def __init__(self):
        self.frames = [Frame()]

    def record_roll(self, knocked_down_pins):
        last_frame = self.frames[len(self.frames) - 1]
        if self.is_tenth_frame():
            last_frame.add_roll(knocked_down_pins)
        elif self.frame_is_full(last_frame):
            last_frame.next_frame = self.start_new_frame_and_return(knocked_down_pins)
        else:
            last_frame.add_roll(knocked_down_pins)            

    def is_tenth_frame(self):
        return len(self.frames) == 10

    def frame_is_full(self, frame):
        return len(frame.rolls) == 2 or frame.is_strike()

    def start_new_frame_and_return(self, knocked_down_pins):
        f = Frame(knocked_down_pins)
        self.frames.append(f)
        return f

    def score(self):
        score = 0
        for index, frame in enumerate(self.frames):
            if frame.is_strike():
                score += frame.strike_bonus()
            elif frame.is_spare():
                score += frame.spare_bonus()
            score += sum(frame.rolls)
        return score

class Frame(object):

    def __init__(self, knocked_down_pins = None):
        self.rolls = []
        if knocked_down_pins != None:
            self.add_roll(knocked_down_pins)
        self.next_frame = None

    def add_roll(self, knocked_down_pins):
        self.rolls.append(knocked_down_pins)

    def is_spare(self):
        return self.rolls[0] + self.rolls[1] == 10                

    def is_strike(self):
        return len(self.rolls) > 0 and self.rolls[0] == 10

    def spare_bonus(self):
        if self.next_frame != None:
            return self.next_frame.rolls[0]
        else:
            return 0

    def strike_bonus(self):
        if self.is_not_tenth_frame():
            bonus = self.next_frame.rolls[0]
            if self.next_is_more_than_one_roll():
                bonus += self.next_frame.rolls[1]
            elif self.next_frame_is_not_tenth_frame(): 
                bonus += self.next_frame.next_frame.rolls[0]
            return bonus
        else:
            return 0

    def next_is_more_than_one_roll(self):
        return len(self.next_frame.rolls) != 1

    def next_frame_is_not_tenth_frame(self):
        return self.next_frame.next_frame != None

    def is_not_tenth_frame(self):
        return self.next_frame != None