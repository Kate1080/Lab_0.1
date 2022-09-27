def test_add() -> None:
    assert Calculator.add(10, 35) == 45
    assert Calculator.add(-200, 150) == -50
    assert Calculator.add(-5, -10) == -15


def test_sub() -> None:
    assert Calculator.sub(345, 30) == 315
    assert Calculator.sub(-2, 1) == -3
    assert Calculator.sub(-175, -200) == 25


def test_mul() -> None:
    assert Calculator.mul(16, 5) == 80
    assert Calculator.mul(-4, 35) == -140
    assert Calculator.mul(-3, -15) == 45


def test_div() -> None:
    assert Calculator.div(-16, 4) == -4
    assert Calculator.div(200, -5) == -40
    assert Calculator.div(32, 8) == 4

