from src.сategory import Category
from src.product import Product

if __name__ == "__main__":
    product1 = Product("Mercedes Bens S600", "Объем двигателя 4.0 литра,"
                                             " цвет черный, полный привод",
                       12500000.0, 10)
    product2 = Product("BMW X6M", "Объем двигателя 4.4 литра,"
                                  " цвет серый, полный привод",
                       10500000.0, 5)
    product3 = Product("AUDI A8", "Объем двигателя 4.0 литра,"
                                  " цвет белый, полный привод",
                       9500000.0, 12)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category("Автомобили", "Автомобили, как средство передвижения",
                         [product1, product2, product3])

    print(str(category1))
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)