import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):

        self.contents = []
        for k in kwargs:
            for _ in range(kwargs[k]):
                self.contents.append(k)

        if len(self.contents) < 1:
            raise Exception("Can't create a hat without any ball")

    def draw(self, num_balls):
        return [
            self.contents.pop(self.contents.index(random.choice(
                self.contents))) for _ in range(num_balls)
        ] if num_balls < len(self.contents) else self.contents


def check(x, y):
    s = set()
    for i in x:
        s.add(x[i] <= y.get(i, 0))
    return False if False in s else True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    f = 0
    c_hat = copy.deepcopy(hat)
    for _ in range(num_experiments):
        x = c_hat.draw(num_balls_drawn)
        c_hat = copy.deepcopy(hat)
        c = dict()
        for items in x:
            c[items] = c.get(items, 0) + 1

        if check(expected_balls, c):
            f += 1

    return f / num_experiments


random.seed(95)
hat = Hat(blue=4, red=2, green=6)
probability = experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
