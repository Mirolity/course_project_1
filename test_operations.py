import unittest
from main import mask_card, mask_account


class TestBankOperations(unittest.TestCase):

    def test_mask_card(self):
        self.assertEqual(mask_card("1234567890123456"), "123456 78** **** 3456")

    def test_mask_account(self):
        self.assertEqual(mask_account("4081781067001234"), "**1234")


if __name__ == '__main__':
    unittest.main()