def oddNumbers(start, stop):
    try:
        type(start), type(stop) == int, int
    except:
        raise TypeError
    return [x for x in range(start, stop+1) if x % 2 != 0]


if __name__ == "__main__":
    import unittest

    # Running test cases.
    class TestOddNumbers(unittest.TestCase):
        def test_type_error(self):
            with self.assertRaises(TypeError):
                oddNumbers("one", "two")

        def test_odd_numbers(self):
            self.assertEqual(oddNumbers(2, 7), [3, 5, 7])

    unittest.main()
