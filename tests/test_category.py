import pytest


def test_category_init(category1, category2):
    assert category1.name == "Автомобили"
    assert category1.description == "Автомобили, как средство передвижения"
    assert len(category1.products_list) == 3

    assert category1.category_count == 2
    assert category2.category_count == 2

    assert category1.product_count == 4
    assert category2.product_count == 4


def test_add_product(category1, product):
    category1.add_product(product)
    assert len(category1.products_list) == 4


def test_add_product_error(category1):
    with pytest.raises(TypeError):
        category1.add_product(1)


def test_products_property(category1):
    assert category1.products == "Mercedes Bens S600, 12500000.0. " \
                                 "Остаток: 10." \
                                 "\nBMW X6M, 10500000.0. Остаток: " \
                                 "5.\nAUDI A8, 9500000.0. Остаток: 12.\n"


def test_sum_count(category1):
    assert category1.sum_count() == 27


def test_category_str(category1):
    assert str(category1) == 'Автомобили, количество продуктов: 27'
