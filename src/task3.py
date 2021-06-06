def dictComp(stop, step):
    try:
        type(stop), type(step) == int, int
    except:
        raise TypeError
    answer = {}  # A dictionary to hold the Items
    count = 0  # A count to calculate steps
    dictionary_items_count = 1
    for number in range(1, stop+1):

        if count == 0:
            # We need to add a new Item to the dictionary
            answer["items-{}".format(dictionary_items_count)] = [number]
            dictionary_items_count += 1
            count = 1
        else:
            # Get the most recently inserted key and append the numbers to it
            last_key = list(answer.keys())[-1]
            answer[last_key].append(number)
            count += 1
        if count == step:
            # If the count is up to step. We reset count and check if the remainder of the range of numbers is enough to fill up another Item.
            count = 0
            if stop-number < step:
                # If not we break from the loop prematurely.
                break

    return answer


if __name__ == "__main__":
    import unittest

    class Test_DictComp(unittest.TestCase):
        def test_typeError(self):
            with self.assertRaises(TypeError):
                dictComp("200", 10)

        def test_dict_length(self):
            # Testing correctness using the length of the Items in the dictionary
            self.assertEqual(len(dictComp(10, 4)), 2)
            self.assertEqual(len(dictComp(8, 2)), 4)
            self.assertEqual(len(dictComp(100, 0)), 1)

        def test_item_length(self):
            # Testing correctness using the length of each list of values for each item in the dictionary
            test_case_1 = dictComp(200, 13)
            for each_key, value in test_case_1.items():
                self.assertEqual(len(value), 13)

    unittest.main()
