# -*- coding: utf-8 -*-
"""Testy unittest dla klasy Product -- uzupelnij metody testowe!

Uruchomienie: python -m unittest test_product_unittest -v
"""

import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Przygotuj instancje Product do testow."""

        self.product = Product("Laptop", 2999.99, 10)

    # --- Testy add_stock ---

    def test_add_stock_positive(self):
        """Sprawdz, czy dodanie towaru zwieksza quantity."""

        amount = 10
        previous_quantity = self.product.quantity
        self.product.add_stock(amount)
        self.assertEqual(previous_quantity + amount, self.product.quantity)

    def test_add_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""

        negative_amount = -10
        with self.assertRaises(ValueError):
            self.product.add_stock(negative_amount)

    # --- Testy remove_stock ---

    def test_remove_stock_positive(self):
        """Sprawdz, czy usuniecie towaru zmniejsza quantity."""

        previous_quantity = self.product.quantity
        amount = previous_quantity - 1
        self.product.remove_stock(amount)
        self.assertEqual(previous_quantity - amount, self.product.quantity)

    def test_remove_stock_too_much_raises(self):
        """Sprawdz, czy proba usuniecia wiecej niz jest dostepne rzuca ValueError."""

        previous_quantity = self.product.quantity
        excessive_amount = previous_quantity + 1
        with self.assertRaises(ValueError):
            self.product.remove_stock(excessive_amount)

    def test_remove_stock_negative_raises(self):
        """Sprawdz, czy ujemna wartosc rzuca ValueError."""

        negative_amount = -10
        with self.assertRaises(ValueError):
            self.product.remove_stock(negative_amount)

    # --- Testy is_available ---

    def test_is_available_when_in_stock(self):
        """Sprawdz, czy produkt z quantity > 0 jest dostepny."""

        self.assertTrue(self.product.is_available())

    def test_is_not_available_when_empty(self):
        """Sprawdz, czy produkt z quantity == 0 nie jest dostepny."""

        empty_product = Product("Mouse", 200, 0)
        self.assertFalse(empty_product.is_available())

    # --- Testy total_value ---

    def test_total_value(self):
        """Sprawdz, czy total_value zwraca price * quantity."""

        price = self.product.price
        quantity = self.product.quantity
        self.assertEqual(price * quantity, self.product.total_value())


if __name__ == "__main__":
    unittest.main()
