from hello import add

def test_add(x, y):
    assert str(add(x, y)).isnumeric()
