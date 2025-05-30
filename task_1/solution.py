def strict(func):
    def wrapper(*args, **kwargs):
        value_type = set([v for v in func.__annotations__.values()])
        input_data_value_type = set([type(x) for x in args])
        if len(input_data_value_type) > 1:
            return "TypeError"
        elif input_data_value_type != value_type:
            return "TypeError"
        else:
            return func(*args, **kwargs)

    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


@strict
def sum_two_bool(a: bool, b: bool) -> bool:
    return a + b


@strict
def sum_three_float(a: float, b: float, c: float) -> float:
    return a + b + c
