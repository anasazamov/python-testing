from main import addition


def test_addition():
    x1 = 3
    x2 = 5

    output = addition(x1, x2)

    answer = x1 + x2
    assert output == answer, "wrong addition"