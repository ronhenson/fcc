# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator

prob_calculator.random.seed(95)
# hat = prob_calculator.Hat(blue=4, red=2, green=6)
# probability = prob_calculator.experiment(
#     hat=hat,
#     expected_balls={"blue": 2,
#                     "red": 1},
#     num_balls_drawn=4,
#     num_experiments=3000)
# print("Probability:", probability)

prob_calculator.random.seed(95)
hat2 = prob_calculator.Hat(blue=3, red=2, green=6)
print("orig: ", hat2.contents)
# print()
probability = prob_calculator.experiment(
    hat=hat2,
    expected_balls={"blue": 2, "green": 1},
    num_balls_drawn=4,
    num_experiments=1000
)
expected = 0.272
print(f'probability: {probability}   expected: {expected}')
