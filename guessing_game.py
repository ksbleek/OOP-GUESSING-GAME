class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
    
        self.temp_game = False

    def guess(self, user_guess):
        if user_guess > self.answer:
            return "high"
        elif user_guess == self.answer:
            self.temp_game = True
            return "correct"
        elif user_guess < self.answer:
            return "low"
    def solved(self):
        return self.temp_game
    pass