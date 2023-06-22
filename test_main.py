from main import addition
import random


def test_addition():
    x1 = random.randint(0, 100)
    x2 = random.randint(0, 100)

    output = addition(x1, x2)

    answer = x1 + x2
    assert output == answer, "wrong addition"