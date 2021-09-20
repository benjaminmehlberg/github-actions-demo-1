from hello import add


def test_add():
    assert str(add(1, 2)).isnumeric()
