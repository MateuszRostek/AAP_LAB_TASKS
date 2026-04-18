# -*- coding: utf-8 -*-
"""Testy pytest dla klasy Product -- uzupelnij!

Uruchomienie: pytest test_product_pytest.py -v
"""

import pytest
from product import Product


# --- Fixture ---

@pytest.fixture
def product():
    """Tworzy instancje Product do testow (odpowiednik setUp)."""

    return Product("Laptop", 3000.0, 10)


# --- Testy z fixture ---

def test_is_available(product):
    """Sprawdz dostepnosc produktu."""

    assert product.is_available()


def test_total_value(product):
    """Sprawdz wartosc calkowita."""

    expected_total_value = product.price * product.quantity
    assert product.total_value() == expected_total_value


# --- Testy z parametryzacja ---

@pytest.mark.parametrize("amount, expected_quantity", [
    (5, 15),
    (0, 10),
    (100, 110),
])
def test_add_stock_parametrized(product, amount, expected_quantity):
    """Testuje add_stock z roznymi wartosciami."""

    product.add_stock(amount)
    assert product.quantity == expected_quantity


# --- Testy bledow ---

def test_remove_stock_too_much_raises(product):
    """Sprawdz, czy proba usuniecia za duzej ilosci rzuca ValueError."""

    with pytest.raises(ValueError):
        product.remove_stock(product.quantity + 11)


def test_add_stock_negative_raises(product):
    """Sprawdz, czy ujemna wartosc w add_stock rzuca ValueError."""

    with pytest.raises(ValueError):
        product.add_stock(-11)


@pytest.mark.parametrize("percent, expected_price", [
    (0, 3000.0),
    (50, 1500.0),
    (75, 750.0),
    (100, 0.0),
])
def test_apply_discount(product, percent, expected_price):
    product.apply_discount(percent)
    assert product.price == expected_price


@pytest.mark.parametrize("percent", [
    2484,
    101,
    -1,
    -1247,
])
def test_apply_discount_wrong_percentage_raises(product, percent):
    with pytest.raises(ValueError):
        product.apply_discount(percent)
