import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

    def test_date(self):
        weekday = calculate(-1, 1, 3)
        self.assertEqual(weekday, -1)

        weekday = calculate(1, 40, 3)
        self.assertEqual(weekday, -1)

        weekday = calculate(1, 1, 40)
        self.assertEqual(weekday, -1)

    def test_input(self):

        retcode = main(("--year", "hehe", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 1)

        retcode = main(("--year", "2001", "--month", "fdvbds", "--day", "3"))
        self.assertEqual(retcode, 1)

        retcode = main(("--year", "2001", "--month", "1", "--day", "dvsdv"))
        self.assertEqual(retcode, 1)

        retcode = main("dffsfsa")
        self.assertEqual(retcode, 1)
        

if __name__ == '__main__':
    unittest.main()
