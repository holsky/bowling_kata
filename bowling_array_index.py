class Game:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        total_score = 0
        frame_index = 0
        for frame in xrange(0, 10):
            if (self.is_strike(frame_index)):
                total_score += self.strike_bonus(frame_index)
                frame_index += 1
            elif (self.is_spare(frame_index)):
                total_score += 10 + self.rolls[frame_index + 2]
                frame_index += 2
            else:
                total_score += self.rolls[frame_index] + self.rolls[frame_index + 1]
                frame_index += 2
        return total_score

    def is_strike(self, frame_index):
        return self.rolls[frame_index] == 10

    def is_spare(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1] == 10

    def strike_bonus(self, frame_index):
        return 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]