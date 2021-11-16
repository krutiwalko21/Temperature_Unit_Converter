from temp_unit import conversion
import unittest

class TestTemperatureConversion(unittest.TestCase):

    def test_invalid(self):
        
        self.assertRaises(ValueError, conversion, -275, 'C', 'F')
        print('\ntest_invalid() function done!')

    def test_valid(self):

        test_cases = [((273.16, 'K',), (0.01, 'C')),
                      ((-40, 'C'), (-40, 'F')),
                      ((450, 'F'), (505.3722222222222, 'K'))]

        for test_case in test_cases:
            ((from_val, from_unit), (to_val, to_unit)) = test_case
            result = conversion(from_val, from_unit, to_unit)
            print(from_val, ' {} to {} is:'.format(from_unit,to_unit), result)
            self.assertAlmostEqual(to_val, result)
        print('\ntest_valid() function done!')

    def test_no_conversion(self):

        T = 56.67
        result = conversion(T, 'C', 'C')
        print('Conversion to same unit: ',result)
        self.assertEqual(result, T)
        print('\ntest_no_conversion() function done!')

    def test_bad_units(self):
        self.assertRaises(ValueError, conversion, 0, 'C', 'R')
        self.assertRaises(ValueError, conversion, 0, 'N', 'K')
        print('\ntest_bad_units() function done!')

unittest.main()


