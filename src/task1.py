def nameValidator(name):
    try:
        first_name, last_name = name.split()
    except:
        raise ValueError
    regex = re.compile(r'\d')
    regex = regex.search(name)
    if regex is None:
        pass
    else:
        raise ValueError

    if (len(first_name) >= 5 and len(first_name) <= 20) and (len(last_name) >= 5 and len(last_name) <= 20):
        return first_name, last_name
    else:
        raise IndexError


if __name__ == "__main__":
    import re
    import unittest

    # Running tests to check for vunerability
    class TestNameValidator(unittest.TestCase):
        def test_value_error(self):
            with self.assertRaises(ValueError):
                nameValidator("DennisChukwunta")

        def test_digit(self):
            with self.assertRaises(ValueError):
                nameValidator("Dennis2 Chukwunta")

        def test_lenght(self):
            with self.assertRaises(IndexError):
                nameValidator(
                    "Thisis notanameofanyhumanbeingorisitiyfgtyddfttcdftfxfgt")

        def test_return_value(self):
            self.assertEqual(nameValidator(
                "Dennis Chukwunta"), ("Dennis", "Chukwunta"))

    unittest.main()
