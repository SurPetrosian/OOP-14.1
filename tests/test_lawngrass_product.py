import pytest


def test_lawngrass_product_init(lawngrass_product1):
    assert lawngrass_product1.name == "Газонная трава"
    assert lawngrass_product1.description == "Элитная трава для газона"
    assert lawngrass_product1.price == 500.0
    assert lawngrass_product1.quantity == 20
    assert lawngrass_product1.country == "Россия"
    assert lawngrass_product1.germination_period == "7 дней"
    assert lawngrass_product1.color == "Зеленый"


def test_lawngrass_product_add(lawngrass_product1, lawngrass_product2):
    assert lawngrass_product1 + lawngrass_product2 == 16750.0


def test_lawngrass_product_error(lawngrass_product1):
    with pytest.raises(TypeError):
        lawngrass_product1 += 1
