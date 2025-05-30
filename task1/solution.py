import inspect
from functools import wraps

def deco(func):
    sig = inspect.signature(func)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()

        for name, value in bound_args.arguments.items():
            expected_type = func.__annotations__.get(name)
            if expected_type and not isinstance(value, expected_type):
                raise TypeError(
                    f"Аргумент '{name}' должен быть типа {expected_type}, но получен тип {type(value)}"
                )
        return func(*args, **kwargs)

    return wrapper



@deco
def sum_two(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    print(sum_two(1, 2))     # 3
    print(sum_two(1, 2.4))   # TypeError
