from shoppingcart.cart import ShoppingCart


def test_add_item():
    cart = ShoppingCart()
    cart.add_item("1", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 1 - €1.00"


def test_add_item_with_multiple_quantity():
    cart = ShoppingCart()
    cart.add_item("1", 2)

    receipt = cart.print_receipt()

    assert receipt[0] == "apple - 2 - €2.00"


def test_add_different_items():
    cart = ShoppingCart()
    cart.add_item("2", 1)
    cart.add_item("3", 1)

    receipt = cart.print_receipt()

    assert receipt[0] == "banana - 1 - €1.10"
    assert receipt[1] == "kiwi - 1 - €3.00"
