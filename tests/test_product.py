def test_product_init(product):
    assert product.name == "AUDI A8"
    assert product.description == "Объем двигателя 4.0 литра, " \
                                  "цвет белый, полный привод"
    assert product.price == 9500000.0
    assert product.quantity == 12
