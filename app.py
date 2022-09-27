class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def sub(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def mul(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def div(a: int, b: int) -> float:
        return a / b


app = FastAPI()


@app.get('/{param}/{frst_arg}/{snd_arg}')
def calc(param: str, frst_arg: int, snd_arg: int) -> dict[str, list]:
    if param == "+":
        return {"Result": [Calculator.add(frst_arg, snd_arg), ""]}
    elif param == "-":
        return {"Result": [Calculator.sub(frst_arg, snd_arg), ""]}
    elif param == "*":
        return {"Result": [Calculator.mul(frst_arg, snd_arg), ""]}
    elif param == ":":
        if snd_arg == 0:
            return{"Result": ["Can't divide by zero", ""]}
        else:
            return {"Result": [Calculator.div(frst_arg, snd_arg), ""]}
    else:
        return{"Result": ["Please, enter parameters", ""]}

