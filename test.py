import unittest
from alphabetsoup import alphabetsoup

class TestSolution(unittest.TestCase):
    def test_lower_case(self):
        self.assertEqual(alphabetsoup("zxyw"),"wxyz", f'Wrong: got {alphabetsoup("zxyw")}')
        self.assertEqual(alphabetsoup("goodluck"), "cdgkloou", f'Wrong: got {alphabetsoup("goodluck")}')
    def test_upper_case(self):
        self.assertEqual(alphabetsoup("ZYWX"),"wxyz", f'Wrong: got {alphabetsoup("ZYWX")}')
        self.assertEqual(alphabetsoup("GOODLUCK"), "cdgkloou", f'Wrong: got {alphabetsoup("GOODLUCK")}')
    def test_with_symbols(self):
        self.assertEqual(alphabetsoup("ZYWX!?"),"wxyz", f'Wrong: got {alphabetsoup("ZYWX")}')
        self.assertEqual(alphabetsoup("Good luck!"), "cdgkloou", f'Wrong: got {alphabetsoup("GOODLUCK")}')
if __name__ == "__main__":
    unittest.main()