import pytest

from app import (
    add_to_cart,
    calculate_total,
    display_menu,
    place_order,
)


def test_menu_contains_five_items():
    assert len(display_menu()) == 5


def test_add_item_to_cart():
    cart = {}
    add_to_cart(cart, 1, 2)
    assert cart == {1: 2}


def test_calculate_total():
    cart = {1: 2, 2: 1}
    assert calculate_total(cart) == 497


def test_place_order():
    order = place_order({2: 2}, "Mayank")

    assert order["customer"] == "Mayank"
    assert order["total"] == 198
    assert order["status"] == "Order Placed"


def test_invalid_menu_item():
    with pytest.raises(ValueError):
        add_to_cart({}, 99, 1)


def test_invalid_quantity():
    with pytest.raises(ValueError):
        add_to_cart({}, 1, 0)


def test_empty_order_is_rejected():
    with pytest.raises(ValueError):
        place_order({}, "Mayank")


def test_customer_name_is_required():
    with pytest.raises(ValueError):
        place_order({1: 1}, "  ")
