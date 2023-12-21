from django.test import TestCase
from .utils import decimal_to_base62

class Base62ConversionTest(TestCase):
    def test_decimal_to_base62(self):
        test_cases = [
            (0, '0'),
            (12345, '3D7'),
            (987654321, '14q60P'),
            (1130000000, '1ETMcS'), # There are about 1.13 billion websites on the internet in 2023. Source: https://www.forbes.com/advisor/business/software/website-statistics/
        ]

        for decimal_num, expected_base62 in test_cases:
            with self.subTest(decimal_num=decimal_num, expected_base62=expected_base62):
                result = decimal_to_base62(decimal_num)
                self.assertEqual(result, expected_base62)