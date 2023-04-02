from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file_data:
            self.highScore = int(file_data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, high score: {self.highScore}", align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        if self.score > self.highScore:
            self.highScore = self.score
            with open("data.txt", mode="w") as file_data:
                file_data.write(f"{self.highScore}")
        self.score = 0  # reset the score to 0 after updating the high score with new high score

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        # self.clear() not required as there is no game over instead reset the game with score as 0
        self.update_scoreboard()
