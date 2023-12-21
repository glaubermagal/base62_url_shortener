from django.test import TestCase
from .utils import decimal_to_base66

class Base66ConversionTest(TestCase):
    def test_decimal_to_base66(self):
        test_cases = [
            (0, '0'),
            (12345, '2t3'),
            (987654321, 'q3OFR'),
            (1130000000, 'xaWK8'), # There are about 1.13 billion websites on the internet in 2023. Source: https://www.forbes.com/advisor/business/software/website-statistics/
        ]

        for decimal_num, expected_base66 in test_cases:
            with self.subTest(decimal_num=decimal_num, expected_base66=expected_base66):
                result = decimal_to_base66(decimal_num)
                self.assertEqual(result, expected_base66)

                