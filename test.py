import unittest

from structure0 import Student

class Test(unittest.TestCase):
    def test_case1(self):
        """ Check if the Student class operates as expected """
        jane = Student("Jane", 322262)
        self.assertEqual(jane.name, "Jane")
        jane.changeID(283833)
        self.assertEqual(jane.id, 283833)


if __name__ == "__main__":
    unittest.main()