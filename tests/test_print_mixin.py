from src.lawngrass_product import LawnGrass
from src.product import Product
from src.smartphone_product import Smartphone


def test_print_mixin(product, smartphone_product1, lawngrass_product1):
    assert Product("AUDI A8", "Объем двигателя 4.0 литра, "
                   "цвет белый, полный привод", 9500000.0, 12)
    assert Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                      "S23 Ultra", 256, "Серый")
    assert LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")