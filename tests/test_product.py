def test_product_init(product):
    assert product.name == "AUDI A8"
    assert product.description == "Объем двигателя 4.0 литра, " \
                                  "цвет белый, полный привод"
    assert product.price == 9500000.0
    assert product.quantity == 12


def test_price_property(product):
    assert product.price == 9500000.0


def test_price_setter(product):
    product.price = 120
    assert product.price == 120
    product.price = 0
    assert "Цена не должна быть нулевая или отрицательная"


def test_new_product(product):
    new_product1 = product.new_product({"name": "Jaguar F-TYPE",
                                        "description":
                                            "Объем двигателя 4.4 литра, "
                                        "цвет красный, задний привод",
                                        "price": 6000000.0,
                                        "quantity": 5})
    assert new_product1.name == "Jaguar F-TYPE"
    assert new_product1.description == "Объем двигателя 4.4 литра, " \
                                       "цвет красный, задний привод"
    assert new_product1.price == 6000000.0
    assert new_product1.quantity == 5


def test_add(product, product1):
    assert product + product1 == 166500000.0


def test_str(product):
    assert str(product) == 'AUDI A8, 9500000.0. Остаток: 12'
