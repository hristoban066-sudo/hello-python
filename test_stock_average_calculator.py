import unittest

from stock_average_calculator import calculate_average_price


class TestCalculateAveragePrice(unittest.TestCase):
    def test_weighted_average(self):
        total_shares, total_cost, average = calculate_average_price(
            [(10, 100), (20, 80)]
        )
        self.assertAlmostEqual(total_shares, 30)
        self.assertAlmostEqual(total_cost, 2600)
        self.assertAlmostEqual(average, 86.6666667, places=5)

    def test_empty_input_raises(self):
        with self.assertRaises(ValueError):
            calculate_average_price([])

    def test_non_positive_shares_raises(self):
        with self.assertRaises(ValueError):
            calculate_average_price([(0, 100)])


if __name__ == "__main__":
    unittest.main()
