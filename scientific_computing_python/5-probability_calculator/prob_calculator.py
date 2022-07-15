import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **balls):
        self.balls = balls
        contents = []
        for ball_color, num_of_balls in balls.items():
            for num in range(0, num_of_balls):
                contents.append(ball_color)
        self.contents = contents

    # draw balls and remove from contents
    def draw(self, num_of_balls):
        if len(self.contents) < num_of_balls:
            return self.contents

        chosen_balls = []
        for ball in range(0, num_of_balls):
            chosen = random.choice(self.contents)
            chosen_balls.append(chosen)
            self.contents.remove(chosen)
        return chosen_balls

# Draw out balls and test against expected results
# Do this a given number of times
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_chosen_balls = 0
    for experiment in range(0, num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls_drawn_result = hat_copy.draw(num_balls_drawn)

        has_expected_balls = True
        for color, num in expected_balls.items():
            if balls_drawn_result.count(color) >= num:
                continue
            else:
                has_expected_balls = False
                break
        if has_expected_balls:
            num_chosen_balls += 1
    return round(num_chosen_balls / num_experiments, 3)

