def plus_one(x):
    return x + 1


def test_plus_one_passes():
    assert plus_one(3) == 4


def test_plus_one_fails():
    assert plus_one(5) == 7


test_plus_one_passes()
test_plus_one_fails()
