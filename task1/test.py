import unittest
from solution import deco


class TestStrictDecorator(unittest.TestCase):

    def test_valid_arguments(self):
        @deco
        def add(a: int, b: int) -> int:
            return a + b

        self.assertEqual(add(2, 3), 5)

    def test_invalid_type_argument(self):
        @deco
        def greet(name: str, repeat: int) -> str:
            return name * repeat

        with self.assertRaises(TypeError) as cm:
            greet("Hi", "2")

        self.assertIn("Аргумент 'repeat'", str(cm.exception))

    def test_multiple_invalid_arguments(self):
        @deco
        def combine(x: int, y: str) -> str:
            return str(x) + y

        with self.assertRaises(TypeError) as cm:
            combine("1", 2.0)

        self.assertIn("Аргумент 'x'", str(cm.exception))

    def test_float_argument(self):
        @deco
        def square(n: float) -> float:
            return n * n

        self.assertEqual(square(2.5), 6.25)

    def test_bool_argument(self):
        @deco
        def check(flag: bool) -> str:
            return "OK" if flag else "NO"

        self.assertEqual(check(True), "OK")
        with self.assertRaises(TypeError):
            check(1)  # 1 не считается bool

if __name__ == '__main__':
    unittest.main()
